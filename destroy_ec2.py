#!/bin/python3

import boto3

instance_id = input("Please enter which instance id do you to terminate: ") 
resource_ec2 = boto3.client("ec2")
resource_ec2.terminate_instances(InstanceIds=[instance_id])
