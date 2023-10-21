#!/bin/python3

import boto3

resource_ec2 = boto3.client("ec2")
print(resource_ec2.describe_instances())
