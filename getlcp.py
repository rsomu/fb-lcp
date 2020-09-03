import boto3
import json
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

try:
  s3 = boto3.resource(service_name='s3', use_ssl=False, 
       aws_access_key_id=akey,
       aws_secret_access_key=skey,
       endpoint_url=eurl)

  print ("Life cycle config of "+bkt+" on "+eurl)
  print(json.dumps(s3.meta.client.get_bucket_lifecycle_configuration ( Bucket=bkt), indent=4))
except Exception as e:
  die(e)
