## PROJECT 6: AWS Security Automation

### 📁 GitHub Structure
```
aws-security-automation/
├── security_check.py
```

### 📄 `security_check.py`
```python
import boto3
client = boto3.client('iam')
users = client.list_users()['Users']
for user in users:
    print(f"User: {user['UserName']}")
```
**Explanation**: Uses boto3 to list IAM users in your AWS account.
