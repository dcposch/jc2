#!/usr/bin/env python3
"""Freeze and verify the audit-only integral exponent decoding correction."""
import hashlib,json,sys
from pathlib import Path
import sympy as sp
N=Path(__file__).resolve().parent;sys.path.insert(0,str(N/'print-audit-flint-runtime'))
import flint
original=N/'deep_flint_jacobian_pair.py';corrected=N/'print-audit-corner-pair-backend.py'
a=original.read_text();b=corrected.read_text()
assert b==a.replace('v**n for v,n','v**int(n) for v,n')
before=N/'print-audit-corner-pair-before-cast.py';before.write_text(a)
ctx=flint.fmpq_mpoly_ctx.get(('w','A_early','zz_late'),'lex')
monomials={(2,1,0):flint.fmpq(3,7),(0,0,13):flint.fmpq(-11,17),(1,5,4):flint.fmpq(19,23),(0,0,0):flint.fmpq(5,29)}
native=ctx.from_dict(monomials);variables=sp.symbols('w A_early zz_late')
reconstructed=sum(sp.Rational(int(c.numerator),int(c.denominator))*sp.Mul(*(v**int(n) for v,n in zip(variables,exps) if n)) for exps,c in native.to_dict().items())
expected=sum(sp.Rational(int(c.numerator),int(c.denominator))*sp.Mul(*(v**n for v,n in zip(variables,exps) if n)) for exps,c in monomials.items())
assert sp.expand(reconstructed-expected)==0 and not reconstructed.atoms(sp.Float)
for power in reconstructed.atoms(sp.Pow):assert power.exp.is_Integer and power.exp>=0
legacy=variables[1]**flint.fmpz(1)
assert legacy.atoms(sp.Float),'This records the actually observed local SymPy1.12/fmpz decoding incompatibility.'
rejected=False
try:sp.Poly(legacy,variables[1],domain=sp.QQ)
except sp.PolynomialError:rejected=True
assert rejected
record={'status':'PASS','flint_version':flint.__version__,'sympy_version':sp.__version__,
 'sole_audit_backend_change':'v**n -> v**int(n) when decoding exact nonnegative FLINT exponent integers',
 'exact_mixed_monomial_roundtrip':True,'all_exponents_nonnegative_sympy_Integer':True,
 'legacy_float_exponent_negative_control':str(legacy),'legacy_polynomial_rejected':True,
 'system_packages_modified':False,'runtime_scope':str(N/'print-audit-flint-runtime'),
 'corrected_backend_sha256':hashlib.sha256(corrected.read_bytes()).hexdigest(),
 'frozen_before_cast_sha256':hashlib.sha256(before.read_bytes()).hexdigest(),
 'runtime_receipt_sha256':hashlib.sha256((N/'print-audit-flint-runtime-receipt.json').read_bytes()).hexdigest(),
 'control_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');print(json.dumps(record,indent=2))
