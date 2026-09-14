#!/usr/bin/env python3
"""Derive minor leaders and maps; no stored solved h3 map is used.

The branch datum supplies split multiplicities [2,1] or [1,1,1].  The
monic degree-three leader is formed as a product of its roots.  Exponents
are computed from the eleven h3 root factors, not copied from old rows.
Corrected mode carries every minor centre (including the delta2 at-level
location).  Old mode is solely the historical restricted-chart control.
"""
from __future__ import annotations
from functools import lru_cache
from math import comb, factorial
import hashlib
import json
import sympy as sp

S = sp.Symbol
TZ = dict[tuple[int, int], sp.Expr]


def branch_data(branch: str, mode: str = "corrected") -> dict:
    assert mode in ("corrected", "old")
    if branch == "delta2":
        radius = sp.Rational(2)
        free = [S("rho"), S("u")]
        if mode == "corrected":
            free += [S("jet0"), S("minor_a2")]
        return {"radius": radius, "denominator": int(radius.q),
                "parameters": free, "localizer": S("rho"),
                "w_terms": [(1, 0, S("jet0")), (2, 0, S("u")),
                            (3, 0, S("minor_a2")), (3, 1, sp.Integer(1))]
                    if mode == "corrected" else
                           [(2, 0, S("u")), (3, 1, sp.Integer(1))]}
    if branch == "delta52":
        radius = sp.Rational(5, 2)
        free = [S("u"), S("v"), S("c")]
        if mode == "corrected":
            free += [S("jet0")]
        return {"radius": radius, "denominator": int(radius.q),
                "parameters": free, "localizer": S("c"),
                "w_terms": [(2, 0, S("jet0")), (4, 0, S("u")),
                            (6, 0, S("v")), (7, 1, sp.Integer(1))]
                    if mode == "corrected" else
                           [(4, 0, S("u")), (6, 0, S("v")),
                            (7, 1, sp.Integer(1))]}
    raise ValueError(branch)


def derive_minor_face(branch: str) -> tuple[sp.Expr, dict]:
    """Product from the branch roots; conjugate-pair elimination is exact."""
    zeta, a = sp.symbols("zeta minor_orbit_root")
    if branch == "delta2":
        # r_double is absorbed into the free at-level centre minor_a2.
        # Defining rho as one third of the signed root separation is invertible.
        roots = [(sp.Integer(0), 2), (-sp.Integer(3)*S("rho"), 1)]
        face = sp.prod((zeta-root)**multiplicity for root, multiplicity in roots)
        proof = {"root_multiplicities": [2,1],
                 "double_root_location": "minor_a2 (carried in the source series)",
                 "signed_separation_coordinate": "3*rho", "root_source": "branch datum"}
    elif branch == "delta52":
        roots = [(sp.Integer(0), 1), (a, 1), (-a, 1)]
        orbit_product = sp.expand(sp.prod((zeta-root)**m for root,m in roots))
        face = sp.rem(orbit_product, a*a-S("c"), a)
        assert sp.expand(face.subs(zeta,-zeta)+face) == 0
        proof = {"root_multiplicities": [1,1,1], "deck_action": "zeta -> -zeta",
                 "orbit_relation": "minor_orbit_root^2=c", "root_source": "branch datum and denominator-two deck action"}
    else:
        raise ValueError(branch)
    return sp.expand(face), proof


def minor_order(branch: str, degree: int = 11) -> dict:
    """Root counts scale by degree/11 in this 3:8 leading split."""
    data = branch_data(branch)
    count_minor = sp.Rational(3*degree,11)
    count_major = sp.Rational(8*degree,11)
    value = count_minor*data["radius"] + count_major*(-1)
    normalized = data["denominator"]*(degree+value)
    assert count_minor.q == count_major.q == normalized.q == 1
    return {"degree": degree, "minor_root_count": int(count_minor),
            "other_root_count": int(count_major), "valuation": str(value),
            "cover": data["denominator"], "normalized_power": int(normalized)}


@lru_cache(maxsize=512)
def _w_power(j: int, branch: str, max_power: int, mode: str) -> tuple:
    terms = branch_data(branch,mode)["w_terms"]
    output = {}
    def visit(index, left, power, coordinate, scalar):
        if index == len(terms)-1:
            n,k,c = terms[index]
            target = power+left*n
            if target <= max_power:
                key=(target,coordinate+left*k)
                output[key] = output.get(key,0)+scalar*c**left
            return
        n,k,c = terms[index]
        for take in range(left+1):
            target=power+take*n
            # Every remaining factor has the following minimum s-exponent.
            minimum=min(term[0] for term in terms[index+1:])
            if target+(left-take)*minimum > max_power:
                continue
            visit(index+1,left-take,target,coordinate+take*k,
                  scalar*comb(left,take)*c**take)
    visit(0,j,0,0,sp.Integer(1))
    return tuple((n,k,sp.expand(c)) for (n,k),c in sorted(output.items()) if c != 0)


