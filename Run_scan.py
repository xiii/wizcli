import boto3
import sys

def create_user_data():
    sts = boto3.client('sts')
    sess = boto3.session.Session()
    aws_region = sess.region_name
    account_id = boto3.client('sts').get_caller_identity()['Account']

    ami_id = sys.argv[1]

    user_data1 = \
'''#!/bin/bash
curl -o /usr/local/bin/wizcli https://wizcli.app.wiz.io/wizcli
chmod +x /usr/local/bin/wizcli
export WIZ_DIR="/root/.wiz"
/usr/local/bin/wizcli auth --id FOFOFOFOFOFOFOOOOOOOOOOOOOOO --secret FOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
/usr/local/bin/wizcli vm-image scan --region '''
    user_data2 = f"{aws_region} --subscriptionId {account_id} -p wiz-cli-test-aci --id {ami_id}"

    user_data = user_data1 + user_data2

    print (user_data)
    return user_data

def create_instance():
    ec2=boto3.client('ec2')
    
    try:
        response = ec2.run_instances(
                MinCount = 1,
                MaxCount = 1,
                DryRun = True,
                ImageId = 'ami-04dd4500af104442f', 
                InstanceType = 't3.medium',
                KeyName = 'Sandbox-gary',
                NetworkInterfaces = [{
                    'DeviceIndex': 0,
                    'AssociatePublicIpAddress' : True,
                    'SubnetId' : 'subnet-0e87082d4ed6d7e2c',
                    'Groups' : ['sg-0f1b49fa9957e9f33']
                }],
                UserData = create_user_data()
        )
        print(response)
    except Exception as e:
        print(e)

def main():
    create_instance()

if __name__ == "__main__":
    main()







