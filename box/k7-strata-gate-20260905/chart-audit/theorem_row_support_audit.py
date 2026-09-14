#!/usr/bin/env python3
"""List the K=7 MASTER-cutoff coefficient rows by exact bivariate support.

This avoids materialising their very large parameter-polynomial coefficients.
All arithmetic in ``specialise`` is over Z, so a nonzero specialised
coefficient proves that the corresponding universal coefficient is nonzero.

The support upper bounds used here follow from monic division in y:

* h has top H=y^6(y-x) and a complete lower triangle of degree <= 6;
* B has a complete lower triangle of degree <= b-1 and top y^4(y-x)Q;
* Al=quo_y(B^2,h) has y-degree <=5 and degree <=2b-7.  Its degree-(2b-7)
  band is B_b^2/H = 4*y^2*(y-x)*Q^2, hence is divisible by y^2 on q0 and
  by y^4 on q1; every other band has degree <=2b-8;
* Rh=B^2-Al*h has y-degree <=6 and degree <=2b-1 because its degree-2b
  band cancels.  The first remaining band is divisible by y^2 on q0 and
  y^4 on q1; every other band has degree <=2b-2.

The exact-Z specialisations witness every point allowed by those upper
bounds for Al and Rh.  Taking the Minkowski support union of the five terms
of E64-lam*f gives an upper bound for the dropped rows; exact-Z
specialisations witness every point of that union too.  Thus the emitted
row list is exact, not probabilistic.  Several seeds are used only to avoid
accidental zeros in an individual witness.
"""

from __future__ import annotations

from collections import defaultdict
import hashlib
import json
from pathlib import Path
from random import Random
import subprocess


HERE = Path(__file__).resolve().parent
Mon = tuple[int, int]
Poly = dict[Mon, int]


def add(a: Poly, b: Poly, scalar: int = 1) -> Poly:
    out: defaultdict[Mon, int] = defaultdict(int, a)
    for mon, coeff in b.items():
        out[mon] += scalar * coeff
    return {mon: coeff for mon, coeff in out.items() if coeff}


def scale(a: Poly, scalar: int) -> Poly:
    return {mon: scalar * coeff for mon, coeff in a.items() if scalar * coeff}


def mul(a: Poly, b: Poly) -> Poly:
    out: defaultdict[Mon, int] = defaultdict(int)
    for (i, j), ca in a.items():
        for (k, ell), cb in b.items():
            out[i + k, j + ell] += ca * cb
    return {mon: coeff for mon, coeff in out.items() if coeff}


def shift(a: Poly, di: int, dj: int) -> Poly:
    return {(i + di, j + dj): coeff for (i, j), coeff in a.items()}


def quoy_with_remainder(p: Poly, h: Poly, degree_y_h: int = 7) -> tuple[Poly, Poly]:
    """Exact monic division in y, matching charged QUOY."""
    p = dict(p)
    quotient: Poly = {}
    while p:
        degree_y_p = max(j for _i, j in p)
        if degree_y_p < degree_y_h:
            break
        leading = {(i, 0): c for (i, j), c in p.items() if j == degree_y_p}
        term = shift(leading, 0, degree_y_p - degree_y_h)
        quotient = add(quotient, term)
        p = add(p, mul(term, h), -1)
    return quotient, p


def minkowski(a: set[Mon], b: set[Mon]) -> set[Mon]:
    return {(i + k, j + ell) for i, j in a for k, ell in b}


def expected_component_supports(b: int, pin: int) -> tuple[set[Mon], ...]:
    h = {(0, 7), (1, 6)} | {
        (i, j) for j in range(6) for i in range(7 - j)
    }
    lower_b = {(i, j) for j in range(7) for i in range(b - j)}
    d = b - 5
    q = {(d - 1, 1)} | ({(d, 0)} if pin == 0 else set())
    b_support = lower_b | minkowski({(0, 5), (1, 4)}, q)

    threshold = 2 if pin == 0 else 4
    al: set[Mon] = set()
    for j in range(6):
        max_total = 2 * b - 7 if j >= threshold else 2 * b - 8
        al |= {(i, j) for i in range(max_total - j + 1)}
    rh: set[Mon] = set()
    for j in range(7):
        max_total = 2 * b - 1 if j >= threshold else 2 * b - 2
        rh |= {(i, j) for i in range(max_total - j + 1)}
    return h, b_support, al, rh


