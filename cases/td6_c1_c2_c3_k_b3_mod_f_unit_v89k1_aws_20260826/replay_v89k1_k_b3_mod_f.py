#!/usr/bin/env python3
"""Exact base-ring identity proving K is a unit modulo F on D(B3)."""

from hashlib import sha256
import os
from pathlib import Path

from flint import fmpq_mpoly_ctx


HERE = Path(__file__).resolve().parent
OUT = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89k1_k_b3_mod_f_")

CTX = fmpq_mpoly_ctx.get(["C", "V", "U"], ordering="lex")
C, V, U = CTX.gens()
F = C*U - V**2 + U**3
B3 = (
    4*C**2*U**2 - 4*C*V**2*U + 24*C*U**4
    + V**4 - 20*V**2*U**3 + 20*U**6
)
K = 2*C*V**2*U + 16*C*U**4 - V**4 - 14*V**2*U**3 + 16*U**6
G = 2*C*U - V**2 + 2*U**3


def canonical(polynomial):
    return repr(tuple(sorted(
        (monomial, str(coefficient))
        for monomial, coefficient in polynomial.to_dict().items()
    )))


def digest(polynomial):
    return sha256((canonical(polynomial) + "\n").encode()).hexdigest()


def specialize_f_zero(polynomial):
    """Evaluate C=(V^2-U^3)/U and return numerator after U clearing."""
    maximum_c = max((monomial[0] for monomial in polynomial.to_dict()), default=0)
    out = CTX.constant(0)
    for (ec, ev, eu), coefficient in polynomial.to_dict().items():
        out += (
            coefficient * (V**2-U**3)**ec * V**ev
            * U**(eu + maximum_c-ec)
        )
    return out, maximum_c


identity = B3 - K - 2*F*G
assert not identity
assert B3 - K - F*G
assert F and B3 and K and G
assert K != B3

k_f0, k_power = specialize_f_zero(K)
b3_f0, b3_power = specialize_f_zero(B3)
assert k_power == 1
assert b3_power == 2
assert k_f0 == U*V**4
assert b3_f0 == U**2*V**4

lines = [
    f"F={F}",
    f"B3={B3}",
    f"K={K}",
    f"G={G}",
    "identity=B3-K-2*F*G=0",
    f"F_sha256={digest(F)}",
    f"B3_sha256={digest(B3)}",
    f"K_sha256={digest(K)}",
    f"G_sha256={digest(G)}",
    f"F_zero_K_after_U_clear=U*V^4;sha256={digest(k_f0)}",
    f"F_zero_B3_after_U2_clear=U^2*V^4;sha256={digest(b3_f0)}",
    "F_zero_uncleared=K=B3=V^4",
    "consequence=K_is_unit_modulo_F_on_D(B3)",
    "inverse_class=B3^-1",
    "K_inverted=false",
    "F_inverted=false",
    "q_inverted=false",
    "P12_FIRST_only_unit_claim=false",
    "whole_TD6_killed=false",
    "JC2_resolved=false",
]
text = "\n".join(lines) + "\n"
result = OUT / "K_B3_MOD_F_EXACT_RESULT.txt"
result.write_text(text)
print(text, end="")
print("negative_control_B3_minus_K_minus_FG_nonzero=true")
print("exact_result_sha256=" + sha256(text.encode()).hexdigest())
print("TD6-V89K1-K-B3-MOD-F-UNIT PASS")
