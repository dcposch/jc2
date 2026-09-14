"""Bounded post-terminal hashes/framing only, no polynomial parsing/arithmetic."""
import hashlib,json,pathlib,resource,signal
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(25,25));signal.alarm(30)
root=pathlib.Path(__file__).resolve().parent
c=json.loads((root/'terminal-custody.json').read_bytes())
for name,info in c['files'].items():
    path=root/name if name=='solver.authority.json' else root/'evidence'/name
    data=path.read_bytes()
    if len(data)!=info['bytes'] or hashlib.sha256(data).hexdigest()!=info['sha256']:raise RuntimeError('copy pin drift '+name)
lines=(root/'evidence/decision.stdout').read_text().splitlines()
indices=[int(line.split(' ',2)[1]) for line in lines if line.startswith('I ') and line.split(' ',2)[1].isdigit()]
result={'status':'TERMINAL_HASH_AND_FRAMING_ONLY','files_verified':len(c['files']),
        'original_index_sequence_803':indices==list(range(1,804)),
        'I_SIZE':[s for s in lines if s.startswith('I_SIZE ')],
        'I_BEGIN':[s for s in lines if s.startswith('I_BEGIN ')],
        'I_END_count':lines.count('I_END'),'G_BEGIN_count':sum(s.startswith('G_BEGIN ') for s in lines),
        'G_END_count':lines.count('G_END'),'T_BEGIN_count':sum(s.startswith('T_BEGIN ') for s in lines),
        'terminal_markers':[s for s in lines if s.startswith('END ')],
        'after_I_END':lines[lines.index('I_END')+1:] if 'I_END' in lines else None,
        'stderr_bytes':(root/'evidence/decision.stderr').stat().st_size,
        'no_certificate_verification':True}
print(json.dumps(result,sort_keys=True))
