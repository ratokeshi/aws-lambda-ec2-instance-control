import boto3   
region = 'us-east-1'
tagvalue = 'mbiii'
lstinstance = list(())
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:usecase',
                'Values': [tagvalue]
            }
        ]
    )
    
    

    

    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This sample print will output entire Dictionary object
            #print(instance)
            # This will print will output the value of the Dictionary key 'InstanceId'
            instancerunning = instance["InstanceId"]
            lstinstance.append(instancerunning)
            print(instance["InstanceId"])

    return {
        'instances' : lstinstance
    }
