#!/bin/bash
aws ec2 run-instances   --image-id ami-04dd4500af104442f \
                        --instance-type t3.medium \
                        --key-name Sandbox-gary \
                        --security-group-ids sg-0f1b49fa9957e9f33 \
                        --subnet-id subnet-0e87082d4ed6d7e2c \
                        --associate-public-ip-address \
                        --user-data file://userdata.sh

