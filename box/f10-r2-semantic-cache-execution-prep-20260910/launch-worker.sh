#!/bin/bash
set -euo pipefail
test ! -e box/f10-r2-semantic-cache-execution-prep-20260910/launch-response.json
test "$(sha256sum xmodel/f10-r2-native-cache-correction-gate-fable5-20260910.md | cut -d ' ' -f 1)" = b7a6aa2590f4695a646f776c1493f80f9f4dcb24b9e8c00d78aa4548d694140a
test "$(sha256sum box/f10-r2-semantic-runtime-astra-20260910/dispatch.py | cut -d ' ' -f 1)" = 6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 15:52:00 UTC' +%s)"
/usr/local/bin/aws ec2 run-instances --region us-east-1 --image-id ami-066263bf15bd856de --instance-type c7i.xlarge --count 1 --key-name jc2-fleet --security-group-ids sg-09ffa8932558f0a79 --subnet-id subnet-948915c9 --associate-public-ip-address --user-data file://box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml --enable-api-termination --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"DeleteOnTermination":false}}]' --client-token jc2-r2-controls-cache-20260910T1545 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=jc2-r2-controls-cache-20260910T1545},{Key=jc2fleet,Value=1},{Key=market,Value=ondemand},{Key=Owner,Value=root-r2-controls-cache-20260910T1545}]' --query 'Instances[].{ID:InstanceId,State:State.Name,PrivateIP:PrivateIpAddress,Type:InstanceType,Launched:LaunchTime,Devices:BlockDeviceMappings}' --output json > box/f10-r2-semantic-cache-execution-prep-20260910/launch-response.json
test "$(jq 'length' box/f10-r2-semantic-cache-execution-prep-20260910/launch-response.json)" = 1
jc2_controlscache_instance=$(jq -r '.[0].ID' box/f10-r2-semantic-cache-execution-prep-20260910/launch-response.json)
[[ "$jc2_controlscache_instance" =~ ^i-[0-9a-f]+$ ]]
systemd-run --user --unit=jc2-r2-controlscache-workerterm-20260910T1545 --on-calendar='2026-09-10 16:18:00 UTC' --timer-property=AccuracySec=1s /usr/local/bin/aws ec2 terminate-instances --region us-east-1 --instance-ids "$jc2_controlscache_instance"
systemctl --user is-active jc2-r2-controlscache-workerterm-20260910T1545.timer
date -u '+ORIGINAL_WORKER_TERMINATION_ARMED %Y-%m-%d %H:%M:%S.%N UTC'
sed -n '1,150p' box/f10-r2-semantic-cache-execution-prep-20260910/launch-response.json
/usr/local/bin/aws ec2 describe-instance-attribute --region us-east-1 --instance-id "$jc2_controlscache_instance" --attribute disableApiTermination --output json
/usr/local/bin/aws ec2 describe-instances --region us-east-1 --instance-ids "$jc2_controlscache_instance" --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Private:PrivateIpAddress,Public:PublicIpAddress,Devices:BlockDeviceMappings}' --output json
