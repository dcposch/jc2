from pathlib import Path
import subprocess,shlex,json
n=Path(__file__).resolve().parent
worker=Path('/home/ubuntu');native=worker/'g9966-corrected-jacobian-flint';base=worker/'g9966-corrected-jacobian';batch=worker/'g9966-corrected-jacobian-batch';q=worker/'g9966-corrected-jacobian-quotient';out=native/'minor-independent-controls';code=native/'minor-verification-code-v4'
records=[]
for b in ['delta2','delta52']:
 args=['python3','-u',str(code/'minor_merged_verify.py'),'--merged',str(out/f'authoritative-v4-{b}-input.json'),'--source-result',str(base/f'results-source-full/source-full-{b}.json'),'--weak-result',str(base/f'results-gauge/gauge-{b}.json'),'--code-dir',str(base/'run-code-source-full'),'--weak-code-dir',str(base/'run-code-gauge'),'--driver',str(q/'deep_resume_jacobian_quotient.py'),'--backend',str(q/'deep_flint_jacobian_pair.py'),'--quotient-seed',str(q/'deep_quotient_seed.py'),'--ancestor-driver',str(native/'deep_resume_jacobian_flint.py'),'--ancestor-driver',str(batch/'deep_resume_jacobian_batch.py'),'--ancestor-backend',str(native/'deep_flint_jacobian.py'),'--ancestor-backend',str(batch/'deep_flint_jacobian_batch.py'),'--safe-exporter',str(q/'deep_safe_singular.py'),'--verified-prefix',str(out/f'authoritative-{b}-verify.json'),'--verified-prefix-input',str(out/f'authoritative-{b}-input.json'),'--trusted-verifier-code',str(native/'minor-verification-code-v2'),'--jacobian-method','flint-direct','--out',str(out/f'authoritative-v4-{b}-verify.json')]
 for p in [base,native,batch,q]:args+=['--certificate-root',str(p)]
 cmd='setsid '+shlex.join(args)+' > '+shlex.quote(str(out/f'authoritative-v4-{b}-verify.log'))+' 2>&1 < /dev/null & echo $!'
 run=subprocess.run(['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','ubuntu@172.30.0.85',cmd],text=True,capture_output=True,check=True)
 records.append({'branch':b,'argv':args,'pid':run.stdout.strip()})
(n/'minor_v4_launch.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps(records,indent=2))
