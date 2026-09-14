#!/usr/bin/env python3
"""Emit a replayable Singular system for the complete nonlinear bridge.

The emitted program uses the quotient ``s^1179=0`` only while assembling the
minor-jet products.  It then splits every coefficient in ``s`` and ``pi`` and
maps those coefficient polynomials to an ordinary chart ring before Q*-style
affine elimination and Groebner computation.  Thus ``s`` and ``pi`` are
bookkeeping variables, not existential variables of the chart.

This file is a next-system generator.  Generation and each Singular run are
separate foreground jobs and should be wrapped in ``timeout 3000``.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import os
from pathlib import Path
import sys

for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_name, "1")

import sympy as sp


HERE = Path(__file__).resolve().parent
BRIDGE_PATH = HERE / "bridge_engine.py"
CAP = 1178
T2_CAP = 391
ALLOWED_CHARACTERISTICS = (0, 32003, 104729, 1299709)


def load_bridge():
    spec = importlib.util.spec_from_file_location("g9966_bridge_full_qring", BRIDGE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {BRIDGE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sx(expression: sp.Expr) -> str:
    """SymPy expression in Singular syntax, without forced expansion."""
    return sp.sstr(expression).replace("**", "^")


def component_statements(name: str, item, joint_map, chunk: int = 128) -> list[str]:
    terms: list[str] = []
    for (r, q), raw in sorted(item.items()):
        if 2 * r > CAP:
            continue
        coefficient = raw.xreplace(joint_map)
        if coefficient == 0:
            continue
        terms.append(f"({sx(coefficient)})*s^{2*r}*zp{q}")
    statements = [f"poly {name}=0;"]
    for start in range(0, len(terms), chunk):
        statements.append(f"{name}=trunc({name}+" + "+".join(terms[start:start + chunk]) + ");")
    statements.append(f'print("COMPONENT {name} terms={len(terms)} size="+string(size({name})));')
    return statements


def extraction_block(source: str, cap: int, prefix: str) -> str:
    # coef() returns a two-row matrix: monomials in the selected variable and
    # their coefficients.  A second call removes pi.  Missing coefficients
    # are identically zero and correctly contribute no generator.
    return f"""
matrix CS_{prefix}=coef({source},s);
matrix CP_{prefix};
for(js=1;js<=ncols(CS_{prefix});js++)
{{
  // The first coef() row is a pure power of s, so total degree is its
  // s-exponent (Singular's two-argument deg expects an intvec, not a var).
  ns=deg(CS_{prefix}[1,js]);
  if(ns<={cap})
  {{
    CP_{prefix}=coef(CS_{prefix}[2,js],pi);
    for(jp=1;jp<=ncols(CP_{prefix});jp++)
    {{
      // Likewise this monomial is a pure power of pi.
      kp=deg(CP_{prefix}[1,jp]);
      rr=CP_{prefix}[2,jp];
      if(rr!=0)
      {{
        if(diff(rr,s)!=0 || diff(rr,pi)!=0)
        {{
          ERROR("coefficient extraction left a bookkeeping variable");
        }}
        Rows[size(Rows)+1]=rr;
        Labels[size(Labels)+1]="{prefix}_s"+string(ns)+"_pi"+string(kp);
      }}
    }}
  }}
}}
"""


def emit(characteristic: int, normalized_jacobian: bool, gauge_c: bool, output: Path) -> None:
    if characteristic not in ALLOWED_CHARACTERISTICS:
        raise ValueError(f"characteristic must be one of {ALLOWED_CHARACTERISTICS}")
    bridge = load_bridge()
    custody = bridge.verify_frozen()
    band = bridge.load_charged_module()
    _stage, free_names, joint_map, k2, outer, endpoint = bridge.load_endpoint(band)

    pieces = {"H": k2}
    for name in ("A2", "A3", "B1", "B2"):
        pieces[name] = band.outer_effective_tz(outer, name, 200)
    max_q = max(q for item in pieces.values() for _r, q in item)

    t2_names = ["T2_a1", "T2_a0", "T2_b1", "T2_b0"]
    t3_names = bridge.t3_coefficient_names()
    base_names = list(free_names) + t2_names + t3_names
    if not normalized_jacobian:
        base_names.append("kappa")
    assert len(base_names) == (907 if normalized_jacobian else 908)
    assert len(base_names) == len(set(base_names))

    # This is the genuine [t^163 w^0] coefficient of the normalized Jacobian,
    # computed in the charged chart before the minor pullback.
    jacobian = bridge.jacobian_scalar(band, k2, outer, joint_map)
    assert jacobian.free_symbols <= set(map(sp.Symbol, free_names))

    denominators = {1, 2, 4, 5}
    for item in pieces.values():
        for raw in item.values():
            image = raw.xreplace(joint_map)
            denominators.update(int(value.q) for value in image.atoms(sp.Rational))
    denominators.update(int(value.q) for value in jacobian.atoms(sp.Rational))
    if characteristic:
        bad = sorted(value for value in denominators if value % characteristic == 0)
        if bad:
            raise RuntimeError(
                f"characteristic {characteristic} divides source denominators: {bad[:8]}"
            )
    denominator_digest = hashlib.sha256(
        "".join(f"{value}\n" for value in sorted(denominators)).encode()
    ).hexdigest()

    z_powers = ["poly zp0=1;", "poly zeta=-1+u*s^4+v*s^6+pi*s^7;"]
    for q in range(1, max_q + 1):
        z_powers.append(f"poly zp{q}=trunc(zp{q-1}*zeta);")

    components: list[str] = []
    for name in ("H", "A2", "A3", "B1", "B2"):
        components.extend(component_statements(name, pieces[name], joint_map))

    alpha_terms = []
    for i in range(2, 10):
        for m in range((2 * i) // 3 + 1):
            if (i, m) == (9, 6):
                continue
            shift = 132 * i - 198 * m
            assert shift >= 0
            alpha_terms.append(
                f"U3=trunc(U3+T3_a{i}_m{m}*s^{shift}*F{m}*G{9-i});"
            )
    assert len(alpha_terms) == 34

    if normalized_jacobian:
        jac_row = f"({sx(jacobian)})-1"
        t3_scale = "1"
        wrapper = "Zc*c-1"
        control_block = """