def specialise(b: int, pin: int, seed: int) -> tuple[Poly, Poly, Poly, Poly, int, Poly]:
    rng = Random(seed)

    def value() -> int:
        return rng.choice((-3, -2, -1, 1, 2, 3))

    h: Poly = {(0, 7): 1, (1, 6): -1}
    for j in range(7):
        for i in range(7 - j):
            if (i, j) != (0, 6):
                h[i, j] = value()

    beta: Poly = {
        (i, j): value() for j in range(7) for i in range(b - j)
    }
    d = b - 5
    q: Poly = {(d - 1, 1): value()}
    if pin == 0:
        q[d, 0] = value()
    btop = mul({(0, 5): 2, (1, 4): -2}, q)
    beta = add(beta, btop)

    b2 = mul(beta, beta)
    al, rh = quoy_with_remainder(b2, h)
    assert rh == add(b2, mul(al, h), -1)
    f = add(mul(h, h), beta)
    e64 = add(
        add(
            add(scale(mul(b2, beta), 8), scale(mul(mul(rh, h), h), -48)),
            scale(mul(beta, rh), -72),
        ),
        scale(mul(al, al), 9),
    )
    lam = value()
    elam = add(e64, scale(f, -lam))
    return h, beta, al, rh, lam, elam


def singular_crosscheck(h: Poly, beta: Poly, al: Poly, rh: Poly, lam: int, elam: Poly) -> set[Mon]:
    """Re-evaluate one exact-Z witness with Singular and return its row support."""

    def singular_poly(poly: Poly) -> str:
        return "+".join(
            f"({coeff})*x^{i}*y^{j}" for (i, j), coeff in sorted(poly.items())
        ) or "0"

    quoy = """proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }"""
    script = "\n".join(
        [
            "option(redSB); short=0;",
            "ring r=0,(x,y),dp;",
            f"poly h={singular_poly(h)};",
            f"poly B={singular_poly(beta)};",
            quoy,
            "poly Al=quoy(B^2,h,7);",
            "poly Rh=B^2-Al*h;",
            "poly f=h^2+B;",
            "poly E64=8*B^3-48*Rh*h^2-72*B*Rh+9*Al^2;",
            f"poly ELAM=E64-({lam})*f;",
            f'print("CHECK__AL "+string(Al==({singular_poly(al)})));',
            f'print("CHECK__RH "+string(Rh==({singular_poly(rh)})));',
            f'print("CHECK__E "+string(ELAM==({singular_poly(elam)})));',
            "matrix CE=coef(ELAM,x*y); int ii; intvec ex;",
            "for(ii=1;ii<=ncols(CE);ii++){ if(deg(CE[1,ii])>13){",
            '  ex=leadexp(CE[1,ii]); print("CHECK__ROW "+string(ex[1])+" "+string(ex[2]));',
            "} }",
            "quit;",
            "",
        ]
    )
    proc = subprocess.run(
        ["Singular", "--no-rc", "-q"],
        input=script,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "CHECK__AL 1" in proc.stdout
    assert "CHECK__RH 1" in proc.stdout
    assert "CHECK__E 1" in proc.stdout
    assert not proc.stderr
    return {
        tuple(map(int, line[len("CHECK__ROW ") :].split()))
        for line in proc.stdout.splitlines()
        if line.startswith("CHECK__ROW ")
    }


def bands(rows: set[Mon]) -> list[dict[str, int]]:
    result = []
    for degree in sorted({i + j for i, j in rows}):
        js = sorted(j for i, j in rows if i + j == degree)
        assert js == list(range(js[0], js[-1] + 1))
        result.append(
            {
                "degree": degree,
                "j_min": js[0],
                "j_max": js[-1],
                "count": len(js),
            }
        )
    return result


def main() -> None:
    records = []
    for b in range(9, 14):
        for pin in (0, 1):
            expected_h, expected_b, expected_al, expected_rh = expected_component_supports(b, pin)
            f_support = minkowski(expected_h, expected_h) | expected_b
            upper = (
                minkowski(minkowski(expected_b, expected_b), expected_b)
                | minkowski(minkowski(expected_rh, expected_h), expected_h)
                | minkowski(expected_b, expected_rh)
                | minkowski(expected_al, expected_al)
                | f_support
            )
            upper = {mon for mon in upper if sum(mon) > 13}

            seen_al: set[Mon] = set()
            seen_rh: set[Mon] = set()
            seen_rows: set[Mon] = set()
            witness: dict[Mon, int] = {}
            seeds = [10000 * b + 100 * pin + offset for offset in range(1, 11)]
            for seed in seeds:
                h, beta, al, rh, lam, elam = specialise(b, pin, seed)
                assert set(h) <= expected_h
                assert set(beta) <= expected_b
                assert set(al) <= expected_al
                assert set(rh) <= expected_rh
                singular_rows = singular_crosscheck(h, beta, al, rh, lam, elam)
                assert singular_rows == {
                    mon for mon, coeff in elam.items() if sum(mon) > 13 and coeff
                }
                seen_al |= set(al)
                seen_rh |= set(rh)
                for mon, coeff in elam.items():
                    if sum(mon) > 13 and coeff:
                        seen_rows.add(mon)
                        witness.setdefault(mon, seed)

            assert seen_al == expected_al
            assert seen_rh == expected_rh
            assert seen_rows == upper
            row_items = [
                {
                    "i": i,
                    "j": j,
                    "monomial": f"x^{i}*y^{j}",
                    "exact_Z_witness_seed": witness[i, j],
                }
                for i, j in sorted(upper, key=lambda mon: (sum(mon), mon[1], mon[0]))
            ]
            records.append(
                {
                    "K": 7,
                    "b": b,
                    "pin": pin,
                    "chart": f"q{pin}",
                    "row_definition": "coeff_(x^i*y^j)(E64-lam*f), i+j>13",
                    "raw_nonzero_coefficient_rows": len(upper),
                    "simplified_rows": len(upper),
                    "simplify_2_note": "initial/zero entries only; every listed coefficient is nonzero",
                    "bands": bands(upper),
                    "rows": row_items,
                    "witness_seeds": seeds,
                }
            )

    payload = {
        "method": "analytic monic-division support upper bound + exact-Z nonzero witness per row",
        "coefficient_polynomial": "E64-lam*f",
        "E64": "8*B^3-48*Rh*h^2-72*B*Rh+9*Al^2",
        "cutoff": 13,
        "all_support_upper_bounds_saturated_by_exact_Z_witnesses": True,
        "singular_exact_Z_crosschecks": 100,
        "charts": records,
    }
    output = HERE / "theorem-row-support.json"
    serialised = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output.write_text(serialised)

    table = ["b\tq\traw\tsimplified\tbands"]
    for record in records:
        compact = ";".join(
            f"{band['degree']}:{band['j_min']}..{band['j_max']}"
            for band in record["bands"]
        )
        table.append(
            f"{record['b']}\t{record['pin']}\t"
            f"{record['raw_nonzero_coefficient_rows']}\t"
            f"{record['simplified_rows']}\t{compact}"
        )
    table_payload = "\n".join(table) + "\n"
    (HERE / "theorem-row-support.tsv").write_text(table_payload)
    print(f"json_sha256={hashlib.sha256(serialised.encode()).hexdigest()}")
    print(table_payload, end="")


if __name__ == "__main__":
    main()
