#!/usr/bin/env python3
"""Emit the exact Q[c] modStd frozen-d4 selected landing test."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
ORDER3 = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
ORDER3_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_compiler():
    for path, expected in ((COMPILER, COMPILER_SHA256), (ORDER3, ORDER3_SHA256)):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_b1_finite_c_modstd_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    q = load_compiler()
    _, rows, imposed, names = q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    lines = [
        'LIB "elim.lib";',
        'LIB "modstd.lib";',
        'ring T=0,(x,y),dp;',
        'ideal TI=x+y,x-y;',
        'ideal TG=modStd(TI,1);',
        'int control_zero=1;int ti;for(ti=1;ti<=size(TI);ti++){if(reduce(TI[ti],TG)!=0){control_zero=0;}}',
        'print("modstd_control_zero="+string(control_zero));',
        'ring S=0,(w,c,d2,d4,x1,x3,x5),dp;',
    ]
    for ell in range(1, 9):
        lines.append(f"poly se{ell}={q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal SI=" + ",".join(f"se{i}" for i in imposed) + ";",
        'ring R=0,(zinv,w,u,x1,x3,x5,c),(dp(1),dp(5),dp(1));',
        'option(redSB);',
        'map phi=S,w,c,2+u,1,x1,x3,x5;',
        'ideal I=phi(SI);poly A=x3-2*x5;',
        'ideal J=I,zinv*w*x5*A-1;',
        'ideal GJ=modStd(J,1);',
        'int original_remainders_zero=1;int ji;for(ji=1;ji<=size(J);ji++){if(reduce(J[ji],GJ)!=0){original_remainders_zero=0;}}',
        'ideal C=eliminate(GJ,zinv);',
        'ideal GC=modStd(C,1);',
        'int contraction_remainders_zero=1;int ci;for(ci=1;ci<=size(C);ci++){if(reduce(C[ci],GC)!=0){contraction_remainders_zero=0;}}',
        'ideal Landing=GC,w,u,x1,x3,x5;',
        'ideal GL=modStd(Landing,1);',
        'int landing_remainders_zero=1;int li;for(li=1;li<=size(Landing);li++){if(reduce(Landing[li],GL)!=0){landing_remainders_zero=0;}}',
        'int landing_empty=0;if(reduce(1,GL)==0){landing_empty=1;}',
        'print("Q8-W0-RANKDROP-B1-FINITE-C-MODSTD");',
        'print("field=Q-polynomial-c");',
        'print("modstd_control_zero="+string(control_zero));',
        'print("original_remainders_zero="+string(original_remainders_zero));',
        'print("contraction_remainders_zero="+string(contraction_remainders_zero));',
        'print("landing_remainders_zero="+string(landing_remainders_zero));',
        'print("landing_empty="+string(landing_empty));',
        'print("GJ_BASIS_BEGIN");GJ;print("GJ_BASIS_END");',
        'print("GC_BASIS_BEGIN");GC;print("GC_BASIS_END");',
        'print("GL_BASIS_BEGIN");GL;print("GL_BASIS_END");',
        'print("Q8_W0_RANKDROP_B1_FINITE_C_MODSTD_PASS");',
        'exit;',
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
