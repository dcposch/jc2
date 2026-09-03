#!/usr/bin/env python3
"""(16,12;13;3;X): p.208 shapes and p.209 eta-form, J = cc * x, sat cc != 0."""
from __future__ import annotations
import json, time, sys, os
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from appii_reduce import datum, supports, tail_m3n4, jac_eqs, groebner_sat

x, y = sp.symbols("x y")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)


def conv(o):
    if isinstance(o, dict):
        return {str(k): conv(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [conv(v) for v in o]
    if isinstance(o, sp.Basic):
        return str(o)
    if isinstance(o, (int, float, str, bool)) or o is None:
        return o
    return str(o)


def main():
    t0 = time.time()
    C = datum(16, 12, 13, 3, 1)
    S = supports(C, use_c=True)
    print("Phi", C["delta2"], C["delta1"], "n_h", S["n_h"], "h_free", S["h_free"], S["notes"])

    b1, b2, b3, b4 = sp.symbols("b1:5")
    h = sp.expand(y ** 3 * (y - x) + b1 * y ** 3 + b2 * y ** 2 + b3 * y + b4)
    A = sp.expand(sp.together((h - b4) / y))
    B = sp.expand(sp.together((A - sp.expand(A.subs(y, 0))) / y))
    cc = sp.symbols("cc")

    # --- p.209 eta-form: 4(h)+2(beta2)+3(beta3)+a2 + cc = 11 ---
    bp, bq, br, bs, bt, a2 = sp.symbols("bp bq br bs bt a2")
    beta2 = sp.expand(bp * A + bq)
    beta3 = sp.expand(br * A + bs * B + bt)
    packed = tail_m3n4(h, beta2, beta3, a2, x, y)
    f, g = packed["f"], packed["g"]
    print("eta deg f,g", sp.degree(f, y), sp.degree(g, y),
          "degx", sp.degree(f, x), sp.degree(g, x))
    print("building eta J...")
    tJ = time.time()
    eqs, J = jac_eqs(f, g, cc, 1, x, y)
    print("eta J eqs", len(eqs), "deg_y J", None if J == 0 else sp.degree(J, y),
          "in %.2fs" % (time.time() - tJ))
    names = ["b1", "b2", "b3", "b4", "bp", "bq", "br", "bs", "bt", "a2", "cc"]
    print("ETA MAIN sat cc!=0 ...")
    main_e = groebner_sat(eqs, names, "cc", order="grevlex", timeout=150, engine="singular")
    print("ETA MAIN", main_e.get("verdict"), "size", main_e.get("basis_size"),
          "time", main_e.get("elapsed"))
    print((main_e.get("stdout_tail") or "")[-600:])
    neg = groebner_sat([cc - 1], names, "cc", order="grevlex", timeout=15, engine="singular")
    print("NEG", neg.get("verdict"))

    # --- p.208 (1)-(5) 17+cc if eta did not empty and we have wall left ---
    main17 = None
    remain = 200 - (time.time() - t0)
    if main_e.get("verdict") != "SATURATED-EMPTY" and remain > 80:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols("u1:14")
        alpha2 = c1 * A + c2
        beta2 = c3 * A + c4
        alpha3 = c5 * A + c6 * B + c7
        beta3 = c8 * A + c9 * B + c10
        alpha4 = c11 * A + c12 * B + c13 * (y - x)
        f17 = sp.expand(h ** 3 + beta2 * h + beta3)
        g17 = sp.expand(h ** 4 + alpha2 * h ** 2 + alpha3 * h + alpha4)
        print("building 17-shape J...")
        eqs17, J17 = jac_eqs(f17, g17, cc, 1, x, y)
        print("17 J eqs", len(eqs17))
        names17 = (["b1", "b2", "b3", "b4"] + ["u%d" % i for i in range(1, 14)] + ["cc"])
        main17 = groebner_sat(eqs17, names17, "cc", order="grevlex",
                              timeout=min(150, remain - 10), engine="singular")
        print("17 MAIN", main17.get("verdict"), main17.get("basis_size"), main17.get("elapsed"))

    verdict = "SATURATED-EMPTY" if (
        main_e.get("verdict") == "SATURATED-EMPTY"
        or (main17 and main17.get("verdict") == "SATURATED-EMPTY")
    ) else (main_e.get("verdict") or "UNKNOWN")
    out = dict(
        name="MOH-1612", verdict=verdict,
        n_eta=11, n_eqs_eta=len(eqs), eta=main_e, negative=neg, main17=main17,
        elapsed=time.time() - t0,
        notes=S["notes"] + ["p.209 eta-form 10 shape + cc; p.208 (1)-(5) if needed"],
    )
    with open(os.path.join(OUT, "moh1612.json"), "w") as f:
        json.dump(conv(out), f, indent=2)
    print("WROTE moh1612.json verdict", verdict, "elapsed", out["elapsed"])


if __name__ == "__main__":
    main()
