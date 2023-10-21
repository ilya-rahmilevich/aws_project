#!/bin/python3

import boto3

instance_id = input("Please enter which instance id do you want to start: ")
resource_ec2 = boto3.client("ec2")
resource_ec2.start_instances(InstanceIds=[instance_id])
