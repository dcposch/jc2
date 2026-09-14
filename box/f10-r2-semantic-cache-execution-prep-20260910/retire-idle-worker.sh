#!/bin/bash
# ROOT closeout: setup admission missed; no registered science was launched.
set -euo pipefail
test "$(date -u +%s)" -ge "$(date -ud '2026-09-10 16:00:00 UTC' +%s)"
test ! -e box/f10-r2-semantic-cache-execution-prep-20260910/ROOT-REGISTRATION.json
test ! -e box/f10-r2-semantic-cache-execution-prep-20260910/setup.sh
sha256sum -c <<'JC2_LOCAL_METADATA'
30d736ed13f016be5756784d01a601663dce8e82278fbb7118674ab831af256a  box/f10-r2-semantic-cache-execution-prep-20260910/native-metadata.sh
a5c86c0512f2104182e0bf601bce086271c2d34cf4f361a4807d0c06f94aeabd  box/f10-r2-semantic-cache-execution-prep-20260910/native.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  box/f10-r2-semantic-cache-execution-prep-20260910/native.stderr
acbf656e441249cacab8b0a002c39b048f4755004e35e70b112f2e704086c722  box/f10-r2-semantic-cache-execution-prep-20260910/native-manifest.json
e1a625094c5213fe29c247aadd2f27232c18889289957e0311fba7ca62b5be7a  box/f10-r2-semantic-cache-execution-prep-20260910/native.sha256
JC2_LOCAL_METADATA
ssh -i /home/ubuntu/.ssh/jc2-fleet -o BatchMode=yes -o ConnectTimeout=10 -o StrictHostKeyChecking=accept-new ubuntu@52.91.33.248 'sudo /bin/bash -se' <<'JC2_REMOTE'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0df0e858f98e614ad
test "$(tr -d '\n' < /proc/sys/kernel/random/boot_id)" = 0153cfb3-ade6-4215-a90a-91de35d7f448
test ! -e /opt/jc2-r2-controls-cache-20260910T1545
test ! -e /run/jc2-r2-controls-cache-20260910T1545
test ! -e /var/lib/jc2-r2-controls-cache-20260910T1545
test "$(systemctl show jc2-f10-r2-controls-cache-20260910T1545.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-controls-cache-20260910T1545.service -p ControlPID --value)" = 0
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-controls-cache-20260910T1545.service
test "$(find /home/ubuntu/jc2-r2-controls-cache-20260910T1545/stage -mindepth 1 -maxdepth 1 -printf '%f\n')" = native-metadata.sh
printf '%s\n' '30d736ed13f016be5756784d01a601663dce8e82278fbb7118674ab831af256a  /home/ubuntu/jc2-r2-controls-cache-20260910T1545/stage/native-metadata.sh' | sha256sum -c
sync -f /home/ubuntu/jc2-r2-controls-cache-20260910T1545/stage/native-metadata.sh
date -u '+NO_SCIENCE_DEPLOYMENT_VERIFIED %FT%T.%NZ'
JC2_REMOTE
sync -f box/f10-r2-semantic-cache-execution-prep-20260910/native.stdout
sync -f box/f10-r2-semantic-cache-execution-prep-20260910/native-manifest.json
/usr/local/bin/aws ec2 describe-instances --region us-east-1 --instance-ids i-0df0e858f98e614ad --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Devices:BlockDeviceMappings}' --output json > box/f10-r2-semantic-cache-execution-prep-20260910/retirement-precheck.json
jq -e 'length==1 and .[0].ID=="i-0df0e858f98e614ad" and .[0].State=="running" and (.[0].Devices|length)==1 and .[0].Devices[0].Ebs.VolumeId=="vol-0d2e61d8edb77ffdd" and .[0].Devices[0].Ebs.DeleteOnTermination==false' box/f10-r2-semantic-cache-execution-prep-20260910/retirement-precheck.json
/usr/local/bin/aws ec2 describe-instance-attribute --region us-east-1 --instance-id i-0df0e858f98e614ad --attribute disableApiTermination --output json > box/f10-r2-semantic-cache-execution-prep-20260910/retirement-protection.json
jq -e '.InstanceId=="i-0df0e858f98e614ad" and .DisableApiTermination.Value==false' box/f10-r2-semantic-cache-execution-prep-20260910/retirement-protection.json
date -u '+RETIRE_IDLE_WORKER_REQUEST %FT%T.%NZ'
/usr/local/bin/aws ec2 terminate-instances --region us-east-1 --instance-ids i-0df0e858f98e614ad --output json > box/f10-r2-semantic-cache-execution-prep-20260910/retirement-response.json
sed -n '1,120p' box/f10-r2-semantic-cache-execution-prep-20260910/retirement-response.json

