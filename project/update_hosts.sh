#!/bin/bash
Get_EC2_IP() {
  
    EC2_IP=$(terraform output server-ip)
}

Update_Inventory() {
    echo "It's Updating Ansible inventory"
    inventory_file="../ansible/hosts"

    # Replace the IP address of the target host in the inventory file
    echo -e "${EC2_IP} ansible_ssh_private_key_file=tim.pem ansible_user=ec2-user" > "${inventory_file}"

    echo "server-ip is ${EC2_IP}"
}


Get_EC2_IP
Update_Inventory