"""UNEXECUTED seven univariate in-process negatives, not production entrypoints.
One genuine checker.main must already have succeeded under this exact caller.
No positive mathematical rerun and no normalized-source regeneration.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from execution_gate import authorize

def main():
    if len(sys.argv)!=7:
        raise SystemExit('usage: semantic_controls.py AUTH NORMALIZED PRIOR_NORMALIZED_RECEIPT UNIVARIATE NEW_FULL_RECEIPT CONTROLS_RECEIPT')
    custody=authorize(sys.argv[1],__file__,'check')
    import copy,hashlib,json
    from input_evidence import verified_input
    normalized,evidence=verified_input(sys.argv[1],sys.argv[2],sys.argv[3])
    import checker
    from algebra import Ring,require
    def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    spec=json.loads(Path(sys.argv[1]).read_text())
    paths=[Path(x).resolve(strict=True) for x in sys.argv[2:6]]
    normalized_path,prior_path,univariate_path,full_path=paths
    for path in paths:
        require(spec['file_sha256'].get(str(path))==sha(path),'each control input must be freshly registered')
    data=json.loads(univariate_path.read_text()); full=json.loads(full_path.read_text())
    expected={'adapter.py':'11ebf4307e7cff9b7909020dcdf69cda32f689236453763ce9433fff66fd7b67',
              'checker.py':'6547063b8cf2970ce0aa1e47e5a49db31c2fd4b1e97d87690c954487500a61f0',
              'algebra.py':'7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc',
              'input_evidence.py':'d262f3d498323b4606c51828a647b7334e8885095b099acbff41d17dd6db88b9'}
    for name,want in expected.items():
        path=Path(__file__).with_name(name).resolve(strict=True)
        require(sha(path)==want==spec['file_sha256'].get(str(path)),'exact registered univariate code/backend/evidence')
    require(data['implementation_sha256']==expected['adapter.py'] and data['input_evidence']==evidence,
            'genuine univariate producer/input binding')
    require(full['status']=='PASS-NINE-ROW-ADAPTER-NOT-IDEAL-DECISION'
            and full['univariate_sha256']==sha(univariate_path) and full['input_evidence']==evidence,
            'genuine prior production receipt binding')
    require(full['row_slots']==9 and full['guard_factors']==['r','h0'],'genuine full univariate inventory')
    # Receipt typing is not lifecycle attestation: the preceding genuine
    # production child and ROOT-owned normalized acceptance remain required.
    ring=Ring(); cases=[]
    def reject(name,mutate,exception_type,reason):
        changed=copy.deepcopy(data)
        mutation_evidence=mutate(changed)
        require(changed!=data,'negative fixture must actually change the object')
        fixture=Path(sys.argv[6]).parent/('fixture-'+name+'.json')
        with fixture.open('x') as stream:
            json.dump(changed,stream,sort_keys=True,separators=(',',':'),allow_nan=False); stream.write('\n')
        fixture_sha=sha(fixture)
        reread=json.loads(fixture.read_text())
        require(reread==changed,'harness JSON changed fixture values')
        try: checker.verify(normalized,reread)
        except Exception as exc:
            require(type(exc) is exception_type and str(exc)==reason,
                    name+': unexpected rejection: '+type(exc).__name__+': '+str(exc))
        else: raise RuntimeError(name+': changed object accepted')
        require(sha(fixture)==fixture_sha,'fixture drift during in-process control')
        cases.append({'name':name,'fixture_sha256':fixture_sha,'fixture_bytes':fixture.stat().st_size,
                      'exception':exception_type.__name__,'reason':reason,'mutation_evidence':mutation_evidence,
                      'entrypoint':'checker.verify IN-PROCESS, not checker.main','status':'EXPECTED-REJECTION'})

    def plus_one(wire): return ring.wire(ring.add(ring.read(wire),ring.c(1)))
    def phi_coefficient(obj):
        obj['coefficients']['a']=plus_one(obj['coefficients']['a'])
        return {'location':'coefficients.a','change':'add exact B constant 1'}
    reject('Phi3-coefficient',phi_coefficient,ValueError,'all Phi3 coefficients')
    def inverse(obj):
        obj['c_inverse']=plus_one(obj['c_inverse'])
        return {'location':'c_inverse','change':'add exact B constant 1'}
    reject('c-inverse',inverse,ValueError,'actual c inverse identity')
    def affine_r(obj):
        obj['r'][0]=plus_one(obj['r'][0])
        return {'location':'r[0]','change':'add exact B constant 1; no b division'}
    reject('affine-r-constant',affine_r,ValueError,'affine r constant')
    def indexed_row(obj):
        obj['rows'][0]['coefficients'][0]=plus_one(obj['rows'][0]['coefficients'][0])
        return {'location':'rows[E1/S1].coefficients[0]','change':'add exact B constant 1'}
    reject('indexed-row-coefficient',indexed_row,ValueError,'literal univariate row E1/S1')
    def guard_factor(obj):
        require(obj['guard']['factors']==['r','h0'],'guard-factor fixture precondition')
        obj['guard']['factors'].pop()
        return {'removed_factor':'h0','q_coefficients_unchanged':True}
    reject('missing-guard-factor',guard_factor,ValueError,'guard equation and both factors retained')
    def guard_coefficient(obj):
        obj['guard']['q'][0]=plus_one(obj['guard']['q'][0])
        return {'location':'guard.q[0]','change':'add exact B constant 1'}
    reject('guard-q-coefficient',guard_coefficient,ValueError,'entire guard q=r*h0')
    def omit_dense(obj):
        slots=obj['rows'][0]['coefficients']
        require(len(slots)==4,'dense-slot fixture precondition')
        removed=slots.pop()
        return {'row':'E1/S1','removed_slot_index':3,'removed_wire':removed,
                'scope':'omitted dense slot; no assumption that it is zero'}
    reject('omitted-dense-slot',omit_dense,ValueError,'every univariate coefficient slot including zeros')
    require(len(cases)==7,'finite seven-control inventory')
    for path in paths: require(sha(path)==spec['file_sha256'][str(path)],'registered control input drift')
    report={'status':'FINITE-UNIVARIATE-CONTROLS-PASS-NOT-IDEAL-DECISION','execution':custody,
            'input_evidence':evidence,'univariate_sha256':sha(univariate_path),
            'genuine_production_receipt_sha256':sha(full_path),'code_sha256':expected,
            'harness_sha256':sha(__file__),'cases':cases,
            'positive_scope':'separate registered checker.main; no repeated positive in-process run',
            'negative_limit':'seven univariate semantic rejections, not new original-source bracket/pole negative coverage'}
    with Path(sys.argv[6]).open('x') as stream:
        json.dump(report,stream,sort_keys=True,separators=(',',':'),allow_nan=False); stream.write('\n')
    print(report['status'])

if __name__=='__main__': main()
