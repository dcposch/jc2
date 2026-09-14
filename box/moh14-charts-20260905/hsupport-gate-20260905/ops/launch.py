import json,subprocess
from pathlib import Path
base=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905')
jobs=[('C_n16m12_M6_13_ell3_s3_V1_1','172.30.0.166',8,60000000),('C_n16m12_M6_13_ell3_s3_V1_3','172.30.0.254',8,60000000),('C_n16m12_M6_13_ell3_s3_V4_3','172.30.0.7',8,24000000),('C_n18m12_M2_9_ell2_s3_V1_8','172.30.0.18',12,45000000),('C_n24m16_M12_17_ell1_s3_V2_1','172.30.0.7',8,24000000),('C_n24m16_M12_17_ell1_s3_V1_2','172.30.0.254',8,60000000),('C_n24m16_M12_17_ell1_s3_V3_2','172.30.0.28',12,45000000),('C_n24m18_M9_20_ell1_s3_V1_9','172.30.0.166',8,60000000)]
launched=[]
for stem,host,threads,vm in jobs:
 cmd=['python3',str(base/'ops/fleet_driver.py'),'--stem',stem,'--host',host,'--threads',str(threads),'--vm-kib',str(vm)]
 log=base/'ops'/(stem+'_native.driver.log')
 with log.open('w') as fh:p=subprocess.Popen(cmd,stdout=fh,stderr=subprocess.STDOUT,start_new_session=True)
 launched.append(dict(stem=stem,host=host,threads=threads,vm_kib=vm,pid=p.pid,mode='native',log=str(log)))
(base/'ops/launched-native.json').write_text(json.dumps(launched,indent=2)+'\n')
print(json.dumps(launched,indent=2))