ideal Czero=c,Zc*c-1;
ideal Cone=c-1,Zc*c-1;
print("BEGIN_CONTROLS");
print(reduce(1,std(Czero))); // expected 0: c=0 excluded
print(reduce(1,std(Cone)));  // expected 1: c=1 retained
print("END_CONTROLS");
"""
        excluded_names = ("c", "s", "pi")
    else:
        jac_row = f"({sx(jacobian)})-kappa"
        t3_scale = "kappa"
        wrapper = "Zck*c*kappa-1"
        control_block = """
ideal Czero=c,Zck*c*kappa-1;
ideal Kzero=kappa,Zck*c*kappa-1;
ideal Cone=c-1,kappa-1,Zck*c*kappa-1;
print("BEGIN_CONTROLS");
print(reduce(1,std(Czero))); // expected 0: c=0 excluded
print(reduce(1,std(Kzero))); // expected 0: kappa=0 excluded
print(reduce(1,std(Cone)));  // expected 1: c=kappa=1 retained
print("END_CONTROLS");
"""
        excluded_names = ("c", "kappa", "s", "pi")

    gauge_statement = "Rows[size(Rows)+1]=c-1; Labels[size(Labels)+1]=\"gauge_c\";" if gauge_c else ""
    exact_certificate = ""
    if characteristic == 0:
        exact_certificate = """
if(reduce(1,G)==0)
{
  ideal Unity=1;
  matrix Cert=lift(I,Unity);
  matrix Check=matrix(I)*Cert;
  if(Check[1,1]!=1) { ERROR("failed exact unit-certificate identity"); }
  print("BEGIN_EXACT_CERTIFICATE");
  for(ci=1;ci<=nrows(Cert);ci++)
  {
    print("generator_"+string(ci)+" coefficient="+string(Cert[ci,1]));
  }
  print("verified_sum_generator_times_coefficient=1");
  print("END_EXACT_CERTIFICATE");
}
"""

    # Pivots are found after coefficient splitting.  In characteristic zero
    # these are exactly QQ* pivots.  In a prime field they are only modular
    # affine preprocessing and must not be promoted as rational pivots.
    qstar = f"""
list PivotVariable, PivotCoefficient, PivotRHS, PivotLabel;
int np=0;
int changed=1;
int ri,vi,jj;
poly ff,xx,dd,rhs;
ideal VV;
while(changed)
{{
  changed=0;
  for(ri=1;ri<=size(Rows);ri++)
  {{
    ff=Rows[ri];
    if(ff!=0)
    {{
      VV=variables(ff);
      for(vi=1;vi<=size(VV);vi++)
      {{
        xx=VV[vi];
        if({" && ".join(f"xx!={name}" for name in excluded_names)})
        {{
          dd=diff(ff,xx);
          if(dd!=0 && deg(dd)==0)
          {{
            rhs=-subst(ff,xx,0)/dd;
            np++;
            PivotVariable[np]=string(xx);
            PivotCoefficient[np]=string(dd);
            PivotRHS[np]=string(rhs);
            PivotLabel[np]=Labels[ri];
            for(jj=1;jj<=size(Rows);jj++)
            {{
              if(jj!=ri)
              {{
                Rows[jj]=reduce(subst(Rows[jj],xx,rhs),std(0));
              }}
            }}
            Rows=delete(Rows,ri);
            Labels=delete(Labels,ri);
            changed=1;
            break;
          }}
        }}
      }}
    }}
    if(changed) {{ break; }}
  }}
}}
print("BEGIN_AFFINE_PIVOTS");
print("count="+string(np));
for(ri=1;ri<=np;ri++)
{{
  print("label="+PivotLabel[ri]+" variable="+PivotVariable[ri]+" coefficient="+PivotCoefficient[ri]+" rhs="+PivotRHS[ri]);
}}
print("END_AFFINE_PIVOTS");
ideal Residual;
for(ri=1;ri<=size(Rows);ri++)
{{
  if(Rows[ri]!=0) {{ Residual[size(Residual)+1]=Rows[ri]; }}
}}
print("residual_count="+string(size(Residual)));
"""

    wrapper_name = "Zc" if normalized_jacobian else "Zck"
    ring0_names = base_names + ["s", "pi"]
    # Keep the two bookkeeping names during imap from the quotient ring, then
    # kill them explicitly.  This makes the source/target ring map literal;
    # the two variables and two equations have zero net dimension effect.
    elimination_names = base_names + ["s", "pi", wrapper_name]
    provenance = (
        f"// charged_inputs={custody['count']} all_match={int(custody['all_match'])}\n"
        f"// stage7_sha256={endpoint['stage7_sha256']}\n"
        f"// free_list_sha256={endpoint['free_list_sha256']}\n"
        f"// bridge_generator_sha256={hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}\n"
        f"// characteristic={characteristic} normalized_jacobian={int(normalized_jacobian)} gauge_c={int(gauge_c)}\n"
        f"// source_denominator_count={len(denominators)} source_denominators_sha256={denominator_digest}\n"
    )

    script = f"""{provenance}
