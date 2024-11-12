# ChMS AI Function App

Function app to process user prompts to produce SQL
- works off an Azure queue
- utilizes AWS Bedrock for LLM model execution
- persists results to CosmoDb

## Config
```
export USE_KEY_VAULT="false"
export QUEUE=""
export LLM_MODEL="anthropic.claude-3-haiku-20240307-v1:0"
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export COSMO_ACCOUNT_NAME=""
export COSMO_ENDPOINT=""
export COSMO_DATABASE_NAME=""
export COSMO_CONTAINER_NAME=""
export AZURE_SUBSCRIPTION_ID=""
export AZURE_RESOURCE_GROUP=""
export SQL_USERNAME=""
export SQL_PASSWORD=""
export SQL_DATABASE_SERVER=""
export SQL_DATABASE_NAME=""
```
## local.settings.json

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "AzureWebJobsQueueConnectionString": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing"
  }
}
```

## Example Message
```
{
    "user_id": "12345-67890",
    "completion_id": "1234567890",
    "diocese_id": 0,
    "church_id": 0,
    "user_prompt": "how many members do we have"
}
```

