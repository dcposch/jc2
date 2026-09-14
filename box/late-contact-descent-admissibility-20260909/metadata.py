import hashlib, json, pathlib, datetime

ROOT = pathlib.Path('/home/ubuntu/jc2')
OUT = ROOT / 'box/late-contact-descent-admissibility-20260909'
def pin(path):
    p = ROOT / path
    b = p.read_bytes()
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

cpath = 'box/source-multiplicity-admissibility-20260909/custody.json'
c = json.loads((ROOT / cpath).read_text())
items = []
mutable = {'COORDINATION.md', 'APPROACHES.md', 'ladder/REDUCTION.md', 'AUDIT.md'}
for section in ('files', 'inputs'):
    for old in c[section]:
        new = pin(old['path'])
        new.update(expected_sha256=old['sha256'], matches=old['sha256'] == new['sha256'], section=section,
                   historical_mutable=old['path'] in mutable)
        items.append(new)
        if not new['matches'] and old['path'] not in mutable:
            raise SystemExit('IMMUTABLE DRIFT: ' + old['path'])
result = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'custody': pin(cpath),
          'checks': items, 'immutable_pass': True,
          'historical_canonical_mismatches': [i['path'] for i in items if not i['matches']],
          'read_scope': 'Metadata hashes only; no report body read by this program.'}
with (OUT / 'source-receipt-check.json').open('x') as f:
    json.dump(result, f, indent=2)
print(json.dumps({'immutable_pass': True, 'checks': len(items), 'historical_canonical_mismatches': result['historical_canonical_mismatches'], 'receipt': pin(str((OUT / 'source-receipt-check.json').relative_to(ROOT)))}))
