
import boto3
from sagemaker import get_execution_role
## The SageMaker role executing your notebook needs to have Lambda permissions.
import json

client = boto3.client('lambda')

payload = {'key': 'value'}

payload_bytes = json.dumps(payload).encode('utf-8')

response = client.invoke(
    FunctionName='example123',
    InvocationType='Event',
    Payload=payload_bytes
)
