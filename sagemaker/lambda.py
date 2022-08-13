%%writefile lambda_function.py

import json

def lambda_handler(event,context):
    return {
        'statusCode':200,
        'body': json.dumps("Hello")
    }


import boto3

from sagemaker import get_execution_role
from zipfile import ZipFile
role = get_execution_role()
client = boto3.client('lambda')

#lambda functions must be zipped
with ZipFile('code.zip', 'w') as f:
    f.write('lambda_function.py')

# If submitting as a ZipFile, you need to insert raw data.
with open('code.zip', 'rb') as f:
    b_code = f.read()

response = client.create_function(
    FunctionName='botoLambdaFunction1',
    Runtime='python3.9',
    Handler='lambda_function.lambda_handler',#name of file and function inside of file
    Code={
        'ZipFile': b_code
    },
    Description='string',
    Timeout=30,
    MemorySize=1024,
    Publish=True,
    PackageType='Zip',
    Role='arn:aws:iam::565094796913:role/lambda_full_access'
)
