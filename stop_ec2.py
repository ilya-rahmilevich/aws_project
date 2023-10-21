#!/bin/python3

import boto3

instance_id = "i-05512825c98054894"
resource_ec2 = boto3.client("ec2")
resource_ec2.stop_instances(InstanceIds=[instance_id])
