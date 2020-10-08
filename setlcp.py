import json
import boto3
import os
import sys

def die(msg):
  print(msg)
  sys.exit(-1)

if os.environ.get('access_key') is not None:
   akey = os.environ.get('access_key')
else:
   die("Set the access_key in the environment file")

if "secret_key" in os.environ:
   skey = os.environ.get('secret_key')
else:
   die("Set the secret_key in the environment file")

if "endpoint_url" in os.environ:
   eurl = os.environ.get('endpoint_url')
else:
   die("Set the endpoint_url in the environment file")

if "bucket" in os.environ:
   bkt = os.environ.get('bucket')
else:
   die("Set the bucket in the environment file")

if "noncurrent_days" in os.environ:
   ncd = int(os.environ.get('noncurrent_days'))
else:
   ncd = 1

s3 = boto3.resource(service_name='s3', verify=False, 
     aws_access_key_id=akey,
     aws_secret_access_key=skey,
     endpoint_url=eurl)

s3.meta.client.put_bucket_lifecycle_configuration (
  Bucket=bkt,
  LifecycleConfiguration={
    'Rules': [
      {
        'ID' : 'rule1',
        'Filter' : {
           'Prefix' : '/',
        },
        'Status' : 'Enabled',
        'NoncurrentVersionExpiration': {
           'NoncurrentDays': ncd
        },
     }
   ]
  }
)