def local_rows(item: TZ, branch: str, max_power: int,
               exact_only: bool = True, mode: str = "corrected") -> TZ:
    """Pull back every represented monomial at the full carried centre.

    exact_only is retained for historical API compatibility; the frozen
    implementation also returns every row through max_power.
    """
    denom = branch_data(branch,mode)["denominator"]
    wbands = {}
    for (r,q), value in item.items():
        if denom*r > max_power:
            continue
        band = wbands.setdefault(r,{})
        for j in range(q+1):
            band[j] = band.get(j,0) + value*comb(q,j)*(-1)**(q-j)
    output={}
    for r,band in sorted(wbands.items()):
        for j,value in sorted(band.items()):
            value=sp.expand(value)
            if value == 0:
                continue
            for n,k,c in _w_power(j,branch,max_power-denom*r,mode):
                key=(denom*r+n,k)
                output[key] = output.get(key,0)+value*c
    return {tag:image for tag,value in sorted(output.items())
            if (image:=sp.expand(value)) != 0}


def _rational_reduce(rows, variables):
    work=[(label,sp.expand(row)) for label,row in rows if row != 0]
    eligible=set(variables)
    mapping={}
    pivots=[]
    while True:
        choice=None
        for index,(label,row) in enumerate(work):
            for variable in sorted(row.free_symbols & eligible,key=str):
                leader=sp.diff(row,variable)
                if leader.is_Rational and leader != 0:
                    remainder=sp.expand(row-leader*variable)
                    if variable not in remainder.free_symbols:
                        choice=index,label,variable,leader,remainder
                        break
            if choice is not None:
                break
        if choice is None:
            break
        index,label,variable,leader,remainder=choice
        rhs=sp.expand(-remainder/leader)
        mapping[variable]=rhs
        eligible.remove(variable)
        pivots.append({"label":label,"variable":str(variable),"coefficient":str(leader)})
        del work[index]
        work=[(label,image) for label,row in work
              if (image:=sp.expand(row.subs(variable,rhs))) != 0]
    # Reverse triangular replacement produces a simultaneous substitution map.
    resolved={}
    for variable,rhs in reversed(list(mapping.items())):
        resolved[variable]=sp.expand(rhs.xreplace(resolved))
    assert not any(rhs.free_symbols & set(resolved) for rhs in resolved.values())
    return work,resolved,pivots


def derive_minor_map(branch: str, h3: TZ, variables, mode: str = "corrected"):
    data=branch_data(branch,mode)
    order=minor_order(branch)
    power=order["normalized_power"]
    face,face_proof=derive_minor_face(branch)
    target={(power,int(key[0])):coefficient
            for key,coefficient in sp.Poly(face,S("zeta")).terms()}
    raw=local_rows(h3,branch,power,False,mode)
    equations=[(f"h3_minor_s{n}_q{k}",sp.expand(raw.get((n,k),0)-target.get((n,k),0)))
               for n,k in sorted(set(raw)|set(target))]
    if mode == "old" and branch == "delta52":
        # Historical pin only.  It is explicitly excluded from corrected mode.
        equations.append(("historical_unsupported_Hc_11_0_pin",S("Hc_11_0")))
    residual,mapping,pivots=_rational_reduce(equations,variables)
    if residual:
        raise AssertionError("minor leader has residual: "+str(residual[:3]))
    rechecked=[sp.expand(row.xreplace(mapping)) for _,row in equations]
    assert all(row == 0 for row in rechecked), "a derived minor map failed exact substitution"
    free=sorted((set(variables)-set(mapping)) | set(data["parameters"]),key=str)
    if mode == "corrected":
        assert S("Hc_11_0") in free
    digest=hashlib.sha256("\n".join(label+"="+str(row) for label,row in equations).encode()).hexdigest()
    meta={"mode":mode,"parameters":[str(v) for v in data["parameters"]],
          "localization":str(data["localizer"])+"!=0", "face":str(face),
          "face_derivation":face_proof,"pole_order_derivation":order,
          "raw_rows":len(equations),"raw_rows_sha256":digest,
          "pivots":pivots,"residual_count":0,"every_row_rechecked":True,
          "minor_series":
            ("y=jet0+u*t+(minor_a2+zeta)*t^2" if branch=="delta2" else
             "y=jet0+u*t+v*t^2+zeta*t^(5/2)") if mode=="corrected" else
            ("y=u*t+zeta*t^2" if branch=="delta2" else
             "y=u*t+v*t^2+zeta*t^(5/2)"),
          "Hc_11_0":"free" if mode=="corrected" or branch=="delta2" else "historical unsupported pin",
          "coefficient_field":"QQ","parameter_divisions":[],
          "free_generators":[str(v) for v in free]}
    return mapping,free,meta
