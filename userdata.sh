#!/bin/bash

curl -o /usr/local/bin/wizcli https://wizcli.app.wiz.io/wizcli
chmod +x /usr/local/bin/wizcli
export WIZ_DIR="/root/.wiz"
/usr/local/bin/wizcli auth --id 4c86B8BpuNm4VoQ0DbaNGjlil8QFxHnm --secret NdOLFfxajRAv_GWTEmh8S56Bpqc3VDKB2S1kjtmkmXKbU55ovjh3aff0_5vHudbv
/usr/local/bin/wizcli vm-image scan   --region eu-west-1 --subscriptionId 752803879791 -p wiz-cli-test-aci --id ami-074b4511adeac08ab

