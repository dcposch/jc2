import pathlib,json,subprocess,hashlib
root=pathlib.Path('/home/ubuntu/jc2/box/graded-moh-20260905');stem77='C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6';stem111='C_n18m12_M2_9_ell2_s3_V3_8'
jobs=[(stem77,root/'proof/torus_branches'/stem77/g/'branch.sing',g,'172.30.0.67','i-05bbedf0197e8eee3',24) for g in ('A3_2_0','B2_1_0','B2_1_1')]
jobs.append((stem111,root/'instrument'/stem111/'slice.sing','full','172.30.0.86','i-02aaa996f54d2c004',40))
for stem,old,gauge,ip,instance,mem in jobs:
 work=root/'runs'/(stem+'_r2_slimgb_'+gauge);work.mkdir(exist_ok=True)
 txt=old.read_text();assert txt.count('std(I)')==1;txt=txt.replace('std(I)','slimgb(I)')
 inp=work/'input.sing';inp.write_text(txt)
 cmd=['/usr/bin/Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(inp)]
 spec=dict(input=str(inp),work=str(work),command=cmd,memory_gib=mem,timeout_seconds=1800,kind='singular_slimgb',chart=stem,field=0,order='dp',representation='full_direct_c1_second_torus_gauge' if gauge!='full' else 'full_direct_c_equals_one',gauge=gauge,worker=instance,ip=ip,source_script=str(old),source_script_sha256=hashlib.sha256(old.read_bytes()).hexdigest(),only_change='std(I) -> slimgb(I)')
 sp=work/'spec.json';sp.write_text(json.dumps(spec,indent=2)+'\n')
 subprocess.run(['python3',str(root/'ops/dispatch_lane.py'),'launch',ip,str(sp)],check=True)
