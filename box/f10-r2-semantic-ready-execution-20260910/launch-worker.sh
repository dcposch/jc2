#!/bin/bash
set -euo pipefail
sha256sum -c <<'JC2_READY_PINS'
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  box/f10-r2-reconstruction-code-astra-20260910/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  box/f10-r2-reconstruction-code-astra-20260910/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  box/f10-r2-reconstruction-code-astra-20260910/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  box/f10-r2-reconstruction-code-astra-20260910/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  box/f10-r2-reconstruction-code-astra-20260910/check.py
6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b  box/f10-r2-semantic-runtime-astra-20260910/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  box/f10-r2-semantic-runtime-astra-20260910/probe.py
a896a8094be9b38f7ffa3a82cab15d340add0d7ab5f513340b2b7f916e489540  box/f10-r2-semantic-mutator-astra-20260910/mutate_controls.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  ops/run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  box/f10-r2-actual-execution-prep-20260910/harvest/run/jc2-r2-20260910T1230/frozen/artifact.json
469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b  xmodel/f10-r2-semantic-code-gate-fable5-20260910.md
3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b  xmodel/f10-r2-reconstruction-code-gate-fable5-20260910.md
3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c  xmodel/f10-r2-actual-result-gate-fable5-20260910.md
edd4c71e86d0d5cac2ee277de69199522a2a5bca9381833f19dc078e9759ea19  box/f10-r2-semantic-runtime-astra-20260910/CONTRACT.md
4d4e63b6cc8ac84479a7b9e24e5fe4752ea3de52a0c8750483b139b5d3862bfd  box/f10-r2-semantic-ready-deployment-prep-20260910/DISABLED-REGISTRATION.template.json
516332e722baeb271ef2d7401265b6cb9b87876af96773e657503c02407729f6  box/f10-r2-semantic-ready-deployment-prep-20260910/setup.template.sh
e6d3c105e8e0c558356c7db891d9a8a6c5d09a758eef2dd3627ba30eb5923848  box/f10-r2-semantic-ready-deployment-prep-20260910/native-metadata.template.sh
0c5820cd60a44704a6d8118a7570a9327c1f2fe62939ff664b1f9b7cfaf42730  box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml
JC2_READY_PINS
test ! -e box/f10-r2-semantic-ready-execution-20260910/launch-response.json
test "$(sha256sum xmodel/f10-r2-native-cache-correction-gate-fable5-20260910.md | cut -d ' ' -f 1)" = b7a6aa2590f4695a646f776c1493f80f9f4dcb24b9e8c00d78aa4548d694140a
test "$(sha256sum box/f10-r2-semantic-runtime-astra-20260910/dispatch.py | cut -d ' ' -f 1)" = 6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 16:22:00 UTC' +%s)"
/usr/local/bin/aws ec2 run-instances --region us-east-1 --image-id ami-066263bf15bd856de --instance-type c7i.xlarge --count 1 --key-name jc2-fleet --security-group-ids sg-09ffa8932558f0a79 --subnet-id subnet-948915c9 --associate-public-ip-address --user-data file://box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml --enable-api-termination --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"DeleteOnTermination":false}}]' --client-token jc2-r2-controls-ready-20260910T1620 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=jc2-r2-controls-ready-20260910T1620},{Key=jc2fleet,Value=1},{Key=market,Value=ondemand},{Key=Owner,Value=root-r2-controls-ready-20260910T1620}]' --query 'Instances[].{ID:InstanceId,State:State.Name,PrivateIP:PrivateIpAddress,Type:InstanceType,Launched:LaunchTime,Devices:BlockDeviceMappings}' --output json > box/f10-r2-semantic-ready-execution-20260910/launch-response.json
test "$(jq 'length' box/f10-r2-semantic-ready-execution-20260910/launch-response.json)" = 1
jc2_controlscache_instance=$(jq -r '.[0].ID' box/f10-r2-semantic-ready-execution-20260910/launch-response.json)
[[ "$jc2_controlscache_instance" =~ ^i-[0-9a-f]+$ ]]
systemd-run --user --unit=jc2-r2-controlsready-workerterm-20260910T1620 --on-calendar='2026-09-10 16:53:00 UTC' --timer-property=AccuracySec=1s /usr/local/bin/aws ec2 terminate-instances --region us-east-1 --instance-ids "$jc2_controlscache_instance"
systemctl --user is-active jc2-r2-controlsready-workerterm-20260910T1620.timer
date -u '+ORIGINAL_WORKER_TERMINATION_ARMED %Y-%m-%d %H:%M:%S.%N UTC'
sed -n '1,150p' box/f10-r2-semantic-ready-execution-20260910/launch-response.json
/usr/local/bin/aws ec2 describe-instance-attribute --region us-east-1 --instance-id "$jc2_controlscache_instance" --attribute disableApiTermination --output json
/usr/local/bin/aws ec2 describe-instances --region us-east-1 --instance-ids "$jc2_controlscache_instance" --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Private:PrivateIpAddress,Public:PublicIpAddress,Devices:BlockDeviceMappings}' --output json
