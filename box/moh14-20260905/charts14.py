#!/usr/bin/env python3
"""Step 3a: size the descended order charts for the 14 rows.

The CHART LOGIC is the charged instrument order_basis_full.py verbatim
(top_face / h_inventory / coeff_inventory / full_basis_gauge_audit /
build_full_spec / native_builder_text).  Only `closed_form` is replaced, by the
multi-level Phi_eff radius map validated in descend14.py against Moh's own
Appendix II table.

THRESHOLD (FALLACY-v2, floor/attainment).  For s'=2 the charged threshold is
B = V2'*delta1' + u'*delta2'.  For s' >= 3 the u' outer roots of h are
distributed over the discs D_2..D_s', so their separation orders are
delta'_2 .. delta'_s', all >= delta'_s'.  Hence
   ord h(sigma) >= V2'*delta1' + u'*delta'_s'  =:  B_safe   <=  B_tight,
and B_safe is the only threshold that yields a NECESSARY over-approximation.
B_tight would be a strict sub-slice and is NOT used for any kill.
"""
import json, sys
from fractions import Fraction as F

sys.path.insert(0, "/home/ubuntu/jc2/box/orderbasis-20260903")
import order_basis_full as OB

ROWSJ = json.load(open("/home/ubuntu/jc2/box/moh14-20260905/descend14.json"))

def make_C(r, mode="safe"):
    d = {int(k): F(v) for k, v in r["delta"].items()}
    B = F(r["Bsafe"]) if mode == "safe" else F(r["Btight"])
    return {"K": r["Kp"], "e": r["ep"], "q": r["qp"], "u": r["up"],
            "R": r["np"] - int(r["Mp"][str(r["sp"])]) - 1, "Pi": r["ep"] + r["qp"],
            "delta1": d[1], "delta2": d[2], "B": B,
            "lambda_P": r["ep"] * B, "lambda_Q": r["qp"] * B,
            "d3prime": 0}

def label(r):
    return "%d,%d|%s|V=%s" % (r["n"], r["m"], ",".join(map(str, r["Ms"])),
                              ",".join(str(v) for _, v in sorted((int(a), b) for a, b in r["V"].items())))

print("== descended chart sizes, SAFE (necessary over-approximation) threshold ==")
print("%-26s %-9s %2s %2s %2s %2s %2s %2s %-7s %5s %-22s %6s %s"
      % ("row", "(n',m')", "K'", "e'", "q'", "V2'", "u'", "l", "B_safe", "#h",
         "alpha/beta dims", "#unk", "partitions"))
print("-" * 150)
SIZES = []
for r in ROWSJ:
    C = make_C(r, "safe")
    Row = OB.Row(key="r", label=label(r), n=r["np"], m=r["mp"],
                 M2=int(r["Mp"][str(r["sp"])]), V2=r["V2p"], k=r["k"])
    try:
        hmons = OB.h_inventory(Row, C)
        alpha = {i: OB.coeff_inventory(C, i) for i in range(1, C["e"] + 1)}
        beta = {i: OB.coeff_inventory(C, i) for i in range(2, C["q"] + 1)}
        nunk = len(hmons) + sum(len(v) for v in alpha.values()) + sum(len(v) for v in beta.values())
        parts = [p for p in OB.partitions(C["u"])] if C["u"] > 0 else [()]
        nunk_tot = nunk + 1  # c
        SIZES.append((nunk_tot, r, len(hmons),
                      [len(alpha[i]) for i in sorted(alpha)],
                      [len(beta[i]) for i in sorted(beta)], parts))
        print("%-26s %-9s %2d %2d %2d %2d %2d %2d %-7s %5d %-22s %6d %s"
              % (label(r)[:26], "(%d,%d)" % (r["np"], r["mp"]), C["K"], C["e"], C["q"],
                 Row.V2, C["u"], r["k"], str(C["B"]), len(hmons),
                 str([len(alpha[i]) for i in sorted(alpha)]) + "/" + str([len(beta[i]) for i in sorted(beta)]),
                 nunk_tot, len(parts)))
    except Exception as exc:
        print("%-26s  EXCEPTION %s" % (label(r)[:26], exc))
        SIZES.append((None, r, None, None, None, None))

print("\n== ordered by chart size (smallest first) ==")
for (nu, r, nh, ad, bd, parts) in sorted([s for s in SIZES if s[0]], key=lambda t: t[0]):
    print("   %6d unknowns  %-26s  (%d,%d) K'=%d u'=%d l=%d  parts=%d"
          % (nu, label(r)[:26], r["np"], r["mp"], r["Kp"], r["up"], r["k"], len(parts)))
json.dump([{"unk": s[0], "row": label(s[1]), "nh": s[2], "alpha": s[3], "beta": s[4],
            "nparts": (len(s[5]) if s[5] is not None else None)} for s in SIZES],
          open("/home/ubuntu/jc2/box/moh14-20260905/chartsizes.json", "w"), indent=1)
