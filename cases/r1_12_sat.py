"""r1_12_sat.py -- (1,2)-branch CORE-LEVEL saturated verdict objects
(SHEET6-R1.md sec 18 mandate 3b; SHEET6-R1-LADDER-REVIEW R2 mandates
1/2/5).  ADDITIVE new file; no prior emission touched.

The banked (1,2) verdict (sec 15) rests on a witness with s1 = 0; the
template forces the tie scale s1 nonzero (Prop 4.2 tower constant s_j;
review front 2, consequence 4).  This engine:

(i) e5port: exact-K3 check of the (1,2) E5-quartic PORT -- the
    relaxation-dropped pole->G_m h1-lead transport, run for the k1 = 1
    tower reading (SHEET6-R6 4.3): at G_m the (1,2) legality is
    h1+ = s1 (f+)^2, so p_h1,Gm = s1*S_M^2*P^4 (P = (e3-a1)(e3-a2),
    mult 4 at c_i); St 3.9(ii) merge-edge transport with the pole
    pattern lead -(3/4)s0 lam_i^3 w_i^4 (TEMPLATE 1b, branch-local)
    and lam_i = 9 S_M c_i^4 (a1-a2)^2 (TEMPLATE 2c-E5, f-side, branch-
    independent) gives
        -(3/4)*729*S_M^3*c_i^12*(a1-a2)^6*w_i^4
            = s1*S_M^2*(3 c_i^2)^4*(a1-a2)^4
        <=>  w_i^4 = -(4/27)*s1 / (S_M*c_i^4*(a1-a2)^2)
        <=>  81*S_M*a_i*alpha_i*W_i^4 + s1 = 0        (c_i = alpha_i,
             c_i^4 = a_i alpha_i, (a1-a2)^2 = 12, S_M = 7^12/2^6).
    METHOD VALIDATION: the same pipeline on the minimal branch (mult 2,
    p_h1,Gm = H_M eta P^2 (e3-b)) reproduces the 13.1 consistency
    identity: E-bracket sum_i (9+-5r3)(a_i-b)/a_i^2 == 0 EXACTLY.  The
    (1,2) E-bracket sum_i (9+-5r3)/a_i == 4 != 0: relation E (the
    banked UU-chart core residual, sec 15.1) and the (1,2)-E5 rows are
    JOINTLY inconsistent at ANY s1 != 0.

(ii) emit/run: saturated core-level verdict systems --
    r1_12sat.ms            = leaf12_UU.ms rows VERBATIM (char 0,
                             radicals as vars) + 2 E5-12 rows +
                             s1*t12 - 1
    r1_12sat_wfree_p*.ms   = leaf12_UU_wfree_p*.ms rows VERBATIM +
                             specialized E5-12 rows + s1*t12 - 1
    r1_12sat_ctl_p*.ms     = CONTROL: saturation without the tie rows
                             (s1 is FREE on the UU chart, so this must
                             stay NONEMPTY: the kill is the TIE, not
                             the chart or the saturation row).
    Soundness: sec-15.2 cover certificate -- EMPTY on the UU leaf ==
    intended-chart core emptiness; ZZ/ZU/UZ are off the intended locus
    (w_i units there).

Phases: e5port | emit | run | all
AUDIT: expanded integer monomials, no parens; p-rows in [0,p).
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_experiment as R1
import r1_fullcore as FC

SYS = FC.OUT_DIR
LVS = os.path.join(SYS, "leaves")
RUNS = os.path.join(os.path.dirname(HERE), "runs")
BASE = "r1_12sat"
C243 = 243 * 7 ** 12          # 3363432789843 -- the 15.1 content factor
C81 = 81 * 7 ** 12


def log(msg):
    print("[12sat %s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)


def e5port():
    """exact-K3 validation of the port (docstring (i))."""
    K3, mk, Fr = R1.K3, R1.mk, __import__("fractions").Fraction
    s3 = R1.SQ3
    a1, a2, b = R1.A1c, R1.A2c, R1.Bc
    SM = mk(Fr(7 ** 12, 2 ** 6))
    da2 = (a1 - a2) * (a1 - a2)
    assert (da2 - mk(12)).iszero()
    # minimal-branch method check: bracket sum (9+-5r3)(a_i-b)/a_i^2 == 0
    bmin = (mk(9) + mk(5) * s3) * (a1 - b) / (a1 * a1) + \
           (mk(9) - mk(5) * s3) * (a2 - b) / (a2 * a2)
    assert bmin.iszero(), "minimal-branch 13.1 bracket NOT reproduced"
    # (1,2) bracket sum (9+-5r3)/a_i == 4
    b12 = (mk(9) + mk(5) * s3) / a1 + (mk(9) - mk(5) * s3) / a2
    assert (b12 - mk(4)).iszero(), "(1,2) bracket != 4"
    # transport identity: -(3/4)*729*SM^3*c_i^12*da^6*w_i^4 =
    #   s1*SM^2*(3c_i^2)^4*da^4  with the row s1 = -81*SM*a_i*c_i*w_i^4
    # substituted (c_i^3 = a_i: c^12 = a^4, c^8*c = a^3):  both sides
    # carry SM^3*a_i^4*w_i^4; the residue is (3/4)*729*da2 == 81^2,
    # i.e. EXACTLY da2 = 12 -- the identity closes with no slack:
    assert (mk(Fr(3, 4)) * mk(729) * da2 - mk(6561)).iszero(), \
        "E5-12 transport identity fails"
    log("e5port PASS: minimal bracket == 0 (13.1 reproduced); (1,2) "
        "bracket == 4 != 0; row constant 81*S_M*a_i*alpha_i verified; "
        "content factor 243*7^12 = %d = the 15.1 row-87 content" % C243)


def read_ms(path):
    hdr, char, body = open(path).read().split("\n", 2)
    return ([h.strip() for h in hdr.split(",")], int(char),
            [e.strip() for e in body.strip().rstrip(",").split(",\n")])


def e5_12_rows_char0():
    """81*7^12*a_i*A_i*W_i^4 + 64*s1 = 0, a_i = 3+-r3, over Z."""
    return [
        ("E5-12 pole 1", "%d*A1*W1^4+%d*r3*A1*W1^4+64*s1" % (3 * C81, C81)),
        ("E5-12 pole 2", "%d*A2*W2^4-%d*r3*A2*W2^4+64*s1"
         % (3 * C81, C81)),
    ]


def e5_12_rows_modp(p):
    pt = FC.radical_point(p)
    out = []
    for i, (ai, Ai) in enumerate((((3 + pt["r3"]) % p, pt["A1"]),
                                  ((3 - pt["r3"]) % p, pt["A2"])), 1):
        c = C81 % p * ai % p * Ai % p
        out.append(("E5-12 pole %d" % i, "%d*W%d^4+64*s1" % (c, i)))
    return out


def phase_emit():
    # char 0
    hdr, char, eqs = read_ms(os.path.join(LVS, "leaf12_UU.ms"))
    assert char == 0 and len(eqs) == 14
    tie = e5_12_rows_char0()
    labels = [("leaf12_UU verbatim eq%d" % i, e) for i, e in
              enumerate(eqs)] + tie + [("SAT s1 (Rabinowitsch)",
                                        "s1*t12-1")]
    p0 = os.path.join(SYS, BASE + ".ms")
    with open(p0, "w") as f:
        f.write(", ".join(hdr + ["s1", "t12"]) + "\n0\n")
        f.write(",\n".join(e for _, e in labels) + "\n")
    with open(os.path.join(SYS, BASE + ".rows.txt"), "w") as f:
        f.write("# (1,2) CORE-LEVEL SATURATED verdict object (sec 18): "
                "leaf12_UU rows verbatim + E5-12 quartic port "
                "(81*S_M*a_i*alpha_i*W_i^4 + s1 = 0, cleared to Z) + "
                "s1*t12-1.\n# s1 = the (1,2) h2-tie scale (h1+ = "
                "s1(f+)^2), template-forced NONZERO.\n")
        for i, (lab, _) in enumerate(labels):
            f.write("eq%d = %s\n" % (i, lab))
    log("emitted %s (%d eqs, %d vars)" % (p0, len(labels), len(hdr) + 2))
    # wfree p-variants + relaxed controls
    for p in FC.good_primes(2):
        hw, cw, ew = read_ms(os.path.join(LVS,
                                          "leaf12_UU_wfree_p%d.ms" % p))
        assert cw == p and len(ew) == 9
        tiep = e5_12_rows_modp(p)
        for tag, extra in (("", tiep), ("_ctl", [])):
            rows = [e for e in ew] + [e for _, e in extra] + \
                   ["s1*t12+%d" % (p - 1)]
            path = os.path.join(SYS, "%s%s_p%d.ms" % (BASE, tag, p))
            with open(path, "w") as f:
                f.write(", ".join(hw + ["s1", "t12"]) + "\n%d\n" % p)
                f.write(",\n".join(rows) + "\n")
            log("emitted %s (%d eqs, %d vars)%s"
                % (path, len(rows), len(hw) + 2,
                   "  [CONTROL: no tie rows -- must stay NONEMPTY]"
                   if tag else ""))
    for fn in os.listdir(SYS):
        if fn.startswith(BASE) and fn.endswith(".ms"):
            t = open(os.path.join(SYS, fn)).read()
            assert "(" not in t and ")" not in t, fn


def phase_run(timeout=1200):
    import r1_decompose as RD
    logf = os.path.join(RUNS, BASE + "_runs.log")
    files = [BASE + ".ms"] + \
        ["%s%s_p%d.ms" % (BASE, tag, p) for p in FC.good_primes(2)
         for tag in ("", "_ctl")]
    for fn in files:
        out = os.path.join(RUNS, fn + ".out")
        verdict, wall, rss = RD.run_msolve_rss(
            os.path.join(SYS, fn), out, timeout, threads=4)
        line = "%s: %s wall %.1fs rss %.1f MB" % (fn, verdict, wall,
                                                  rss / 1024.0)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


def phase_minsat(timeout=1200):
    """MINIMAL-branch core-level saturated object (ledger symmetry):
    leaf_UU rows verbatim + minimal E5 quartic (HM restored; the
    review-verified TEMPLATE 2c-E5 rows, cleared to Z) + HM*tH-1.
    EXPECTED NONEMPTY (the 13.1 consistency identity: bracket == 0):
    the minimal branch SURVIVES core-level saturation; its kill is at
    depth 84 (r1_q0_sat/r1_q0_fam)."""
    import r1_decompose as RD
    b = "r1_minsat"
    cW = 729 * 7 ** 36 * 144            # * a_i^2 * A_i * W_i^4
    ties = [("E5-min pole 1", "%d*A1*W1^4+%d*r3*A1*W1^4-1048576*HM"
             "+1048576*r3*HM" % (12 * cW, 6 * cW)),
            ("E5-min pole 2", "%d*A2*W2^4-%d*r3*A2*W2^4-1048576*HM"
             "-1048576*r3*HM" % (12 * cW, 6 * cW))]
    hdr, char, eqs = read_ms(os.path.join(LVS, "leaf_UU.ms"))
    assert char == 0 and len(eqs) == 14
    rows = eqs + [e for _, e in ties] + ["HM*tH-1"]
    path = os.path.join(SYS, b + ".ms")
    with open(path, "w") as f:
        f.write(", ".join(hdr + ["HM", "tH"]) + "\n0\n")
        f.write(",\n".join(rows) + "\n")
    t = open(path).read()
    assert "(" not in t and ")" not in t
    log("emitted %s (%d eqs, %d vars)" % (path, len(rows), len(hdr) + 2))
    out = os.path.join(RUNS, b + ".ms.out")
    verdict, wall, rss = RD.run_msolve_rss(path, out, timeout, threads=4)
    line = "%s.ms (char 0): %s wall %.1fs" % (b, verdict, wall)
    log(line)
    with open(os.path.join(RUNS, b + "_runs.log"), "a") as f:
        f.write(line + "\n")


def phase_corr(timeout=1200):
    """CORRECTED (1,2) verdict object (SHEET6-R1-Q2E5.md review: the
    e5port rows are RETRACTED -- level slip).  The count-exact St 3.9
    pole-edge transport for (1,2) is the FIRST DEAD MEMBER h2 = h1 -
    s1 f^2 (p_h2,Gm = H12 eta P^2(eta^3-b), mult 2 = deg p_h2,P, lands
    6/42 EXACT; the port's mult-4 h1 rows land at 4/42 = the s1(f+)^2
    level, an R1-series tier condition per SHEET6-R6 4.3).  Corrected
    rows = minimal-shape E5 with H12 restored + H12*tH12-1 + s1*t12-1
    (s1 absent from every row: core saturation of s1 is VACUOUS).
    EXPECTED NONEMPTY (13.1 bracket == 0), mirroring r1_minsat."""
    import r1_decompose as RD
    b = BASE + "_corr"
    cW = 729 * 7 ** 36 * 144            # * a_i^2 * A_i * W_i^4 (x 2^18)
    ties = [("E5-12corr pole 1 (h2-transport, H12)",
             "%d*A1*W1^4+%d*r3*A1*W1^4-1048576*H12+1048576*r3*H12"
             % (12 * cW, 6 * cW)),
            ("E5-12corr pole 2 (h2-transport, H12)",
             "%d*A2*W2^4-%d*r3*A2*W2^4-1048576*H12-1048576*r3*H12"
             % (12 * cW, 6 * cW))]
    hdr, char, eqs = read_ms(os.path.join(LVS, "leaf12_UU.ms"))
    assert char == 0 and len(eqs) == 14
    labels = [("leaf12_UU verbatim eq%d" % i, e) for i, e in
              enumerate(eqs)] + ties + \
             [("SAT H12 (Rabinowitsch)", "H12*tH12-1"),
              ("SAT s1 (vacuous at core: s1 in NO row)", "s1*t12-1")]
    path = os.path.join(SYS, b + ".ms")
    with open(path, "w") as f:
        f.write(", ".join(hdr + ["H12", "tH12", "s1", "t12"]) + "\n0\n")
        f.write(",\n".join(e for _, e in labels) + "\n")
    t = open(path).read()
    assert "(" not in t and ")" not in t
    with open(os.path.join(SYS, b + ".rows.txt"), "w") as f:
        f.write("# (1,2) CORRECTED core-saturated object (Q2E5 review):"
                " leaf12_UU verbatim + h2-transport E5 rows (H12 = the"
                " (1,2) h2-stage G_m lead, template-forced nonzero) +\n"
                "# H12/s1 saturation.  SUPERSEDES r1_12sat.ms (e5port "
                "rows retracted: mult-4 h1 transport lands at 4/42, "
                "not the 6/42 pole top -- level slip).\n")
        for i, (lab, _) in enumerate(labels):
            f.write("eq%d = %s\n" % (i, lab))
    log("emitted %s (%d eqs, %d vars)" % (path, len(labels),
                                          len(hdr) + 4))
    logf = os.path.join(RUNS, b + "_runs.log")
    out = os.path.join(RUNS, b + ".ms.out")
    verdict, wall, rss = RD.run_msolve_rss(path, out, timeout, threads=4)
    line = "%s.ms (char 0): %s wall %.1fs" % (b, verdict, wall)
    log(line)
    with open(logf, "a") as f:
        f.write(line + "\n")
    # p-variants on the wfree leaves (banked radical point, W symbolic)
    for p in FC.good_primes(2):
        pt = FC.radical_point(p)
        hw, cw, ew = read_ms(os.path.join(LVS,
                                          "leaf12_UU_wfree_p%d.ms" % p))
        assert cw == p and len(ew) == 9
        rows = list(ew)
        for i, (ai, Ai) in enumerate((((3 + pt["r3"]) % p, pt["A1"]),
                                      ((3 - pt["r3"]) % p, pt["A2"])), 1):
            c = cW % p * (ai * ai % p) % p * Ai % p
            d = 4 * ((ai - 4) % p) % p * pow(2, 18, p) % p
            rows.append("%d*W%d^4+%d*H12" % (c, i, d))
        rows += ["H12*tH12+%d" % (p - 1), "s1*t12+%d" % (p - 1)]
        pp = os.path.join(SYS, "%s_p%d.ms" % (b, p))
        with open(pp, "w") as f:
            f.write(", ".join(hw + ["H12", "tH12", "s1", "t12"])
                    + "\n%d\n" % p)
            f.write(",\n".join(rows) + "\n")
        t = open(pp).read()
        assert "(" not in t and ")" not in t
        out = os.path.join(RUNS, "%s_p%d.ms.out" % (b, p))
        verdict, wall, rss = RD.run_msolve_rss(pp, out, timeout,
                                               threads=4)
        line = "%s_p%d.ms: %s wall %.1fs" % (b, p, verdict, wall)
        log(line)
        with open(logf, "a") as f:
            f.write(line + "\n")


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    if ph in ("e5port", "all"):
        e5port()
    if ph in ("emit", "all"):
        phase_emit()
    if ph in ("run", "all"):
        phase_run()
    if ph == "minsat":
        phase_minsat()
    if ph == "corr":
        phase_corr()
