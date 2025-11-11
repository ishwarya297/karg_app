from datetime import date
from datetime import datetime
from decouple import config

t=datetime.now()
x = t.replace(microsecond=0)
Time = int(datetime.timestamp(x))

Resource="Batch accounts"	
Assets = "Batch account"

def output(Policyname,location,asset_id,Status,Description,Recommendation,subscription_id):
    if Status=="Open":  
          
        json_obj={
                    "Source" : "Native service - Azure",
                    "PolicyName": Policyname,
                    "CloudType": "Azure",
                    "CloudAccountId": subscription_id,
                    "ResourceRegion": location,
                    "Resource": Resource,
                    "Assets": Assets,
                    "AssetId": asset_id,
                    "Status": Status,
                    "OpenedAt" : Time,
                    "ClosedAt": "Nil",
                    "Description": Description,
                    "Recommendation": Recommendation
                }
    else:
        json_obj={
                    "Source" : "Native service - Azure",
                    "PolicyName": Policyname,
                    "CloudType": "Azure",
                    "CloudAccountId": subscription_id,
                    "ResourceRegion": location,
                    "Resource": Resource,
                    "Assets": Assets,
                    "AssetId": asset_id,
                    "Status": Status,
                    "OpenedAt" : "Nil",
                    "ClosedAt": Time,
                    "Description": Description,
                    "Recommendation": Recommendation
                }
    return json_obj

def p367(asset_id,location,Status,subscription_id):
    Policyname = "Resource logs in Batch accounts should be enabled"
    Description = "Audit enabling of resource logs. This enables you to recreate activity trails to use for investigation purposes; when a security incident occurs or when your network is compromised"  
    Recommendation  = "1. In the Azure portal, select All services > Batch accounts, and then select the name of your Batch account. 2. Under Monitoring, select Diagnostic settings. 3. In Diagnostic settings, select Add diagnostic setting. 4. Enter a name for the setting. 5. Select a destination: Send to Log Analytics, Archive to a storage account, or Stream to an event hub. If you select a storage account, you can optionally select the number of days to retain data for each log. If you don't specify a number of days for retention, data is retained during the life of the storage account. 6. Select ServiceLog, AllMetrics, or both. 7. Select Save to create the diagnostic setting."    
    return output(Policyname,location,asset_id,Status,Description,Recommendation,subscription_id)

def p368(asset_id,location,Status,subscription_id):
    Policyname = "Public network access should be disabled for Batch accounts"
    Description = "Disabling public network access on a Batch account improves security by ensuring your Batch account can only be accessed from a private endpoint. Learn more about disabling public network access at https://docs.microsoft.com/azure/batch/private-connectivity."  
    Recommendation  = "Once a Batch account is created with public network access, you can't change it to private access only"    
    return output(Policyname,location,asset_id,Status,Description,Recommendation,subscription_id)

def p369(asset_id,location,Status,subscription_id):
    Policyname = "Azure Batch account should use customer-managed keys to encrypt data"
    Description = "Use customer-managed keys to manage the encryption at rest of your Batch account's data. By default, customer data is encrypted with service-managed keys, but customer-managed keys are commonly required to meet regulatory compliance standards. Customer-managed keys enable the data to be encrypted with an Azure Key Vault key created and owned by you. You have full control and responsibility for the key lifecycle, including rotation and management. Learn more at https://aka.ms/Batch-CMK."  
    Recommendation  = "1. The keys you provide must be generated in Azure Key Vault, and they must be accessed with managed identities for Azure resources. 2. You can either create your Batch account with system-assigned managed identity, or create a separate user-assigned managed identity that will have access to the customer-managed keys. 3. In the Azure portal, go to the Batch account page. 4. Under the Encryption section, enable Customer-managed key. 5. You can directly use the Key Identifier, or you can select the key vault and then click Select a key vault and key."    
    return output(Policyname,location,asset_id,Status,Description,Recommendation,subscription_id)

def p370(asset_id,location,Status,subscription_id):
    Policyname = "Ensure that the API authentication mechanism for a Batch account is restricted to only Azure AD"
    Description = "Batch account access supports two methods of authentication: Shared Key and Azure Active Directory (Azure AD). Azure strongly recommend using Azure AD for Batch account authentication. The service API authentication mechanism for a Batch account can be restricted to only Azure AD using the allowedAuthenticationModes property. When this property is set, API calls using Shared Key authentication will be rejected."  
    Recommendation  = "1. In the Azure portal, go to Batch account page. 2. Under Settings section, click on Authentication mode. 3. Make sure only 'Azure Active Directory' is selected. For more info, refer https://docs.microsoft.com/en-in/azure/batch/batch-aad-auth"    
    return output(Policyname,location,asset_id,Status,Description,Recommendation,subscription_id)
