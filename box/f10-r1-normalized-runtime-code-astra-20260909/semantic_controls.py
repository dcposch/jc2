"""UNEXECUTED finite normalized in-process negatives, not a production checker.
The genuine checker.main must already have succeeded under this exact caller.
No change to checker APIs, no solver, no normalized-source re-generation.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from execution_gate import authorize

def main():
    if len(sys.argv)!=6:
        raise SystemExit('usage: semantic_controls.py AUTH ORIGINAL NORMALIZED FULL_RECEIPT CONTROLS_RECEIPT')
    custody=authorize(sys.argv[1],__file__,'check')
    # All mathematical imports and mutations remain below exact authority.
    import copy,hashlib,json
    import checker
    from algebra import Ring,Q,require
    ring=Ring()
    def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    spec=json.loads(Path(sys.argv[1]).read_text())
    paths=[Path(x).resolve(strict=True) for x in sys.argv[2:5]]
    original_path,normalized_path,full_path=paths
    for path in paths:
        require(spec['file_sha256'].get(str(path))==sha(path),'each control input must be freshly registered')
    original=json.loads(original_path.read_text())
    normalized=json.loads(normalized_path.read_text())
    full=json.loads(full_path.read_text())
    codepaths={name:Path(__file__).with_name(name).resolve(strict=True)
               for name in ('generator.py','checker.py','algebra.py')}
    expected={'generator.py':'d444d022593c99a8d5a22d9cd9cbcac2bea9c88ef1a305d3c1c8ddf1635a6d8e',
              'checker.py':'091bbf35693c52833f2de936eeecd2e734f8404f26e9c68039bb8ab6aaecb551',
              'algebra.py':'7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc'}
    require(sha(original_path)==checker.SOURCE,'frozen original source')
    for name,path in codepaths.items():
        require(sha(path)==expected[name]==spec['file_sha256'].get(str(path)),'exact registered normalized code/backend')
    require(normalized['implementation_sha256']==expected['generator.py'],'genuine normalized producer binding')
    require(full['status']=='PASS-NORMALIZED-REPRESENTATION-NOT-IDEAL-DECISION'
            and full['source_sha256']==sha(original_path)
            and full['artifact_sha256']==sha(normalized_path),'genuine prior production receipt binding')
    require(full['original_slots']==20 and full['G_slots']==9 and full['H_slots']==2
            and full['full_inverse_poles']==10 and full['full_bracket_bands']==8,'genuine full-condition inventory')
    # The receipt is supplied only by the preceding genuine production call.
    # This in-process harness is not an independent lifecycle attestation.
    cases=[]
    def reject(name,mutate,exception_type,reason):
        changed=copy.deepcopy(normalized)
        evidence=mutate(changed)
        require(changed!=normalized,'negative fixture must actually change the object')
        fixture=Path(sys.argv[5]).parent/('fixture-'+name+'.json')
        with fixture.open('x') as stream:
            json.dump(changed,stream,sort_keys=True,separators=(',',':'),allow_nan=False); stream.write('\n')
        fixture_sha=sha(fixture)
        reread=json.loads(fixture.read_text())
        require(reread==changed,'harness JSON changed fixture values')
        try: checker.verify(original,reread)
        except Exception as exc:
            require(type(exc) is exception_type and str(exc)==reason,
                    name+': unexpected rejection: '+type(exc).__name__+': '+str(exc))
        else: raise RuntimeError(name+': changed object accepted')
        require(sha(fixture)==fixture_sha,'fixture drift during in-process control')
        cases.append({'name':name,'fixture_sha256':fixture_sha,'fixture_bytes':fixture.stat().st_size,
                      'exception':exception_type.__name__,'reason':reason,'mutation_evidence':evidence,
                      'entrypoint':'checker.verify IN-PROCESS, not checker.main','status':'EXPECTED-REJECTION'})

    def matrix_entry(data):
        old=ring.read(data['N1'][0][0])
        data['N1'][0][0]=ring.wire(ring.add(old,ring.c(1)))
    reject('completed-matrix-entry',matrix_entry,ValueError,'source-bound completed matrix')

    def historic_wrong_index(data):
        # A's S-constant linear coefficient is gap=z-U*d0. Here d0 is
        # maps[2][2], NOT the leading mate coefficient D[0]. All D_i below
        # are theta-indexed leading-mate coefficients from the frozen object.
        F,H,a,b=[ring.read(w) for w in data['leading']]
        D=[ring.read(w) for w in data['D']]
        low=[ring.read(w) for w in data['maps']['2']]
        gap=ring.sub(ring.atom(2),ring.mul(low[0],low[2]))
        deltaN=[ring.mul(gap,ring.sub(ring.scale(D[i+1],6-i),ring.scale(D[i],7-i))) for i in range(5)]
        deltaV2=ring.scale(deltaN[4],Q(-1,4))
        deltaV1=ring.scale(deltaN[3],Q(-1,8))
        deltaV0=ring.scale(ring.add(ring.scale(ring.mul(F,deltaV1),-4),ring.scale(ring.mul(H,deltaV2),4),ring.scale(deltaN[2],-1)),Q(1,12))
        deltaC1=ring.add(ring.scale(ring.mul(a,deltaV2),8),ring.scale(ring.mul(F,deltaV0),-8),ring.scale(deltaN[1],-1))
        deltaC0=ring.add(ring.scale(ring.mul(a,deltaV1),4),ring.scale(ring.mul(H,deltaV0),-4),ring.scale(deltaN[0],-1))
        require(deltaC1 or deltaC0,'historic wrong-index fixture must change at least one c3 coefficient')
        column=copy.deepcopy(data['h3'])
        data['c3']=[ring.wire(ring.add(ring.read(w),d)) for w,d in zip(data['c3'],(deltaC1,deltaC0))]
        require(data['h3']==column,'historic control must retain homogeneous column')
        return {'literal_old_rule':'N_i=-W_i+(6-i)*gap*D_(i+1)',
                'correct_rule':'N_i=-W_i+(7-i)*gap*D_i','i_range':[0,1,2,3,4],
                'gap':'z-U*d0; d0=maps[2][2], not leading D[0]',
                'delta_N':[ring.wire(p) for p in deltaN],
                'delta_V':[ring.wire(p) for p in (deltaV0,deltaV1,deltaV2)],
                'delta_c3':[ring.wire(p) for p in (deltaC1,deltaC0)],'h3_retained':True}
    reject('historic-third-forcing-index',historic_wrong_index,ValueError,'full affine forcing including third correction')

    def pi_sign(data):
        old=ring.read(data['Pi']); require(old,'Pi sign fixture nonzero')
        data['Pi']=ring.wire(ring.scale(old,-1))
    reject('full-Pi-sign',pi_sign,ValueError,'full Pi')
    def add_constant(key):
        def mutate(data): data[key]=ring.wire(ring.add(ring.read(data[key]),ring.c(1)))
        return mutate
    reject('H0-projection',add_constant('H0'),ValueError,'H0 whole constant target')
    reject('H1-projection',add_constant('H1'),ValueError,'H1 whole linear target')
    reject('float-anywhere',lambda data:data.__setitem__('control_float',0.5),ValueError,'float forbidden')
    def noncanonical(data):
        wire=data['units']['L']; require(wire,'noncanonical fixture needs a nonzero coefficient')
        wire[0][1]='+'+wire[0][1]
    reject('noncanonical-rational-string',noncanonical,ValueError,'canonical rational')
    big=9007199254740993
    require(big>2**53 and int(float(big))!=big,'genuine beyond-binary64 integer precondition')
    def wrong_large(data):
        wire=[[[0]*7,str(big),'1']]
        require(data['H0']!=wire,'large canonical integer fixture must change H0')
        data['H0']=wire
    reject('canonical-wrong-large-integer',wrong_large,ValueError,'H0 whole constant target')
    require(len(cases)==8,'finite eight-control inventory')
    for path in paths: require(sha(path)==spec['file_sha256'][str(path)],'registered control input drift')
    report={'status':'FINITE-NORMALIZED-CONTROLS-PASS-NOT-IDEAL-DECISION','execution':custody,
            'source_sha256':sha(original_path),'normalized_sha256':sha(normalized_path),
            'genuine_production_receipt_sha256':sha(full_path),'code_sha256':expected,
            'harness_sha256':sha(__file__),'cases':cases,
            'precision':{'canonical_wrong_integer':str(big),'scope':'one exact semantic rejection, one noncanonical parser rejection and one float rejection; no successful large nested-parser payload claim'},
            'positive_scope':'separate registered checker.main; no repeated positive in-process run',
            'negative_limit':'matrix and third forcing hit original bindings; no altered-pair late bracket/pole coverage'}
    with Path(sys.argv[5]).open('x') as stream:
        json.dump(report,stream,sort_keys=True,separators=(',',':'),allow_nan=False); stream.write('\n')
    print(report['status'])

if __name__=='__main__': main()
