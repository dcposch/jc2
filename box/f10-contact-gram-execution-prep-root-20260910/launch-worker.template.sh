#!/bin/bash
# DISABLED ROOT worker-allocation template. No science, imports or provisioning.
set -euo pipefail
cd /home/ubuntu/jc2
jc2_contact_release=JC2_ROOT_WORKER_RELEASE_PLACEHOLDER
test "$jc2_contact_release" = RELEASED
if rg -n 'JC2_[A-Z_]+_PLACEHOLDER' "$0"; then exit 2; fi
test ! -e box/f10-contact-gram-execution-prep-root-20260910/launch-response.json
sha256sum -c box/f10-contact-gram-execution-prep-root-20260910/ROOT-READY-INPUTS.sha256
test "$(sha256sum box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml | cut -d ' ' -f 1)" = 0c5820cd60a44704a6d8118a7570a9327c1f2fe62939ff664b1f9b7cfaf42730
test "$(date -u +%s)" -lt "$(date -ud 'JC2_LATEST_WORKER_LAUNCH_UTC_PLACEHOLDER' +%s)"
# ROOT first verifies current exact tagged fleet, quota, complete offline packet,
# original setup/math/custody/termination ordering and the no-idle policy.
/usr/local/bin/aws ec2 run-instances --profile personal --region us-east-1 \
 --image-id ami-066263bf15bd856de --instance-type c7i.xlarge --count 1 \
 --key-name jc2-fleet --security-group-ids sg-09ffa8932558f0a79 \
 --subnet-id subnet-948915c9 --associate-public-ip-address \
 --user-data file://box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml \
 --enable-api-termination \
 --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"DeleteOnTermination":false}}]' \
 --client-token jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER \
 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER},{Key=jc2fleet,Value=1},{Key=market,Value=ondemand},{Key=Owner,Value=root-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER}]' \
 --query 'Instances[].{ID:InstanceId,State:State.Name,PrivateIP:PrivateIpAddress,Type:InstanceType,Launched:LaunchTime,Devices:BlockDeviceMappings}' \
 --output json > box/f10-contact-gram-execution-prep-root-20260910/launch-response.json
test "$(jq 'length' box/f10-contact-gram-execution-prep-root-20260910/launch-response.json)" = 1
jc2_contact_instance=$(jq -r '.[0].ID' box/f10-contact-gram-execution-prep-root-20260910/launch-response.json)
[[ "$jc2_contact_instance" =~ ^i-[0-9a-f]+$ ]]
systemd-run --user --unit=jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER-worker-stop \
 --on-calendar='JC2_WORKER_TERMINATION_UTC_PLACEHOLDER' --timer-property=AccuracySec=1s \
 /usr/local/bin/aws ec2 terminate-instances --profile personal --region us-east-1 \
 --instance-ids "$jc2_contact_instance"
systemctl --user is-active jc2-contact-gram-JC2_BATCH_SUFFIX_PLACEHOLDER-worker-stop.timer
date -u '+ORIGINAL_WORKER_TERMINATION_ARMED %Y-%m-%d %H:%M:%S.%N UTC'
sed -n '1,150p' box/f10-contact-gram-execution-prep-root-20260910/launch-response.json
/usr/local/bin/aws ec2 describe-instance-attribute --profile personal --region us-east-1 \
 --instance-id "$jc2_contact_instance" --attribute disableApiTermination --output json
/usr/local/bin/aws ec2 describe-instances --profile personal --region us-east-1 \
 --instance-ids "$jc2_contact_instance" \
 --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Private:PrivateIpAddress,Public:PublicIpAddress,Devices:BlockDeviceMappings}' --output json
# If the backup timer fails, ROOT owns immediate exact-ID retirement with the
# root disk already retained. A launcher failure is never permission to retry.
