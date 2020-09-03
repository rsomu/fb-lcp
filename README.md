# fb-lcp
 Managing Lifecycle policy on Pure Storage FlashBlade object storage.

 Docker image with custom python scripts to manage the life cycle policy for a bucket on FlashBlade.

## Build the docker image
   Make sure the python scripts (setlcp.py, getlcp.py, rmlcp.py) are in the same directory as the Dockerfile is.

Usage
```
   docker build -t fb-lcp .
```

## Prerequisites to run the python scripts
 Requires an environment file with the following values set.
 (Follow your standard security procedures to protect the environment file)

``` 
   access_key=<access key>
   secret_key=<secret key>
   endpoint_url=http://<FB-datavip>
   bucket=<bucket-name>
   noncurrent_days=<integer>
```

If noncurrent_days is not set, default of 1 day is assumed.

## Setting a Lifecycle policy for a bucket on FlashBlade

  Make sure to set the environment file as stated above before running the script.

Usage
```
  docker run --rm --env-file=<envfile> fb-lcp python ./setlcp.py
```

## Listing the Lifecycle policy for a bucket on FlashBlade

  Make sure to set the environment file as stated above before running the script as the bucket name is passed through environment variables along with access key, secret key and the FB datavip.

Usage
```
  docker run --rm --env-file=<envfile> fb-lcp python ./getlcp.py
```

## Removing the Lifecycle policy for a bucket on FlashBlade

  Make sure to set the environment file as stated above before running the script.

Usage
```
  docker run --rm --env-file=<envfile> fb-lcp python ./rmlcp.py
```
