#!/usr/bin/env python3
"""Exact nested-factor identities for the V82QSD CURRENT denominator."""

from hashlib import sha256
import os
from pathlib import Path
import platform

import flint


assert platform.system() == "Linux"
assert "Amazon EC2" in Path("/sys/devices/virtual/dmi/id/sys_vendor").read_text()
tag = os.environ.get("AWS_RUN_TAG", "")
assert tag.startswith("td6_v82qsf_nested_")

ctx = flint.fmpq_mpoly_ctx.get(["C", "V", "U"], ordering="lex")
C, V, U = ctx.gens()

F = C*U - V**2 + U**3
G = (
    4*C**2*U**2 - 8*C*V**2*U + 8*C*U**4
    + 5*V**4 - 8*V**2*U**3 + 4*U**6
)
L = (
    64*C**4*U**7 - 256*C**3*V**2*U**6 + 256*C**3*U**9
    + 4*C**2*V**6*U**2 + 432*C**2*V**4*U**5
    - 768*C**2*V**2*U**8 + 384*C**2*U**11
    - 4*C*V**8*U - 328*C*V**6*U**4 + 864*C*V**4*U**7
    - 768*C*V**2*U**10 + 256*C*U**13 + V**10
    + 100*V**8*U**3 - 332*V**6*U**6 + 432*V**4*U**9
    - 256*V**2*U**12 + 64*U**15
)

assert G == V**4 + 4*F**2
L_nested = 4*U**3*G**2 + V**4*(V**2 + 4*U**3)*(V**2 + 2*F)**2
assert L == L_nested

norm = flint.fmpq_mpoly_ctx.get(["x", "s"], ordering="lex")
x, s = norm.gens()
g = x**2 + 4*s**2
ell = (
    64*s**4 + 4*x**2*(x+12)*s**2 + 4*x**3*(x+4)*s
    + x**4*(x+8)
)
assert ell == 4*g**2 + x**2*(x+4)*(x+2*s)**2

F_target = V**8*(V**2 + 8*U**3)
F_quotient = (L - F_target) // F
assert L - F_target == F*F_quotient

A = V**2 + 2*F
collapse = G - A**2 + 2*A*V**2
assert collapse == 2*V**4
anorm = x + 2*s
assert g - anorm**2 + 2*anorm*x == 2*x**2

def digest(value):
    return sha256((str(value) + "\n").encode()).hexdigest()

print("producer=TD6-V82QSF-NESTED-CURRENT-DENOMINATOR")
print("aws_run_tag=" + tag)
print("python_flint_version=" + flint.__version__)
print("G_equals_V4_plus_4F2=true")
print("G_sha256=" + digest(G))
print("L_nested_identity=true")
print("L_sha256=" + digest(L))
print("L_nested_rhs_sha256=" + digest(L_nested))
print("normalized_identity=true")
print("normalized_ell_sha256=" + digest(ell))
print("F_zero_L=V^8*(V^2+8U^3)")
print("F_specialization_quotient_sha256=" + digest(F_quotient))
print("G_zero_L=V^4*(V^2+4U^3)*(V^2+2F)^2")
print("G_and_V2plus2F_collapse_certificate=2V^4")
print("normalized_G_and_xplus2s_collapse_certificate=2x^2")
print("normalized_radical_branches_on_DU=x=0_or_x=-4")
print("raw_fibres_still_require_source_rebuild=true")
print("no_current_coefficient_cover_family_TD6_SP2_landing_or_JC2_claim=true")
print("TD6 V82QSF NESTED DENOMINATOR IDENTITY PASS")
