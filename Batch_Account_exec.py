import requests
import json
import sys
from decouple import config
from Batch_Account_policy import *
from Batch_Account_carg import *

non_status = "Open"
com_status = "Closed"

non367,non368,non369,non370=([] for i in range(4))
com367,com368,com369,com370=([] for i in range(4))

def authentication(url,headers,payload):
    response = requests.request("POST", url, headers=headers, data = payload)
    return json.loads(response.text).get('access_token')

def list_subscription(head):
    url1 ="https://management.azure.com/subscriptions?api-version=2020-01-01"
    r = requests.request("GET", url1, headers=head)
    return json.loads(r.text).get('value',[]) 

def list_batchacc(subscription_id,head):
    url1 ="https://management.azure.com/subscriptions/"+subscription_id+"/providers/Microsoft.Batch/batchAccounts?api-version=2022-01-01"
    r = requests.request("GET", url1, headers=head)
    return json.loads(r.text).get('value',[]) 

def get_diagnostics(resourceId,head):
    diagnostic_url="https://management.azure.com/"+resourceId+"/providers/microsoft.insights/diagnosticSettings?api-version=2021-05-01-preview"
    req = requests.request("GET", diagnostic_url, headers=head)
    return json.loads(req.text).get('value',[])

def main(subscription_id,head):
    count=0
    BatchAccount=list_batchacc(subscription_id,head)
    for batch_acc in BatchAccount:
        name = batch_acc['name']
        location = batch_acc['location']
        rg=(batch_acc['id'].split("/"))[4]
        asset_id=rg+"/"+name
        resourceId = batch_acc['id']
        diagnostics = get_diagnostics(resourceId,head)
        for log in diagnostics:
            logs=log['properties']['logs']
            for logdata in logs:
                enabled=logdata['enabled']
                retentionenabled=logdata['retentionPolicy']['enabled']
                retentiondays=logdata['retentionPolicy']['days']
                if enabled is True:
                    if retentionenabled==False:
                        count=count+1
                    
                    if retentionenabled==True:
                        if retentiondays==0 or retentiondays>29:
                            count=count+1

        if count>0:
            com367.append(p367(name,location,com_status,subscription_id))
        else:
            non367.append(p367(name,location,non_status,subscription_id))

        publicNetworkAccess=batch_acc['properties']['publicNetworkAccess']
        if publicNetworkAccess=="Enabled":
            non368.append(p368(name,location,non_status,subscription_id))
        else:
            com368.append(p368(name,location,com_status,subscription_id))
    
        keySource=batch_acc['properties']['encryption']['keySource']
        if keySource!="Microsoft.KeyVault":
            non369.append(p369(name,location,non_status,subscription_id))
        else:
            com369.append(p369(name,location,com_status,subscription_id))

        allowedAuthenticationModes=batch_acc['properties']['allowedAuthenticationModes']
        if 'AAD' in allowedAuthenticationModes and len(allowedAuthenticationModes)==1:
            com370.append(p370(name,location,com_status,subscription_id))
        else:
            non370.append(p370(name,location,non_status,subscription_id))
    
    p367_send(non367,com367)
    p368_send(non368,com368)
    p369_send(non369,com369)
    p370_send(non370,com370)

if __name__=='__main__':
    tenant_ID = config('AZURE_TENANT') 
    client_id = config('AZURE_CLIENT') 
    client_secret = config('AZURE_SECRET') 

    # STATIC VARIABLES, DO NOT CHANGE
    grant_type = "client_credentials"
    resource = "https://management.azure.com/"
    
    url = "https://login.microsoftonline.com/"+tenant_ID+"/oauth2/token"
    payload = 'client_id='+client_id+'&client_secret='+client_secret+'&grant_type='+grant_type+'&resource='+resource
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}   

    # sending request to authorize api request. The generated access token is stored in a variable 
    response = requests.request("POST", url, headers=headers, data = payload)
    token = json.loads(response.text)['access_token']
    head={'Authorization': 'bearer '+token}
    subscriptions = list_subscription(head)
    for subscription in subscriptions:
        main(subscription['subscriptionId'],head)
