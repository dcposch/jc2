import pathlib,json,subprocess
root=pathlib.Path('/home/ubuntu/jc2/box/graded-moh-20260905')
for stem,ip,instance in [('C_n24m18_Mm15_14_ell1_s3_V1_9','172.30.0.86','i-02aaa996f54d2c004'),('C_n18m12_M2_9_ell2_s3_V1_8','172.30.0.67','i-05bbedf0197e8eee3')]:
 for kind,mem in [('msolve',180),('singular',48)]:
  work=root/'runs'/(stem+'_r2_'+kind+'_full');work.mkdir(exist_ok=True)
  inp=root/'instrument'/stem/('slice_p1073741827.ms' if kind=='msolve' else 'slice.sing')
  cmd=[str(root/'ops/bin/msolve'),'-g','2','-t','16','-v','2','-l','44','-m','2000','-f',str(inp),'-o',str(work/'basis.out')] if kind=='msolve' else ['/usr/bin/Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(inp)]
  s=dict(input=str(inp),work=str(work),command=cmd,memory_gib=mem,timeout_seconds=1800,kind=kind,chart=stem,field=1073741827 if kind=='msolve' else 0,order='dp',representation='full_direct_c_equals_one',worker=instance,ip=ip)
  spec=work/'spec.json';spec.write_text(json.dumps(s,indent=2)+'\n')
  subprocess.run(['python3',str(root/'ops/dispatch_lane.py'),'launch',ip,str(spec)],check=True)
