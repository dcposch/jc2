"""UNEXECUTED metadata binding only, after unchanged authorize().
Root's registered acceptance is necessary; this module cannot create it.
"""
import hashlib
import json
from pathlib import Path

ORIGINAL='168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'
NORMAL_GENERATOR='d444d022593c99a8d5a22d9cd9cbcac2bea9c88ef1a305d3c1c8ddf1635a6d8e'
NORMAL_CHECKER='091bbf35693c52833f2de936eeecd2e734f8404f26e9c68039bb8ab6aaecb551'
ARITHMETIC='7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc'

def verified_input(authority,normalized,receipt):
    spec=json.loads(Path(authority).read_text())
    evidence=spec.get('normalized_acceptance')
    if not isinstance(evidence,dict) or evidence.get('status')!='ROOT-ACCEPTED-GENUINE-CHECKER-RECEIPT':
        raise RuntimeError('no independently registered normalized-input acceptance')
    if evidence.get('checker_sha256')!=NORMAL_CHECKER or evidence.get('generator_sha256')!=NORMAL_GENERATOR:
        raise RuntimeError('provisional backend code version differs')
    norm,rec=Path(normalized).resolve(strict=True),Path(receipt).resolve(strict=True)
    raw,rawreceipt=norm.read_bytes(),rec.read_bytes()
    nh,rh=hashlib.sha256(raw).hexdigest(),hashlib.sha256(rawreceipt).hexdigest()
    for path,digest in ((norm,nh),(rec,rh)):
        if spec['file_sha256'].get(str(path))!=digest: raise RuntimeError('input/receipt pin absent or changed')
    if evidence.get('normalized_sha256')!=nh or evidence.get('receipt_sha256')!=rh:
        raise RuntimeError('registered acceptance binds different artifacts')
    arith=Path(__file__).with_name('algebra.py').resolve(strict=True)
    if spec['file_sha256'].get(str(arith))!=ARITHMETIC: raise RuntimeError('exact arithmetic copy not registered')
    if str(Path(__file__).resolve()) not in spec['file_sha256']: raise RuntimeError('evidence-helper pin absent')
    data,result=json.loads(raw),json.loads(rawreceipt)
    if data.get('source_sha256')!=ORIGINAL or data.get('implementation_sha256')!=NORMAL_GENERATOR:
        raise RuntimeError('normalized original-source/implementation binding')
    if result.get('status')!='PASS-NORMALIZED-REPRESENTATION-NOT-IDEAL-DECISION' or result.get('artifact_sha256')!=nh or result.get('source_sha256')!=ORIGINAL:
        raise RuntimeError('genuine full-checker receipt does not bind input')
    expected={'original_slots':20,'G_slots':9,'H_slots':2,'full_inverse_poles':10,'full_bracket_bands':8}
    if any(result.get(k)!=v for k,v in expected.items()): raise RuntimeError('incomplete original-source checker scope')
    # A correctly spelled receipt is not proof of provenance. The root-owned
    # acceptance field above is supplied ONLY after actual registered execution
    # and custody review. Nothing here emits that authorization.
    return data,{'normalized_sha256':nh,'normalized_receipt_sha256':rh,'normal_generator_sha256':NORMAL_GENERATOR,'normal_checker_sha256':NORMAL_CHECKER,'original_source_sha256':ORIGINAL}

COVER={
 'base':'B[T,xi]/(rows[0..8],xi*q(T)-1)',
 'q':'r*h0',
 'cubic':'X^3=h0^2/r^7',
 'back_y':'y=X^2*T',
 'back_z':'z=X^3*r',
 'back_s':'s=h0/r^3',
 'target':'H0=s^7; H1=U*s^5; z=s^2',
 'source':'use complete bound normalized A/B and all four maps; no factor or new gauge',
 'scope':'finite etale rank-three parameter cover; not source-map degree; no ideal decision'
}
