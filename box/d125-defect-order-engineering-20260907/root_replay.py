"""Tiny local replay of copied terminal actual-engine evidence; no CAS/SSH."""
import hashlib, json, pathlib, resource, signal, sys
root=pathlib.Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(25,25));signal.alarm(30)
evidence=root/'evidence';sys.path.insert(0,str(evidence))
import exact as E
import driver as D
import defect_order as O
custody=json.loads((root/'remote-custody.json').read_bytes())
for name, item in custody['files'].items():
    data=(evidence/name).read_bytes()
    E.need(len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'],'copy hash '+name)
eng=evidence/'engineering'
E.need((eng/'levels.stderr').read_bytes()==b'','levels stderr')
E.need((eng/'levels.stdout').read_text()=='LEVELS_BEGIN\n1\nx\nx\nx\ny^2\nz\nLEVELS_END\n','levels mismatch')
names=['x','y','z'];order=O.descriptor(names,[[3,1,4],[1,0,1],[1,0,1]])
prefix=O.ring_declaration(order)+'ideal I=x-y^2,z-y^3;\n';source=E.digest(prefix.encode())
raw=(eng/'graph.stdout').read_bytes();err=(eng/'graph.stderr').read_bytes()
engine,basis,cofactors=E.parse_result(raw,err,names,source,order)
rows=[E.polynomial(p,names) for p in ('x-y^2','z-y^3')]
E.engine_map(rows,engine);E.need(cofactors is None,'graph not nonunit')
verdict=E.proper_certificate(rows,basis,3,order['weight_rows'])
try:E.parse_result(raw.replace(O.digest(order).encode(),E.ring_id(names).encode(),1),err,names,source,order)
except ValueError:pass
else:raise ValueError('changed graph header accepted')
control=D.check_control((evidence/'control.stdout').read_bytes(),(evidence/'control.stderr').read_bytes())
for job in json.loads((eng/'batch.result.json').read_bytes())['jobs']:
    t=job['telemetry'];E.need(job['group_absent'] and t['error'] is None,'terminal custody')
    if job['label']=='rss':
        E.need(t['status']=='RESOURCE_CAP' and all(t['termination'][k] for k in
               ('term_sent','kill_sent','leader_reaped','cleanup_complete')),'RSS cleanup')
    else:E.need(t['status']=='NORMAL_EXIT' and t['child_returncode']==0,'normal terminal')
print(json.dumps({'status':'LOCAL_ACTUAL_EVIDENCE_REPLAY_PASS','optimized':not __debug__,
                 'files_verified':len(custody['files']),'graph':verdict,'control':control},sort_keys=True))
