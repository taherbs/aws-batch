# AWS Batch
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/taherbs/aws-batch/master/LICENSE)

## Description
This is sample project that deploys a python application on AWS batch (on-demand).
This project is meant to be a tutorial/sample for deploying an AWS batch application.
The python job will print current system info.

## Prerequisites
- [Docker](https://docs.docker.com/)/[Docker Compose](https://docs.docker.com/compose/)
- [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- [sceptre](https://sceptre.cloudreach.com/latest/)

## Run python job in local (Docker/Docker-compose)
Build container
* `docker-compose build`

run container
* `docker-compose up`

## Creating the AWS pipeline and batch infrastructure

### Install Requirements
The project needs python3 to be installed prior.
You can install the project requirements running this command.

```
# Optional - Install and load Virtualenv
pip3 install virtualenv
virtualenv env
source env/bin/activate

# Install required packages
pip3 install -r requirements.txt

# build sceptre hooks and resolvers
cd infrastructure/sceptre && for dir in {./resolvers/*,./hooks/*}; do (cd "$dir" && pip install .); done
```

### Configure AWS credentials
Make sure to load credentials with the admin privileges.
* ```aws configure```

### Set AWS pipeline and batch infrastructure entry parameters
Edit the [sceptre yaml config file](./infrastructure/sceptre/config/config.yaml) and set the parameters values.

### Deploy the AWS pipeline and batch infrastructure via sceptre
```
# cd the sceptre directory
cd infrastructure/sceptre

# Deploy the environment
## Deploy the pipeline infrastructure
sceptre launch aws

## Deploy the batch infrastructure for staging environment
sceptre launch stg

## Deploy the batch infrastructure for production environment
sceptre launch prd
```

* **Important Note:** it seems like cloudformation does not support creating cloudwatch event to scheduled batch jobs yet. creating the cloudwatch event is manual for the moment.
Documentation of how to create a [AWS Batch Jobs as CloudWatch Events Targets](https://docs.aws.amazon.com/batch/latest/userguide/batch-cwe-target.html)
