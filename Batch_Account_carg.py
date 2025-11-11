
import requests
import json
import boto3
from datetime import date
from datetime import datetime
from decouple import config

CSP="Azure"
'''bucket_name="carg-qradar-cw-logs"
s3 = boto3.client('s3',aws_access_key_id=config('ACCESS_KEY'),
            aws_secret_access_key=config('SECRET_KEY'))'''

Resource="Batch accounts"	
Assets = "Batch account"	

def send_to_CARGapi(body):
    url = config('URL')
    payload = body
    headers = {
        'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)
    print(" CARG API invoked successfully ...")

'''def send_to_s3(compliant,non_compliant,Policyname):
    #response=s3.put_object(Body=compliant, Bucket=bucket_name, Key=CSP+'/'+Resource+'/'+Assets+'/'+Policyname+'/Compliant/'+str(datetime.now())+'.json')
    #response=s3.put_object(Body=non_compliant, Bucket=bucket_name, Key=CSP+'/'+Resource+'/'+Assets+'/'+Policyname+'/Noncompliant/'+str(datetime.now())+'.json')
    print("done")
'''
def p367_send(nc_body,c_body):
    comp_message_list=json.dumps(c_body)
    message_list=json.dumps(nc_body)
    Policyname = "Resource logs in Batch accounts should be enabled"
    send_to_CARGapi(message_list)
    #send_to_s3(comp_message_list,message_list,Policyname)

def p368_send(nc_body,c_body):
    comp_message_list=json.dumps(c_body)
    message_list=json.dumps(nc_body)
    Policyname = "Public network access should be disabled for Batch accounts"
    send_to_CARGapi(message_list)
    #send_to_s3(comp_message_list,message_list,Policyname)

def p369_send(nc_body,c_body):
    comp_message_list=json.dumps(c_body)
    message_list=json.dumps(nc_body)
    Policyname = "Azure Batch account should use customer-managed keys to encrypt data"
    send_to_CARGapi(message_list)
    #send_to_s3(comp_message_list,message_list,Policyname)

def p370_send(nc_body,c_body):
    comp_message_list=json.dumps(c_body)
    message_list=json.dumps(nc_body)
    Policyname = "Ensure that the API authentication mechanism for a Batch account is restricted to only Azure AD"
    send_to_CARGapi(message_list)
    #send_to_s3(comp_message_list,message_list,Policyname)
