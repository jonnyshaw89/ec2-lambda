# EC2 stopper Lambda

## Structure

### Lambda
This Python lambda takes a string value and stops all EC2 instances that contain that value with in the instances `Name` tag

A sample payload is shown below

```
{
  "Name": "Rowden"
}
```

#### Developing
If you would like to develop this lambda locally here are some tools you will need

- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

There is a Makefile with commands you will need, these include the following amoung others:
- `make build`
- `make test`
- `make run`
- `make zip`


### Terraform 
The Terraform is provided to deploy this lambda into an AWS environment.
This deploys a zip of the lambda into the environment so it can be triggered manually or by another process.

The backend state for this terraform is stored in S3

### GitHub actions
This repo contains 2 github actions

#### PR check
This action checks PRs that are raised against the `main` branch to ensure that the Terraform is valid and that the 
python for the lambda is correctly formatted and that the unit tests pass.

#### Deployment
There is a deployment action that runs when a PR is merged to the main branch.
This action builds and packages the Lambda, then runs the Terraform to deploy this Lambda into AWS