output "dev-vpc-id" {

  value = aws_vpc.myapp-vpc.id
}

output "dev-subnet-id" {

  value = aws_subnet.dev-subnet-1.id
}

output "dev-route-table-id" {
  value = aws_route_table.myapp-route-table.id
}

output "dev-internet-gateway-id" {
  value = aws_internet_gateway.myapp-igw.id
}

output "server-id" {
  value = aws_instance.myapp-server.id
}

output "server-ip" {
  value = aws_instance.myapp-server.public_ip
}

output "security_group_id" {
  value = aws_security_group.myapp-sg.id
}