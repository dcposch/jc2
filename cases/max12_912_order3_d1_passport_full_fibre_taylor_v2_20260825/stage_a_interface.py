#!/usr/bin/env python3
"""Fail-closed Stage-A interfaces for the cyclic-D1 incidence.

``--generic-absolute`` emits an AWS Singular navigation job using
``absPrimdecGTZ`` over Q(s,k,mu,nu).  Its absolute primes do *not* by
themselves distinguish a finite extension of the constant field from an
algebraic cover depending on s, so every output is labelled navigation-only.

``--section-verifier`` consumes a small JSON certificate and emits Sage code
that verifies one rational section over a finite extension of
Q(k,mu,nu).  This can certify a positive geometric degree-one section, but it
cannot certify completeness or exclusion.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = Path(__file__).with_name("compile_gate_v2.py")


class StageAFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_compiler():
    spec = importlib.util.spec_from_file_location("d1_v2_stage_a_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise StageAFailure(str(COMPILER))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def generic_absolute_source(engine: str) -> str:
    compiler = load_compiler()
    _, M, ring, rows, _ = compiler.compile_all()
    variables = ",".join(f"A{i}" for i in range(8))
    lines = [
        'LIB "primdec.lib";',
        f"ring R=(0,s,k,mu,nu),({variables}),dp;",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly R{ell}={M.coeff_string(rows[ell], ring.names)};")
    lines.extend([
        "ideal I=R1,R2,R3,R4,R5,R6,R7,R8;",
        f"ideal G={engine}(I);",
        'print("PASS-D1-STAGE-A-GENERIC-GB");',
        'print("generic_dim="+string(dim(G)));',
        'print("generic_vdim="+string(vdim(G)));',
        'print("generic_degree="+string(mult(G)));',
        "def ABS=absPrimdecGTZ(G);",
        "setring ABS;",
        'print("rational_primary_count="+string(size(primary_decomp)));',
        'print("absolute_class_count="+string(size(absolute_primes)));',
        "for (int component=1; component<=size(absolute_primes); component++)",
        "{",
        "  ideal P=std(absolute_primes[component][1]);",
        "  int conjugates=absolute_primes[component][2];",
        '  print("ABSOLUTE_CLASS="+string(component));',
        '  print("conjugates="+string(conjugates));',
        '  print("prime_dim="+string(dim(P)));',
        '  print("prime_vdim="+string(vdim(P)));',
        '  print("prime_degree="+string(mult(P)));',
        '  print("prime_generators_begin");',
        "  P;",
        '  print("prime_generators_end");',
        "}",
        'print("STATUS=NAVIGATION_ONLY");',
        'print("UNRESOLVED=CONSTANT_EXTENSION_VERSUS_S_DEPENDENT_COVER");',
        'print("UNRESOLVED=LOAD_FITTING_AND_DISCRIMINANT_STRATA");',
        'print("NO_GENERIC_ONLY_THEOREM");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def read_certificate(path: Path) -> dict[str, object]:
    certificate = json.loads(path.read_text())
    if certificate.get("schema") != "d1_constant_section_v1":
        raise StageAFailure("wrong certificate schema")
    if not isinstance(certificate.get("A"), list) or len(certificate["A"]) != 8:
        raise StageAFailure("certificate must contain eight A expressions")
    allowed = {
        "schema", "name", "theta_minpoly", "A", "denominators_nonzero",
        "scope", "provenance",
    }
    extra = set(certificate) - allowed
    if extra:
        raise StageAFailure(("unknown certificate fields", sorted(extra)))
    if certificate.get("theta_minpoly") is not None \
            and not isinstance(certificate["theta_minpoly"], str):
        raise StageAFailure("theta_minpoly must be null or a string")
    for expression in certificate["A"]:
        if not isinstance(expression, str):
            raise StageAFailure("A expressions must be strings")
    for expression in certificate.get("denominators_nonzero", []):
        if not isinstance(expression, str):
            raise StageAFailure("nonzero expressions must be strings")
    return certificate


def sage_section_verifier(certificate_path: Path) -> str:
    certificate = read_certificate(certificate_path)
    compiler = load_compiler()
    _, M, ring, rows, _ = compiler.compile_all()
    row_strings = [M.coeff_string(rows[ell], ring.names)
                   for ell in range(1, 9)]
    certificate_sha = sha256(certificate_path.read_bytes()).hexdigest()
    quoted_certificate = json.dumps(certificate, sort_keys=True)
    quoted_rows = json.dumps(row_strings)
    lines = [
        "from sage.all import *",
        "from sage.misc.sage_eval import sage_eval",
        "import hashlib, json, os, platform",
        "if platform.system() != 'Linux': raise SystemExit('REFUSE_NON_LINUX')",
        "from pathlib import Path",
        "vendor_path=Path('/sys/class/dmi/id/sys_vendor')",
        "vendor=vendor_path.read_text().strip() if vendor_path.is_file() else ''",
        "if vendor!='Amazon EC2': raise SystemExit('REFUSE_NON_AWS_EC2')",
        "tag=os.environ.get('JC2_AWS_TAG','')",
        "if not tag.startswith('max12_912_order3_d1_'): raise SystemExit('REFUSE_UNREGISTERED_AWS_TAG')",
        f"certificate=json.loads({json.dumps(quoted_certificate)})",
        f"expected_certificate_sha={certificate_sha!r}",
        f"row_strings=json.loads({json.dumps(quoted_rows)})",
        "Cpoly=PolynomialRing(QQ,names=('k','mu','nu'))",
        "k,mu,nu=Cpoly.gens()",
        "C=Cpoly.fraction_field()",
        "k,mu,nu=map(C,(k,mu,nu))",
        "theta_minpoly=certificate.get('theta_minpoly')",
        "if theta_minpoly is None:",
        "    L=C",
        "    theta=L(0)",
        "else:",
        "    CT=PolynomialRing(C,'T'); T=CT.gen()",
        "    mp=CT(sage_eval(theta_minpoly,locals={'T':T,'k':k,'mu':mu,'nu':nu}))",
        "    if mp.degree()<2 or not mp.is_irreducible(): raise AssertionError('constant minpoly not irreducible degree>=2')",
        "    L=C.extension(mp,'theta'); theta=L.gen()",
        "S=PolynomialRing(L,'s'); s=S.gen(); Ks=S.fraction_field()",
        "k,mu,nu=map(Ks,(L(k),L(mu),L(nu))); theta=Ks(L(theta))",
        "environment={'s':s,'k':k,'mu':mu,'nu':nu,'theta':theta}",
        "A=[Ks(sage_eval(expr,locals=environment)) for expr in certificate['A']]",
        "environment.update({f'A{i}':A[i] for i in range(8)})",
        "if k==0: raise AssertionError('certificate is not on k!=0 chart')",
        "for expression in certificate.get('denominators_nonzero',[]):",
        "    if Ks(sage_eval(expression,locals=environment))==0: raise AssertionError(('declared denominator zero',expression))",
        "for index,expression in enumerate(row_strings,1):",
        "    value=Ks(sage_eval(expression,locals=environment))",
        "    if value!=0: raise AssertionError(('source row nonzero',index,value))",
        "print('PASS-D1-EXACT-CONSTANT-FIELD-SECTION-CERTIFICATE')",
        "print('geometric_degree_over_P1_s=1')",
        "print('finite_constant_extension_only=YES')",
        "print('completeness=NOT_CERTIFIED')",
        "print('Taylor=NOT_CERTIFIED')",
        "print('certificate_sha256='+expected_certificate_sha)",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generic-absolute", action="store_true")
    group.add_argument("--section-verifier", type=Path)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()
    require_aws()
    if args.generic_absolute:
        print(generic_absolute_source(args.engine), end="")
    else:
        print(sage_section_verifier(args.section_verifier), end="")


if __name__ == "__main__":
    main()
