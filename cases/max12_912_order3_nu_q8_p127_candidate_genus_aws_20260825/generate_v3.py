#!/usr/bin/env python3
"""Corrected fail-closed Singular genus diagnostics for candidate H."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import generate_v2 as base


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument(
        "--mode", choices=("normal", "brnoeth", "singular", "discriminant"), required=True
    )
    args = parser.parse_args()
    got = sha256(args.candidate.read_bytes()).hexdigest()
    if got != base.CANDIDATE_SHA256:
        raise RuntimeError((got, base.CANDIDATE_SHA256))
    payload = json.loads(args.candidate.read_text())
    if (
        payload.get("status") != "PASS"
        or payload.get("prime") != base.P
        or payload.get("degree_v") != 190
        or payload["nonzero_support"].get("190") != [[0, 1]]
    ):
        raise RuntimeError("candidate endpoint mismatch")
    h = base.polynomial(payload)
    print("ring R=127,(w,v),dp;")
    print(f"poly H={h};")
    print('print("Q8-P127-CANDIDATE-GENUS-DIAGNOSTIC-V3");')
    print(f'print("mode={args.mode}");')
    print('print("candidate_sha256=' + got + '");')
    print('print("degree_H="+string(deg(H)));')
    print('print("degree_v_H=190");')
    print('print("degree_w_H=21");')
    if args.mode == "normal":
        print('LIB "normal.lib";')
        print("ideal I=H;")
        print('print("input_dim="+string(dim(std(I))));')
        print('print("normal_genus_begin");')
        print("int geometric_genus=genus(I);")
        print('print("geometric_genus="+string(geometric_genus));')
        print('print("normal_genus_end");')
    elif args.mode == "brnoeth":
        print('LIB "brnoeth.lib";')
        print('print("adj_div_begin");')
        print("list CURVE=Adj_div(H);")
        print('print("curve_degree_genus="+string(CURVE[2]));')
        print('print("closed_place_count="+string(size(CURVE[3])));')
        print('print("closed_places_begin");')
        print("CURVE[3];")
        print('print("closed_places_end");')
        print('print("conductor_begin");')
        print("CURVE[4];")
        print('print("conductor_end");')
        print('print("adj_div_end");')
    elif args.mode == "singular":
        print("poly Hw=diff(H,w); poly Hv=diff(H,v);")
        print("ideal S=H,Hw,Hv;")
        print("ideal G=std(S);")
        print('print("singular_locus_dim="+string(dim(G)));')
        print('if(dim(G)==0){print("singular_locus_vdim="+string(vdim(G)));}')
        print('print("singular_basis_begin"); G; print("singular_basis_end");')
        print("ring T=127,(u,w,v),dp;")
        print("ideal ST=imap(R,S),u*w*v-1;")
        print("ideal GT=std(ST);")
        print('print("torus_singular_dim="+string(dim(GT)));')
        print('if(dim(GT)==0){print("torus_singular_vdim="+string(vdim(GT)));}')
        print('print("torus_unit="+string(size(GT)==1 && GT[1]==1));')
    else:
        print("poly Hv=diff(H,v);")
        print('print("discriminant_begin");')
        print("poly D=resultant(H,Hv,v);")
        print('print("resultant_total_degree="+string(deg(D)));')
        print('print("resultant_w_degree="+string(deg(D)));')
        print("poly Ds=gcd(D,diff(D,w));")
        print('print("resultant_derivative_gcd_degree="+string(deg(Ds)));')
        print('print("resultant_squarefree_radical_degree="+string(deg(D)-deg(Ds)));')
        print('print("discriminant_end");')


if __name__ == "__main__":
    main()