LIB "general.lib";
ring P={characteristic},({','.join(ring0_names)}),dp;
ideal Truncation=s^{CAP+1};
qring Q=std(Truncation);
proc trunc(poly f) {{ return(reduce(f,std(0))); }}
{"\n".join(z_powers)}
{"\n".join(components)}

poly H2=trunc(H*H);
poly H3=trunc(H2*H);
poly H4=trunc(H2*H2);
poly EF=trunc(A2*H+A3);
poly EG=trunc(B1*H+B2);
poly F0=1;
poly F1=trunc(H3+EF);
poly F2=trunc(F1*F1);
poly F3=trunc(F2*F1);
poly F4=trunc(F3*F1);
poly F5=trunc(F4*F1);
poly G0=1;
poly G1=trunc(H2+EG);
poly G2=trunc(G1*G1);
poly G3=trunc(G2*G1);
poly G4=trunc(G3*G1);
poly G5=trunc(G4*G1);
poly G6=trunc(G5*G1);
poly G7=trunc(G6*G1);
poly EG2=trunc(EG*EG);
poly EG3=trunc(EG2*EG);
poly EF2=trunc(EF*EF);
poly D2=trunc(3*H4*EG+3*H2*EG2+EG3-2*H3*EF-EF2);
poly U2=trunc(D2+T2_a1*s^66*F1*G1+T2_a0*s^264*G1+T2_b1*s^198*F1+T2_b0*s^396);
poly p=pi*(pi^2-c);
poly E2=trunc(U2-s^{T2_CAP}*p^5);
poly D3=trunc(D2*(G6+G3*F2+F4));
poly U3=D3;
{"\n".join(alpha_terms)}
poly q1=-pi^10/5+3*c*pi^8/4-c^2*pi^6+c^3*pi^4/2;
poly E3=trunc(U3-s^{CAP}*({t3_scale})*p^10*q1);

ideal Rows;
list Labels;
int js,jp,ns,kp;
poly rr;
{extraction_block('E2', T2_CAP, 'T2')}
{extraction_block('E3', CAP, 'T3')}
Rows[size(Rows)+1]={jac_row}; Labels[size(Labels)+1]="Jacobian_constant";
{gauge_statement}
print("raw_coefficient_rows="+string(size(Rows)));
{qstar}

ring E={characteristic},({','.join(elimination_names)}),dp;
ideal I=imap(Q,Residual);
I[size(I)+1]=s;
I[size(I)+1]=pi;
I[size(I)+1]={wrapper};
option(redSB);
ideal G=std(I);
print("BEGIN_RESULT");
print("unit_remainder="+string(reduce(1,G)));
print("active_ring_dimension_with_pivot_variables="+string(dim(G)));
if(dim(G)>=0) {{ print("localized_dimension_after_affine_pivots="+string(dim(G)-np)); }}
print("basis_size="+string(size(G)));
print("END_RESULT");
{control_block}
{exact_certificate}
quit;
"""
    encoded = script.encode()
    if len(encoded) > 256 * 1024 * 1024:
        raise RuntimeError("refusing an unexpectedly unbounded Singular artifact (>256 MiB)")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(encoded)
    print(f"wrote {output} bytes={len(encoded)} sha256={hashlib.sha256(encoded).hexdigest()}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, choices=ALLOWED_CHARACTERISTICS, default=32003)
    parser.add_argument("--normalized-jacobian", action="store_true",
                        help="impose J0=1 and target p^10*q1; default keeps kappa, J0=kappa, and target kappa*p^10*q1")
    parser.add_argument("--gauge-c", action="store_true", help="also impose the explicit slice c=1")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    suffix = "Q" if args.characteristic == 0 else f"p{args.characteristic}"
    mode = "J1" if args.normalized_jacobian else "Jkappa"
    output = args.output or HERE / f"full-bridge-{suffix}-{mode}.sing"
    emit(args.characteristic, args.normalized_jacobian, args.gauge_c, output)


if __name__ == "__main__":
    main()
