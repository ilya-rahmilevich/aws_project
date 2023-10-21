
#!/bin/python3

import boto3

# Create a new EC2 instance
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-0261755bbcb8c4a84",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="Ilya_key_pair"
)
