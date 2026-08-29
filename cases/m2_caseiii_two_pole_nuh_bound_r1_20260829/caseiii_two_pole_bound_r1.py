#!/usr/bin/env python3
"""Exact incoming-index bound for a two-pole case-III merge.

At the merge, one nonzero edge has multiplicity ``mu`` and invariant ``w``;
the zero-direction edge has multiplicity ``mu0``, invariant ``w0``, and
incoming index ``h``.  The merge-local index is ``nu``.  Its pattern is

    dp = mu0 + nu*(mu + sum(m_j)),
    dq = 1 + nu*(1 + k + lex).

Every nonchain multiplicity obeys ``m_j*dq < dp < mu*dq``.  The two
case-II/III handshakes then give a cap-free finite bound on ``h``.  This file
derives certificates; it does not enumerate full merge configurations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from typing import Iterable


SCHEMA = "m2-caseiii-two-pole-incoming-index-bound-r1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def strict_integer_upper(value: Fraction) -> int:
    """Largest integer h with h < value."""
    return ceil_fraction(value) - 1


def fraction_text(value: Fraction) -> str:
    return (str(value.numerator) if value.denominator == 1 else
            f"{value.numerator}/{value.denominator}")


def incoming_index_certificate(mu: int, w: Fraction,
                               mu0: int, w0: Fraction) -> dict[str, object]:
    """Return the exact finite incoming-h conclusion for all three regimes."""
    require(isinstance(mu, int) and mu >= 1, "mu must be a positive integer")
    require(isinstance(mu0, int) and mu0 >= 1,
            "mu0 must be a positive integer")
    require(isinstance(w, Fraction) and w > 0, "w must be positive")
    require(isinstance(w0, Fraction) and w0 > 0, "w0 must be positive")

    if mu0 < mu:
        strict = Fraction(mu, mu0) * w / w0
        bound = strict_integer_upper(strict)
        return {
            "regime": "mu0<mu",
            "strict_upper": fraction_text(strict),
            "max_integer_h": max(0, bound),
            "reason": "positive kbar forces mu0*h*w0 < mu*w",
        }

    if mu0 == mu:
        forced = w / w0
        legal = forced.denominator == 1 and forced >= 1
        return {
            "regime": "mu0=mu",
            "forced_h": fraction_text(forced),
            "legal_integer_h": int(forced) if legal else None,
            "max_integer_h": int(forced) if legal else 0,
            "reason": "equal-multiplicity handshakes force h*w0=w",
        }

    delta = mu0 - mu
    kbar_bound = mu * w * (2 * delta + 3)
    h_bound_rational = (delta * kbar_bound + mu * w) / (mu0 * w0)
    return {
        "regime": "mu0>mu",
        "delta": delta,
        "kbar_upper": fraction_text(kbar_bound),
        "h_upper": fraction_text(h_bound_rational),
        "max_integer_h": max(0, floor_fraction(h_bound_rational)),
        "reason": (
            "D=mu*dq-dp>0 and pattern NE give dq/D<=2*delta+3; "
            "then kbar=mu*w*dq/D and "
            "mu0*h*w0=delta*kbar+mu*w"
        ),
    }


def pattern_certificate(mu: int, mu0: int, nu: int, k: int, lex: int,
                        multiplicities: tuple[int, ...], w: Fraction,
                        w0: Fraction) -> dict[str, object]:
    """Check one literal two-pole pattern and derive its possible h.

    This is an audit helper.  A returned nonintegral ``h`` means the pattern
    cannot satisfy the two handshakes for the supplied edge invariants.
    """
    require(mu0 > mu >= 1, "pattern helper is for the difficult mu0>mu case")
    require(nu >= 1 and k >= 0 and lex >= 0, "invalid pattern indices")
    require(len(multiplicities) == k, "multiplicity census mismatch")
    require(all(1 <= m <= mu - 1 for m in multiplicities),
            "NE multiplicity must lie in [1,mu-1]")
    require(w > 0 and w0 > 0, "edge invariants must be positive")

    sm = sum(multiplicities)
    s = k + lex
    dp = mu0 + nu * (mu + sm)
    dq = 1 + nu * (1 + s)
    D = mu * dq - dp
    require(D >= 1, "nonzero arriving edge is not searrow")
    require(s >= 1, "positive degree gap forces at least one extra direction")
    A = mu * s - sm
    require(A >= s, "A>=s consequence of strict NE failed")
    require(D == nu * A - (mu0 - mu), "degree-gap identity failed")

    delta = mu0 - mu
    ratio = Fraction(dq, D)
    require(ratio <= 2 * delta + 3, "universal dq/D bound failed")
    kbar = mu * w * ratio
    X = kbar * Fraction(dp, dq)
    h = (kbar - X / mu0) / w0
    require(mu0 * h * w0 == delta * kbar + mu * w,
            "case-III handshake elimination failed")
    general = incoming_index_certificate(mu, w, mu0, w0)
    require(h <= Fraction(str(general["h_upper"])),
            "derived h exceeds universal bound")
    return {
        "mu": mu,
        "mu0": mu0,
        "nu_G": nu,
        "k": k,
        "lex": lex,
        "multiplicities": list(multiplicities),
        "dp": dp,
        "dq": dq,
        "D": D,
        "A": A,
        "dq_over_D": fraction_text(ratio),
        "kbar": fraction_text(kbar),
        "X": fraction_text(X),
        "h": fraction_text(h),
        "h_is_positive_integer": h.denominator == 1 and h >= 1,
        "universal_max_integer_h": general["max_integer_h"],
    }


def charged_certificate() -> dict[str, object]:
    # The S3/S5 discriminator: nonzero edge (mu,w)=(1,2), zero edge
    # (mu0,w0)=(2,3/2).  The universal theorem leaves h<=4, so the neutral
    # odd ray h>=3 has only h=3 to inspect.
    bound = incoming_index_certificate(1, Fraction(2), 2, Fraction(3, 2))
    require(bound["max_integer_h"] == 4, "charged bound mismatch")
    special = pattern_certificate(1, 2, 3, 0, 1, (),
                                  Fraction(2), Fraction(3, 2))
    require((special["dp"], special["dq"], special["h"]) == (5, 7, "3"),
            "charged special cell mismatch")
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "theorem_scope": "TWO-POLE CASE-III MERGES ONLY",
        "bound": bound,
        "charged_neutral_ray": {
            "domain": "odd h>=3",
            "finite_candidates_after_bound": [3],
            "special_pattern": special,
            "special_verdict": "(dp,dq,M)=(5,7,1), MP2-dead",
            "generic_verdict": "every odd h>=5 excluded before cell solve",
        },
        "notation_correction": (
            "the merge-local nu_G in dp,dq is distinct from the incoming "
            "case-III index h=nu_H"
        ),
        "firewall": {
            "equal_nonzero_join_kbar_bounded": False,
            "multipole_merges": False,
            "full_merge_grammar": False,
            "landing": False,
            "degree_bound": False,
            "jc2": False,
        },
    }
    body = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["certificate_sha256"] = hashlib.sha256(body).hexdigest()
    return payload


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    blob = json.dumps(charged_certificate(), indent=2, sort_keys=True) + "\n"
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(blob)
    else:
        print(blob, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
