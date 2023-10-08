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

def delete_ssh_rule(ec2):
    try:
        security_group_id = get_security_group_id(ec2)
        response = ec2.describe_security_groups(GroupIds=[security_group_id])
        existing_ingress = response['SecurityGroups'][0]['IpPermissions']
    
        updated_ingress = [rule for rule in existing_ingress if not (
            rule['IpProtocol'] == 'tcp' and
            rule['FromPort'] == 22 and
            rule['ToPort'] == 22 and
            {'CidrIp': '0.0.0.0/0'} in rule.get('IpRanges', [])
        )]
    
        # Revoke all ingress rules for the security group
        ec2.revoke_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=existing_ingress
        )

        # Authorize the updated ingress rules back to the security group
        for rule in updated_ingress:
            ec2.authorize_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=[rule]
            )

        print("SSH rule deleted successfully.")
    except Exception as e:
        print("Error deleting SSH rule:", str(e))

def main():
    ec2 = boto3.client("ec2", region_name=aws_region)

    # Uncomment the function calls you want to test
    delete_ssh_rule(ec2)

if __name__ == "__main__":
    main()