#!/bin/bash
set -euo pipefail
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/authority.py' | cut -d ' ' -f 1)" = '2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/arithmetic.py' | cut -d ' ' -f 1)" = 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/produce.py' | cut -d ' ' -f 1)" = 'eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check_arithmetic.py' | cut -d ' ' -f 1)" = 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'
test "$(sha256sum 'box/f10-r2-reconstruction-code-astra-20260910/check.py' | cut -d ' ' -f 1)" = 'e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0'
test "$(sha256sum 'box/f10-r2-fullunit-runtime-astra-20260910/dispatch.py' | cut -d ' ' -f 1)" = 'b6998cae2d38e962777dc1064f39a841cfee3e5bb0fc3905599a5378aa78ff69'
test "$(sha256sum 'box/f10-r2-highest-runtime-status-fix-astra-20260910/probe.py' | cut -d ' ' -f 1)" = '1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde'
test "$(sha256sum 'box/f10-r2-fullunit-runtime-astra-20260910/mutate.py' | cut -d ' ' -f 1)" = '4548656af387b7e08df5bd5c56504f97c2d11d2b5375cbfbadde5304465c4c97'
test "$(sha256sum 'ops/run_capped.py' | cut -d ' ' -f 1)" = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
test "$(sha256sum 'box/f10-r2-actual-execution-prep-20260910/harvest/run/jc2-r2-20260910T1230/frozen/artifact.json' | cut -d ' ' -f 1)" = 'dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587'
test "$(sha256sum 'box/f10-r2-fullunit-runtime-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'cb0da8dcfe19a033f9daad1de7de4e602a330f15a90c383824550522b8d847eb'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/entry.py' | cut -d ' ' -f 1)" = 'c49b7dfabe6dc8cc5b7aaea485171a6b709fc6158f180ae1157afd90b3cf4b1f'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/produce.py' | cut -d ' ' -f 1)" = '60a290aee2ed5def7ed4242743f187dea755659f287707fa79c6c1e05f2d1f10'
test "$(sha256sum 'box/f10-r2-fullunit-modular-code-astra-20260910/check.py' | cut -d ' ' -f 1)" = 'ccc3d2ddfca98f7faaed9df323fb90ec183b437b3c6b0bfcde0820186e667023'
test "$(sha256sum 'xmodel/f10-r2-fullunit-runtime-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = 'eca8d1e56b4d119c346e56be9730281169097c747468cc195df26c961213e317'
test "$(sha256sum 'box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml' | cut -d ' ' -f 1)" = '0c5820cd60a44704a6d8118a7570a9327c1f2fe62939ff664b1f9b7cfaf42730'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-runtime-astra-20260910/CONTRACT.md' | cut -d ' ' -f 1)" = 'cb0da8dcfe19a033f9daad1de7de4e602a330f15a90c383824550522b8d847eb'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-runtime-astra-20260910/dispatch.py' | cut -d ' ' -f 1)" = 'b6998cae2d38e962777dc1064f39a841cfee3e5bb0fc3905599a5378aa78ff69'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-highest-ready-deployment-prep-astra-20260910/DISABLED-REGISTRATION.template.json' | cut -d ' ' -f 1)" = 'a18e2f8d75433b90b6cc6a9ac76232789e41ffb5bd5a0135f4cc6b31f88addf9'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-highest-ready-deployment-prep-astra-20260910/INSTALL-INPUTS.template.json' | cut -d ' ' -f 1)" = '33352aad5d24f91189d782b0ba5fe98212ef86c86fc3013acfabd44060577da8'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-highest-ready-deployment-prep-astra-20260910/native-metadata.template.sh' | cut -d ' ' -f 1)" = 'e6d3c105e8e0c558356c7db891d9a8a6c5d09a758eef2dd3627ba30eb5923848'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-highest-ready-deployment-prep-astra-20260910/setup.template.sh' | cut -d ' ' -f 1)" = 'cc68b8ec6a57d870742acbd110414bdfa535baa95453314aa6aabf704a70651b'
test "$(sha256sum '/home/ubuntu/jc2/xmodel/f10-r2-fullunit-runtime-gate-fable5-20260910.md' | cut -d ' ' -f 1)" = 'eca8d1e56b4d119c346e56be9730281169097c747468cc195df26c961213e317'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/DISABLED-REGISTRATION.template.json' | cut -d ' ' -f 1)" = 'e83e219dc79087b9531f6df2f46dd0a23de48e900697dbb384195aaeb30fef7e'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/INSTALL-INPUTS.template.json' | cut -d ' ' -f 1)" = '7683bf1b68d38402beb8367e43780e05d4605e763f40ff5ab49b1e0e69553a7a'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/PINS.json' | cut -d ' ' -f 1)" = 'b189a68f994af0394565b0fd29c88a5175a2121451d1ca176cc6dee6c96b6bfa'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/READ-SCOPE.md' | cut -d ' ' -f 1)" = '07570c8e541ddbff4ade8ff650a1e972cf2253fa4237133c1d401dd14addc0e5'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/ROOT-FINALIZATION-CHECKLIST.md' | cut -d ' ' -f 1)" = 'c5950a159f875b58098ea4d99de54c75b73f25cc97c5a07151455b937aeed289'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/native-metadata.template.sh' | cut -d ' ' -f 1)" = 'e6d3c105e8e0c558356c7db891d9a8a6c5d09a758eef2dd3627ba30eb5923848'
test "$(sha256sum '/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/setup.template.sh' | cut -d ' ' -f 1)" = 'eb0035fe25e77921e3f7c43854b43961d138f7f71cace235c62091bcf89f0637'
test "$(sha256sum '/home/ubuntu/jc2/xmodel/f10-r2-fullunit-ready-deployment-prep-astra-20260910.md' | cut -d ' ' -f 1)" = 'c4957646f3498d084060af96b14237d812dde23178db3c679f51a4035956441b'
test "$(sha256sum '/home/ubuntu/jc2/xmodel/f10-r2-fullunit-ready-deployment-prep-astra-20260910.md.artifact.json' | cut -d ' ' -f 1)" = 'f868cce5970418cc176af37fc30ddf6d64f72846836680ed875ec9b03f551fcc'
test ! -e box/f10-r2-fullunit-ready-execution-20260910/launch-response.json
test "$(date -u +%s)" -lt "$(date -ud '2026-09-10 18:03:00 UTC' +%s)"
/usr/local/bin/aws ec2 run-instances --profile personal --region us-east-1 --image-id ami-066263bf15bd856de --instance-type c7i.xlarge --count 1 --key-name jc2-fleet --security-group-ids sg-09ffa8932558f0a79 --subnet-id subnet-948915c9 --associate-public-ip-address --user-data file://box/f10-r2-map-observer-execution-prep-20260910/stdlib-user-data.yaml --enable-api-termination --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"DeleteOnTermination":false}}]' --client-token jc2-r2-fullunit-ready-20260910T1800 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=jc2-r2-fullunit-ready-20260910T1800},{Key=jc2fleet,Value=1},{Key=market,Value=ondemand},{Key=Owner,Value=root-r2-fullunit-ready-20260910T1800}]' --query 'Instances[].{ID:InstanceId,State:State.Name,PrivateIP:PrivateIpAddress,Type:InstanceType,Launched:LaunchTime,Devices:BlockDeviceMappings}' --output json > box/f10-r2-fullunit-ready-execution-20260910/launch-response.json
test "$(jq 'length' box/f10-r2-fullunit-ready-execution-20260910/launch-response.json)" = 1
jc2_fullunit_instance=$(jq -r '.[0].ID' box/f10-r2-fullunit-ready-execution-20260910/launch-response.json)
[[ "$jc2_fullunit_instance" =~ ^i-[0-9a-f]+$ ]]
systemd-run --user --unit=jc2-r2-fullunitready-workerterm-20260910T1800 --on-calendar='2026-09-10 18:34:00 UTC' --timer-property=AccuracySec=1s /usr/local/bin/aws ec2 terminate-instances --profile personal --region us-east-1 --instance-ids "$jc2_fullunit_instance"
systemctl --user is-active jc2-r2-fullunitready-workerterm-20260910T1800.timer
date -u '+ORIGINAL_WORKER_TERMINATION_ARMED %Y-%m-%d %H:%M:%S.%N UTC'
sed -n '1,150p' box/f10-r2-fullunit-ready-execution-20260910/launch-response.json
/usr/local/bin/aws ec2 describe-instance-attribute --profile personal --region us-east-1 --instance-id "$jc2_fullunit_instance" --attribute disableApiTermination --output json
/usr/local/bin/aws ec2 describe-instances --profile personal --region us-east-1 --instance-ids "$jc2_fullunit_instance" --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Private:PrivateIpAddress,Public:PublicIpAddress,Devices:BlockDeviceMappings}' --output json

