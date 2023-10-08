import boto3
import time

aws_region = "us-east-2"
security_group_name = "myapp-sg" 

def get_security_group_id(ec2):
    response = ec2.describe_security_groups(
        Filters=[{'Name': 'group-name', 'Values': [security_group_name]}]
    )
    if response['SecurityGroups']:
        return response['SecurityGroups'][0]['GroupId']
    else:
        raise ValueError(f"Security group '{security_group_name}' not found.")
    
def add_ssh_rule(ec2):
    try:
        security_group_id = get_security_group_id(ec2)
        response = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpProtocol="tcp",
            FromPort=22,
            ToPort=22,
            CidrIp="0.0.0.0/0"
        )
        print("SSH rule added successfully.")
    except Exception as e:
        print("Error adding SSH rule:", str(e))

def main():

   
    ec2 = boto3.client("ec2", region_name=aws_region)

    # Uncomment the function calls you want to test
   
    
    add_ssh_rule(ec2)
    time.sleep(20)  # Wait for 20 seconds
if __name__ == "__main__":
    main()
