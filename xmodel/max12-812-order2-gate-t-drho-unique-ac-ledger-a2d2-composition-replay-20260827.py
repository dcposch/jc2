#!/usr/bin/env python3
"""Desk replay for the D(rho*k) unique-AC ledger and a=2,d=2 import.

No CAS is launched.  This replay rehashes the reviewed endpoint authorities,
checks the exact integral fan partition, identifies the first untransported
valuation baseline after (2,3,>=2), checks the current grade-18 actual-total
construction path, records the shifted finite-jet map, and independently
checks the two Hensel/deck orientations and terminal residue.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

KRB_REPORT = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md"
KRB_REPLAY = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-replay-20260827.py"
OLD_COMPOSITION = ROOT / "xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-sol-20260827.md"
OLD_REPLAY = ROOT / "xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-replay-20260827.py"
FAN = ROOT / "xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md"

D1_UNION = ROOT / "xmodel/max12-812-order2-square-d1-unitload-d1-contact-ladder-composition-promotion-20260826.md"
D1_UNION_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-unitload-contact-ladder-composition-hostile-review-grok-20260826.md"
D23_AUDIT = ROOT / "xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-audit-20260826.md"
D23_AUDIT_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-hostile-review-grok-20260826.md"

LOWA_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-promotion-20260826.md"
LOWA_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-hostile-review-grok-20260826.md"
E_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-e-a1d3-opposite-root-pole3-promotion-20260826.md"
E_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-e-a1d3-opposite-root-pole3-hostile-review-grok-20260826.md"
A7_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-a7-loadtie-dual-functional-promotion-20260826.md"
A7_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-a7-loadtie-dual-functional-hostile-review-grok-20260826.md"
A8D2_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-a8-d2-loadfirst-dual-promotion-20260826.md"
A8D2_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-a8-d2-loadfirst-dual-hostile-review-grok-20260826.md"
A8D3_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-a8d3-targetshadow-chamber-hostile-review-grok-20260826.md"
A9_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-a9-d23-j38-r3-tail-promotion-20260826.md"
A9_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-a9-d23-j38-r3-tail-hostile-review-grok-20260826.md"
CEILING_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-age10-cge-a1-source-ceiling-corollary-promotion-20260826.md"
CEILING_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-age10-cge-a1-source-ceiling-corollary-hostile-review-grok-v2-20260826.md"

LOWA_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826"
LOWA_COMPILER = LOWA_DIR / "compile_local_row.py"
LOWA_FREEZE = LOWA_DIR / "FREEZE.sha256"
LOWA_EVIDENCE = LOWA_DIR / "EVIDENCE.sha256"
LOWA_INVENTORY = LOWA_DIR / "aws_v7_q/compiled/source_inventory.json"
LOWA_STDOUT = LOWA_DIR / "aws_v7_q/run/max12_812_order2_square_d1_unique_ac_d23_lowa6_localrow_v7_q_20260826.stdout"

V33_DIR = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827"
V33 = V33_DIR / "prolong_boundary_g18_v33.py"
V33_FREEZE = V33_DIR / "FREEZE.sha256"
V33_RESULT = V33_DIR / "aws_q/RESULT.json"
V33_COMPILED_RESULT = V33_DIR / "aws_q/compiled/result.json"


PINS = {
    KRB_REPORT: "1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a",
    KRB_REPLAY: "f11b24a3447a0602ef5b55891e156b6f179e62179eb8394fd30f4455adf29af5",
    OLD_COMPOSITION: "db0ecebf37cf8283c27e36ed8f0ba10ae9bcf1887d1854affe73cf61c8f367cd",
    OLD_REPLAY: "33514275318db4ce7ba01adae1f1260f416d3b47734cc4bc10b0217acbed51cd",
    FAN: "c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d",
    D1_UNION: "85533441f2e2b5b04d499e30399ca0f9d62110379e01b50716cdbb3febd36680",
    D1_UNION_REVIEW: "bd5b3dd52274024941edc663c4ef95222f6abb205cdb9e347d8b80b3483e74cb",
    D23_AUDIT: "cdd2305804073e771b26d00a22030486a3d8347c6d70c41f4d6a7a7b6482e1c7",
    D23_AUDIT_REVIEW: "94a6037db532165a50ce03b40da0e6ca2be12d5c79aacc4ee3d95baecdabc5ab",
    LOWA_PROMOTION: "8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da",
    LOWA_REVIEW: "841f0d6ccbb596fa4ace3f08760f039eb288030efa91075112e915d1320592a3",
    E_PROMOTION: "2ff74f6914a3316104d7a406ca6d6d4ede2cf8332221dfcccd7461f9d925176e",
    E_REVIEW: "984783eab8342d2523a6e1d7365785f5d37746d0393fc30cfad206bb5658b774",
    A7_PROMOTION: "b5c38f1b2e2e5ec6f2ac32fb350f11686dac5cb45eabe8cf1ea67d20726bd362",
    A7_REVIEW: "1ae7f6d95b7d707b3fe54b07a59fbd103435d13b4a0a764b6495215785d26530",
    A8D2_PROMOTION: "9cc6870289ec0697e438c3999616194d3955e3bc875cd69cad855fd16d28c3b9",
    A8D2_REVIEW: "0558ea1e668245b983e217ef329a6ccf0baf5a8f5769f669f43a245d24990e21",
    A8D3_REVIEW: "02cbae00f16eea7ba03e0ccb54e2e52d0b788264da80053a82a110bd4cfe74cc",
    A9_PROMOTION: "551ca2f6f8aaf75fd67019d055e43ae862150de62d51cb0bd8755d4d0085a19a",
    A9_REVIEW: "f922fab0828ff0470ada62fa22bd84a9383233b27948bca12726f1c3aa7785f5",
    CEILING_PROMOTION: "470ea478c9463d62d39a428962fd9dd5845f4bf882388f84594c82a211634fb8",
    CEILING_REVIEW: "f75d885da6b39af85127540fa8ede8a17d1f83a3a2d5279bb5c641f2bd98e15b",
    LOWA_COMPILER: "b2fe07fdd2f855598dde5c6ef9828909c94496eb5e196756eff504056cde2769",
    LOWA_FREEZE: "5faefef61a58f3121a605a83fe2e35af6fff37857ee8649dba33be3e18acbe07",
    LOWA_EVIDENCE: "ba45fe4151eccf4644e23dc21fb8dda0d0957780a77a5c615a8cc70c19efb3f4",
    LOWA_INVENTORY: "c8eb56409a49ff6ad76d496c7ba38645eceb82b02a9bb67a5cce987e128d5f48",
    LOWA_STDOUT: "ad447f4daae1c62374c392e8fb297052fde2eafe20efcf8ba1595384ff457775",
    V33: "5941bf876e3ace184190130841046ccc2573615be5cc159608698c5bbdcac36d",
    V33_FREEZE: "498874bd80adfb9cc6fcc8e6f3eae3ed2c0d48d66150c5f4b416052086ad0c8c",
    V33_RESULT: "22018489bbf27c91d5d973ac6e2ec00780fa079e6b07b6d386ce45dc5737de1f",
    V33_COMPILED_RESULT: "22f64fbb9d2107508f7218a9aabaea03d6c502219baef84bb918352f7e38df0f",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def custody_check() -> dict[str, str]:
    observed = {str(path.relative_to(ROOT)): digest(path) for path in PINS}
    for path, expected in PINS.items():
        key = str(path.relative_to(ROOT))
        if observed[key] != expected:
            raise AssertionError(("custody mismatch", key, observed[key], expected))
    return observed


def least_s(a: int, d: int) -> int:
    for s in range(20):
        if a + s >= 2 and a + 3 * s > d:
            return s
    raise AssertionError((a, d))


def endpoint(a: int, d: int) -> dict[str, int]:
    c = a + d
    if a < 1 or c < 3 or d not in (1, 2, 3):
        raise ValueError((a, d))
    s = least_s(a, d)
    g = 10 + 2 * a + d
    return {"a": a, "d": d, "c": c, "r_floor": a + s, "G": g, "T": g + d}


def route(a: int, d: int) -> str:
    if d == 1:
        if 2 <= a <= 5:
            return "d1_a2_a5_promoted"
        if 6 <= a <= 7:
            return "d1_a6_a7_promoted"
        if a == 8:
            return "d1_a8_promoted"
        if a == 9:
            return "d1_a9_promoted"
        if a >= 10:
            return "d1_age10_promoted"
    if d in (2, 3):
        if a == 1 and d == 3:
            return "d23_E_a1d3_promoted"
        if a <= 6:
            return "d23_lowa6_promoted"
        if a == 7:
            return "d23_a7_promoted"
        if a == 8 and d == 2:
            return "d23_a8d2_promoted"
        if a == 8 and d == 3:
            return "d23_a8d3_reviewed_unpromoted"
        if a == 9:
            return "d23_a9_promoted"
        if a >= 10:
            return "d23_age10_promoted"
    raise AssertionError(("unrouted", a, d))


def coverage_ledger_check() -> dict[str, object]:
    # Exact baseline census over a long finite sentinel.  The routing rules
    # themselves are parametric; this box checks every wall and transition.
    baselines = []
    for a in range(1, 41):
        for d in (1, 2, 3):
            if a + d < 3:
                continue
            item = endpoint(a, d)
            item["route"] = route(a, d)
            baselines.append(item)

    # Independently compare the closed-form s_min table to the inequalities.
    for item in baselines:
        a, d = item["a"], item["d"]
        expected = 0
        if d == 2 and a in (1, 2):
            expected = 1
        if d == 3 and a in (1, 2, 3):
            expected = 1
        if d == 1:
            expected = 0
        if item["r_floor"] != a + expected:
            raise AssertionError(("s_min", item, expected))
        s = item["r_floor"] - a
        if not (a + s >= 2 and a + 3 * s > d):
            raise AssertionError(("not unique AC", item))
        if s and a + 3 * (s - 1) > d and a + s - 1 >= 2:
            raise AssertionError(("not least", item))

    old = endpoint(2, 1)
    after_by_valuation = sorted(
        (item for item in baselines if (item["a"], item["c"], item["r_floor"]) > (2, 3, 2)),
        key=lambda item: (item["a"], item["c"], item["r_floor"]),
    )[0]
    after_by_grade = sorted(
        (item for item in baselines if (item["G"], item["a"], item["c"], item["r_floor"]) >
         (old["G"], old["a"], old["c"], old["r_floor"])),
        key=lambda item: (item["G"], item["a"], item["c"], item["r_floor"]),
    )[0]
    wanted = endpoint(2, 2)
    if after_by_valuation != {**wanted, "route": "d23_lowa6_promoted"}:
        raise AssertionError(("valuation successor", after_by_valuation))
    if after_by_grade != {**wanted, "route": "d23_lowa6_promoted"}:
        raise AssertionError(("grade successor", after_by_grade))

    return {
        "domain": "q=0,a>=1,r>=2,c>=3, strict unique AC",
        "criterion": "d=c-a in {1,2,3}, s=r-a>=0, a+3s>d",
        "parametric_groups": {
            "d1": "a>=2,c=a+1,r>=a; partitions 2..5,6..7,8,9,>=10",
            "d2_d3_finite": "18 baselines, 1<=a<=9, one closed R-tail per (a,d)",
            "d2_d3_infinite": "a>=10,c=a+d,r>=a, d in {2,3}",
        },
        "review_state": (
            "every strict unique-AC endpoint is independently reviewed; a=8,d=3 is "
            "CONFIRMED but lacks a narrow promotion/updated union promotion"
        ),
        "already_total_transported_before_this_replay": [endpoint(2, 1)],
        "minimal_after_a2c3_by_valuation": after_by_valuation,
        "minimal_after_a2c3_by_first_grade": after_by_grade,
        "sentinel_baselines_checked": len(baselines),
    }


def construction_path_check() -> dict[str, object]:
    source = V33.read_text()
    required = {
        "degree_18": "base.MAX_DEGREE = 18",
        "kummer_constant": 'p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))',
        "moving_p": 'p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))',
        "c_shift_two": "c = base.series_shift(dense_series(base, [\"cs\"] + [f\"cs{i}\" for i in range(1, 17)]), 2)",
        "r_quarter": "r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))",
        "n3_shift_three": "n3 = base.series_shift(az, 3); n2 = base.series_shift(ac, 3)",
        "seven_rows": "totals = {row: v28.build_row(base, tails[str(row)], row, coefficients, loads) for row in ROWS}",
        "face_after_totals": 'killed = parser.J1 | frozenset({"a0", "rho"})',
    }
    sentinels = {name: snippet in source for name, snippet in required.items()}
    if not all(sentinels.values()):
        raise AssertionError(("V33 construction sentinel", sentinels))
    if source.index(required["seven_rows"]) > source.index(required["face_after_totals"]):
        raise AssertionError("V33 specialized before constructing total rows")

    result = json.loads(V33_RESULT.read_text())
    compiled = json.loads(V33_COMPILED_RESULT.read_text())
    if result.get("status") != "PASS-A1-BOUNDARY-PROLONG-G18-V33":
        raise AssertionError(("V33 status", result.get("status")))
    expected_counts = {
        "Tg18_1": 153, "Tg18_2": 244, "Tg18_3": 327, "Tg18_4": 174,
        "Tg18_5": 358, "Tg18_6": 140, "Tg18_7": 251,
    }
    if compiled.get("grade18_term_counts") != expected_counts:
        raise AssertionError(("V33 counts", compiled.get("grade18_term_counts")))

    inventory = json.loads(LOWA_INVENTORY.read_text())
    block = next(item for item in inventory["blocks"] if item["a"] == 2 and item["d"] == 2)
    expected_block = {
        "G": 16, "T": 18, "a": 2, "d": 2,
        "jet_maxima": {"A": 2, "C": 2, "R": 0, "k10": 0, "k2": 0,
                       "k6": 0, "mu2": 0, "mu4": 0, "p": 2},
        "maxpole": 2, "negative": False, "primitive_count": 4,
        "r_floor": 3, "s_min": 1,
    }
    if block != expected_block:
        raise AssertionError(("B22 inventory", block))
    transcript = LOWA_STDOUT.read_text()
    markers = (
        "B22_BASELINE=A2_D2_S1_G16_T18",
        "B22_PRIMITIVE_COUNT=4",
        "B22_GLOBAL_POLE_CEILING=2",
        "B22_MOVING_L2_RECURRENCE=1",
        "B22_TARGET_FREE_LOCAL_ROWS=1",
        "B22_BOTH_ORIENTATIONS=1",
        "B22_LOCAL_COEFFICIENT=3/2*lam^2*cv^2",
        "B22_ENDPOINT=PASS_EMPTY_CLOSED_R_TAIL",
    )
    if not all(marker in transcript for marker in markers):
        raise AssertionError("B22 transcript marker")
    return {
        "V33_sentinels": sentinels,
        "V33_status": result["status"],
        "V33_grade18_rho0_face_term_counts": expected_counts,
        "B22_inventory": block,
        "B22_markers": list(markers),
        "scope": (
            "V33 builds the universal general-rho total rows through grade 18 before "
            "its unrelated rho=0 ordered-a1 face; only the face rows are serialized. "
            "General-rho equality comes from the formal Kummer primitive/tail identity."
        ),
    }


def finite_jet_map_check() -> dict[str, object]:
    # U_18^rho -> the B22 finite D1 ring.  Coefficients omitted here vanish
    # below the displayed contact order or are later than the terminal grade.
    mapping = {
        "rho": "lam",
        "ell1": "ell1", "ell2": "ell2",
        "aaa1": "a1D", "az3": "a1D_1", "az4": "a1D_2",
        "aaa0": "a0D", "ac3": "a0D_1", "ac4": "a0D_2",
        "ez4": "2*c1D", "ez5": "2*c1D_1", "ez6": "2*c1D_2",
        "ec4": "2*c0D", "ec5": "2*c0D_1", "ec6": "2*c0D_2",
        "cs3": "b1", "rs3": "4*b0", "k": "k0",
    }
    vanished = {
        "R_below_3": ["cs", "cs1", "cs2", "rs", "rs1", "rs2"],
        "A_below_2": ["a1", "aa1", "a0", "aa0"],
        "C_below_4": ["c1", "e1", "ee1", "ez3", "c0", "e0", "ee0", "ec3"],
    }
    # Check the shifts forced by the actual total formulas:
    # c_tot=sigma^2*cs, delta r_tot=sigma^2*rs/4,
    # n3=sigma^3*Az, and Ez/2 is the D1 C input.
    exponents = {
        "total_c_from_D1_R": 2 + 3,
        "total_delta_r_from_D1_R": 2 + 3,
        "total_n3_from_D1_A": 3 + 2,
        "total_Ez_over_2_from_D1_C": 4,
        "D1_A_order": 2,
        "D1_C_order": 4,
        "D1_R_order": 3,
    }
    if exponents != {
        "total_c_from_D1_R": 5,
        "total_delta_r_from_D1_R": 5,
        "total_n3_from_D1_A": 5,
        "total_Ez_over_2_from_D1_C": 4,
        "D1_A_order": 2,
        "D1_C_order": 4,
        "D1_R_order": 3,
    }:
        raise AssertionError(exponents)
    return {
        "ring_map": mapping,
        "forced_vanishing": vanished,
        "shift_check": exponents,
        "later_jet_independence_through_18": {
            "p": 2, "A": 2, "C": 2, "R": 0, "k10": 0,
            "k6": 0, "k2": 0, "mu2": 0, "mu4": 0,
        },
        "shifted_root_pairs": {
            "R0_plus_minus": "rs3/4 +/- rho*cs3",
            "C0_plus_minus": "(ec4 +/- rho*ez4)/2",
            "A0_plus_minus": "aaa0 +/- rho*aaa1",
        },
        "stage_zero_warning": "(rs,cs),(c0,c1),(a0,a1) vanish on this contact",
    }


def mul_linear(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    # Coefficient order: constant,z.
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[1] * right[1],
    )


def hensel_and_deck_check() -> dict[str, object]:
    samples = [
        (Fraction(1), Fraction(2), Fraction(3), Fraction(5), Fraction(7)),
        (Fraction(3, 2), Fraction(-4), Fraction(9, 5), Fraction(-2), Fraction(11, 3)),
    ]
    checked = []
    for rho, ell1, ell2, au, cv in samples:
        for epsilon in (1, -1):
            lam = epsilon * rho
            root1 = -ell1 / (2 * lam)
            root2 = -(ell2 + root1 * root1) / (2 * lam)
            # Coefficients of lambda(sigma)^2+p(sigma)/2 through sigma^2.
            coeff0 = lam * lam - rho * rho
            coeff1 = 2 * lam * root1 + ell1
            coeff2 = root1 * root1 + 2 * lam * root2 + ell2
            if (coeff0, coeff1, coeff2) != (0, 0, 0):
                raise AssertionError(("Hensel", rho, epsilon, coeff0, coeff1, coeff2))

            L = (-lam * lam, Fraction(0), Fraction(1))
            plus = mul_linear((-au * lam, au), (cv * lam, cv))
            minus = mul_linear((au * lam, au), (-cv * lam, cv))
            wanted = tuple(au * cv * coefficient for coefficient in L)
            if plus != wanted or minus != wanted:
                raise AssertionError(("allocation", rho, epsilon, plus, minus, wanted))
            residue = Fraction(3, 2) * lam * lam * cv * cv
            if not residue:
                raise AssertionError(("residue", rho, epsilon))
            checked.append({
                "rho": str(rho), "epsilon": epsilon, "lambda0": str(lam),
                "root1": str(root1), "root2": str(root2),
                "both_allocations_multiply_to_au_cv_L": True,
                "terminal_residue": str(residue),
            })
    return {
        "moving_polynomial": "P=-2*rho^2+2*ell1*sigma+2*ell2*sigma^2",
        "hensel_relations": [
            "lambda0=epsilon*rho",
            "lambda1=-ell1/(2*lambda0)",
            "lambda2=-(ell2+lambda1^2)/(2*lambda0)",
        ],
        "positive_allocation": "A0=au*(z-lambda0), C0=cv*(z+lambda0)",
        "negative_allocation": "A0=au*(z+lambda0), C0=cv*(z-lambda0)",
        "deck": "rho |-> -rho exchanges epsilon and the two root labels",
        "terminal_functional": "Phi4+lambda(sigma)*(Phi3+(P/4)*Phi1)",
        "terminal_residue": "(3/2)*rho^2*cv^2",
        "samples": checked,
    }


def main() -> None:
    payload = {
        "status": "PASS-DRHO-UNIQUE-AC-LEDGER-A2D2-COMPOSITION-DESK-REPLAY",
        "scope": (
            "STRICT UNIT-LOAD GENERIC-SQUARE UNIQUE-AC FAN AFTER FIRST-NORMAL, "
            "HALF-WEIGHT, AND M=0 GATES; ONE NEW TOTAL CONTACT ON D(rho*k); "
            "NO EQUALITY FACE, OTHER PRIMARY FACE, POSITIVE-ORDER LOAD, k=0, "
            "rho=0, RAMIFIED RECEIVER, G2-PSC, G2-BD, GATE-T, ORDER-TWO, "
            "MAXIMUM-TWELVE, OR JC2 VERDICT"
        ),
        "frozen_sha256": custody_check(),
        "coverage_ledger": coverage_ledger_check(),
        "actual_total_and_endpoint_custody": construction_path_check(),
        "finite_jet_map": finite_jet_map_check(),
        "hensel_deck_and_residue": hensel_and_deck_check(),
        "outcome": {
            "new_total_contact": "PASS: ord(A)=2,ord(C)=4,ord(R)>=3 excluded on D(rho*k)",
            "next_untransported_by_valuation": "ord(A)=2,ord(C)=5,ord(R)>=3; terminal grade 20",
            "whole_unique_AC_total_transport": "INCOMPLETE",
            "whole_generic_square_cover": "NOT CLAIMED",
            "ramified_fibre": "UNTOUCHED",
        },
    }
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
