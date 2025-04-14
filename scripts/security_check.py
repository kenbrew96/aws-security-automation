python
import boto3
client = boto3.client('iam')
users = client.list_users()['Users']
for user in users:
    print(f"User: {user['UserName']}")
