"""Emit Generator-A systems for all reduced cases of GGV-Horruitiner 2022 (arXiv:2204.14178).

Solved cases (regression suite -- expect EMPTY, i.e. msolve GB = [1]):
  Prop 4.1 (9,27)  -> (72,108) #1 : [P,Q] = x
  Prop 4.2 (9,24)  -> (66,99), 3 subcases : [P,Q] = x
  Prop 4.4 (7,21)  -> (56,84) : [P,Q] = x
Open case (the target):
  Prop 4.3 (8,28)  -> (108,72), 2 subcases : [P,Q] = x^2
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from jc import SystemA

X, X2 = (1, 0), (2, 0)   # rhs monomials x and x^2

CASES = {
    # ---- solved: Prop 4.1, case (9,27)
    "reg_9_27": dict(
        cornersP=[(0, 0), (1, 1), (6, 16), (6, 18), (0, 18)],
        cornersQ=[(0, 0), (1, 0), (9, 24), (9, 27), (0, 27)],
        rhs=X),
    # ---- solved: Prop 4.2, case (9,24), subcases (1)-(3)
    "reg_9_24_c1": dict(
        cornersP=[(0, 0), (1, 1), (6, 16), (6, 18), (0, 12)],
        cornersQ=[(0, 0), (1, 0), (9, 24), (9, 27), (0, 18)],
        rhs=X),
    "reg_9_24_c2": dict(
        cornersP=[(0, 0), (1, 1), (6, 16), (6, 18), (0, 6)],
        cornersQ=[(0, 0), (1, 0), (9, 24), (9, 27), (0, 9)],
        rhs=X),
    "reg_9_24_c3": dict(
        cornersP=[(0, 0), (1, 1), (6, 16), (6, 18)],
        cornersQ=[(0, 0), (1, 0), (9, 24), (9, 27)],
        rhs=X),
    # ---- solved: Prop 4.4, case (7,21)
    "reg_7_21": dict(
        cornersP=[(0, 0), (4, 0), (6, 2), (0, 14)],
        cornersQ=[(0, 0), (6, 0), (9, 3), (0, 21)],
        rhs=X),
    # ---- OPEN: Prop 4.3, case (8,28)
    "open_8_28_c1": dict(
        cornersP=[(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)],
        cornersQ=[(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)],
        rhs=X2),
    "open_8_28_c2": dict(
        cornersP=[(0, 0), (1, 0), (8, 14), (8, 16)],
        cornersQ=[(0, 0), (2, 1), (12, 21), (12, 24)],
        rhs=X2),
}

PRIMES = [65521, 1048573]

def main():
    outdir = os.path.join(os.path.dirname(__file__), "..", "systems")
    for name, spec in CASES.items():
        for mode in ("nonorigin", "all"):
            tag = name if mode == "nonorigin" else name + "_strict"
            S = SystemA(tag, spec["cornersP"], spec["cornersQ"], spec["rhs"], nonvanish=mode)
            print(S.stats())
            for p in PRIMES:
                S.write_msolve(os.path.join(outdir, f"{tag}.p{p}.ms"), p)
            S.write_msolve(os.path.join(outdir, f"{tag}.q.ms"), 0)
            S.write_singular(os.path.join(outdir, f"{tag}.p{PRIMES[0]}.sing"), PRIMES[0])
            mapping = {S.varnames[i]: list(k) if k[1] is None else [k[0], list(k[1])]
                       for k, i in S.varof.items()}
            with open(os.path.join(outdir, f"{tag}.vars.json"), "w") as f:
                json.dump(mapping, f)

if __name__ == "__main__":
    main()

# ---------------- v2: torus-normalized systems ("_n" suffix) ----------------
FIX = {
    "reg_9_27":    [("P", (6, 18)), ("Q", (9, 27))],
    "reg_9_24_c1": [("P", (6, 18)), ("Q", (9, 27))],
    "reg_9_24_c2": [("P", (6, 18)), ("Q", (9, 27))],
    "reg_9_24_c3": [("P", (6, 18)), ("Q", (9, 27))],
    "reg_7_21":    [("P", (6, 2)),  ("Q", (9, 3))],
    "open_8_28_c1": [("P", (8, 16)), ("Q", (12, 24))],
    "open_8_28_c2": [("P", (8, 16)), ("Q", (12, 24))],
}

def emit_normalized():
    outdir = os.path.join(os.path.dirname(__file__), "..", "systems")
    for name, spec in CASES.items():
        k = spec["rhs"][0]
        (kp, (ip, jp)), (kq, (iq, jq)) = FIX[name]
        det = (ip - (k + 1) * jp) + (iq - (k + 1) * jq)
        assert det != 0, f"{name}: torus weight determinant vanishes"
        tag = name + "_n"
        S = SystemA(tag, spec["cornersP"], spec["cornersQ"], spec["rhs"],
                    nonvanish="nonorigin", fix_ones=FIX[name])
        print(S.stats(), f"[torus det {det}]")
        for p in PRIMES:
            S.write_msolve(os.path.join(outdir, f"{tag}.p{p}.ms"), p)
        S.write_msolve(os.path.join(outdir, f"{tag}.q.ms"), 0)
        S.write_singular(os.path.join(outdir, f"{tag}.p{PRIMES[0]}.sing"), PRIMES[0])

if __name__ == "__main__" and "--normalized" in sys.argv:
    emit_normalized()
