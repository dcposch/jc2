"""Own-disc data for Moh 6.3, conditional on the reduced source hypotheses.

All arithmetic is exact.  A source row is necessary data, not a polynomial
pair.  ``V_vectors`` enumerates necessary first-support alternatives, NOT
realizable pairs.  An empty set is retained; it is never filled with a cap,
copied V, or an arbitrary representative.  The old scalar descend API is not
used here.

Sources: Moh (1983), pp.150, 170, 179-180, 188-190, 196-199, 207.
Proof and scope: xmodel/child-own-v-astra-20260905.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd
from typing import Any, Mapping

from .own_v_routes import OwnVRouteTree


def exact_int(value: Any) -> int:
    """Reject nonintegral values rather than truncating them."""
    value = Q(value)
    if value.denominator != 1:
        raise ValueError(f"nonintegral characteristic datum: {value}")
    return value.numerator


def prefix_gcds(n: int, M: Mapping[int, int]) -> dict[int, int]:
    d = {1: n}
    for i in range(1, len(M) + 1):
        d[i + 1] = gcd(d[i], M[i])
    return d


def characteristic_mu(M: Mapping[int, int], d: Mapping[int, int]) -> dict[int, int]:
    """Recurrence derived from p.150, not its inconsistent p.154 display."""
    mu = {1: M[1]}
    for i in range(2, len(M) + 1):
        mu[i] = exact_int(Q(d[i - 1], d[i]) * mu[i - 1] + M[i] - M[i - 1])
    return mu


def def51_radii(n: int, M: Mapping[int, int], d: Mapping[int, int],
                V: Mapping[int, int], multiplier: int = 1) -> dict[int, Q]:
    """Printed source formula, optionally scaled for a CONFIRMED child top.

    The multiplier alone is not a theorem that a retained prefix is terminal.
    ``descend_own`` therefore calls the child version only for u_s=1.
    """
    s = len(M)
    if n - M[s] - 1 == 0:
        raise ValueError("drop the ineffective n-1 tail before computing radii")
    answer = {}
    for i in range(1, s + 1):
        ratio = Q(n - M[i], n - M[s] - 1)
        for j in range(i + 1, s + 1):
            ratio *= Q(V[j] * (n - M[j]) - d[j],
                       V[j] * (n - M[j - 1]) - d[j])
        answer[i] = multiplier * (1 - ratio)
    return answer


def finite_datum(values, *, basis: str) -> dict:
    values = sorted(set(Q(v) for v in values))
    return {"type": "DETERMINED" if len(values) == 1 else "SET-VALUED",
            "values": values, "empty": not values, "basis": basis}


def inverse_top(n: int, ds: int, dprev: int, us: int, vs: int,
                delta: Q, zero_multiplicity: int,
                orbit_multiplicities: tuple[int, ...]) -> dict:
    """Invert an explicit top p=xi^z product(xi^b-c)^r factor pattern.

    One source b-orbit produces a CHILD COEFFICIENT DISC for each of a
    inverse coefficients, with r*n/dprev roots in each.  Multiplication by
    u_s is absent from this projection count; the gamma cover changes
    exponents, not the degree in the root variable.
    """
    delta = Q(delta)
    if delta <= 0:
        raise ValueError("inverse_top requires a positive source radius")
    a, b = delta.numerator, delta.denominator
    P = exact_int(Q(vs * dprev, ds))
    if zero_multiplicity < 0 or any(r <= 0 for r in orbit_multiplicities):
        raise ValueError("invalid multiplicities")
    if zero_multiplicity + b * sum(orbit_multiplicities) != P:
        raise ValueError("factor pattern does not have the source p degree")
    normalizer = Q(n, dprev)
    W0 = Q(us * dprev, ds) - a * sum(orbit_multiplicities)
    groups = [dict(kind="zero", V=W0, roots=normalizer * W0)]
    for orbit, multiplicity in enumerate(orbit_multiplicities):
        for coefficient in range(a):
            groups.append(dict(kind="nonzero", orbit=orbit,
                               coefficient=coefficient, V=Q(multiplicity),
                               roots=normalizer * multiplicity))
    assert sum(g["roots"] for g in groups) == Q(us * n, ds)
    return dict(source_p_degree=P, source_radius=delta,
                child_growth=Q(us, 1) / delta - vs,
                source_roots_per_coefficient=normalizer,
                inverse_groups=groups)


def descend_own(source, *, radius_licensed: bool = False,
                reduced_source: bool = True) -> dict:
    """Return exact M', d' and a correlated finite set of own V' vectors.

    ``source`` has the Skel attributes n,m,s,M,V; d/delta are recomputed.
    The method is for the campaign's reduced, normalized source tower with
    M_s=n-2 and delta_s=-1.  It does not silently extend to arbitrary pairs.
    ``radius_licensed`` asserts an independently supplied Prop6.3 radius
    proof for u_s>1; u_s=1 is automatic by Prop6.4.

    Values on empty full-route sets are not called own data.  Independent
    ``level2_identity`` and ``local_V`` expose conditional deductions that
    remain useful for diagnosing an incompatible source row (e.g. gate96).
    """
    if not reduced_source:
        raise ValueError("OPEN: nonreduced/all-zero source towers need extra data")
    n, m, s = exact_int(source.n), exact_int(source.m), exact_int(source.s)
    M = {i: exact_int(source.M[i]) for i in range(1, s + 1)}
    d = prefix_gcds(n, M)
    V = {i: exact_int(source.V[i]) for i in range(2, s + 1)}
    V[s + 1] = d[s + 1]
    delta = def51_radii(n, M, d, V)
    if M[1] != -m or M[s] != n - 2 or delta[s] != -1:
        raise ValueError("outside the normalized campaign source scope")
    if not (0 < delta[1] < 1) or any(delta[i] >= 1 for i in delta):
        raise ValueError("source radius hypotheses of first-support proof fail")
    if any(delta[i] >= delta[i - 1] for i in range(2, s + 1)):
        raise ValueError("source radii are not a strict tower")
    ds, vs = d[s], V[s]
    us, ell = ds - vs, 2 * vs - ds - 1
    if us < 1 or ell < 0:
        raise ValueError("Prop6.3 degree/Jacobian parameters outside scope")
    scale = Q(us, ds)
    np, mp = exact_int(n * scale), exact_int(m * scale)
    raw_M = {i: exact_int(M[i] * scale) for i in range(1, s)}
    raw_d = prefix_gcds(np, raw_M)
    assert raw_d == {i: exact_int(d[i] * scale) for i in range(1, s + 1)}
    assert raw_d[s] == us
    dropped = raw_M[s - 1] == np - 1
    effective_M = {i: value for i, value in raw_M.items()
                   if not (dropped and i == s - 1)}
    effective_d = prefix_gcds(np, effective_M)
    se = len(effective_M)
    mu = characteristic_mu(M, d)
    child_mu = characteristic_mu(raw_M, raw_d)
    assert all(child_mu[i] == scale * mu[i] for i in child_mu)

    # Until first nonzero support, all selected discs are Galois invariant.
    # Hence the modulus is den(delta_i), NOT an accumulated denominator.
    Wzero = {s: Q(us)}
    local = {i: set() for i in range(2, s)}
    choices, steps = [], []
    first_failure = None
    for i in range(s - 1, 1, -1):
        di = delta[i]
        P = exact_int(Q(V[i + 1] * d[i], d[i + 1]))
        b = di.denominator
        zero_ok = (P - V[i]) % b == 0
        nonzero_ok = di > 0 and b * V[i] <= P
        step = dict(i=i, source_delta=di, full_denominator=b,
                    P=P, selected_V=V[i], zero_ok=zero_ok,
                    nonzero_ok=nonzero_ok, incoming_child_V=Wzero[i + 1])
        if nonzero_ok:
            vector = {k: Wzero[k] if k > i else Q(V[k])
                      for k in range(2, s)}
            choices.append(dict(first_nonzero=i, V=vector))
            for k, value in vector.items():
                local[k].add(value)
        if zero_ok:
            Wzero[i] = Q(d[i], d[i + 1]) * Wzero[i + 1] - di * (P - V[i])
            step["zero_child_V"] = Wzero[i]
            # This is a local implication, not a completed reduced tower.
            local[i].add(Wzero[i])
        else:
            first_failure = i
        steps.append(step)
        if not zero_ok:
            break

    # The local projection is an OUTER set.  Source siblings must extend too.
    # Check them with the actual centre stabilizer; zero adds no denominator.
    outer_choices = choices
    engine = OwnVRouteTree(source)
    full_choices = []
    rejected_routes = []
    for choice in outer_choices:
        witness = engine.compatible_first_support(choice["first_nonzero"])
        if witness is None:
            rejected_routes.append(choice["first_nonzero"])
        else:
            full_choices.append(dict(**choice, source_tree_witness=witness))
    obstructions = []
    if dropped:
        # At source delta_(s-1)=0, p170 supplies >=3 distinct constants in
        # the retained T_(s-1). At least one stays nonzero under ANY single
        # normalization. It maps to a pole above finite nonzero gamma,
        # impossible for a root of a monic polynomial in k[gamma][pi].
        r = s - 1
        q_degree = exact_int(Q(V[s] * (n - M[r]), d[s]))
        p_exponent = exact_int(Q(-mu[r] + M[r] - n, d[r]))
        assert us == 1 and delta[r] == 0 and q_degree >= 3 and p_exponent >= 0
        obstructions.append(dict(type="DETERMINED", name="PROP6.3_FINITE_POLE",
                                 source_q_degree=q_degree,
                                 source_p_exponent=p_exponent,
                                 license="Prop6.4; Prop4.6 p170; Prop6.3(1)(2)"))
    choices = [] if obstructions else full_choices

    # Do not remove alternatives using U-NEG, C-TOP or any child cap.
    # These are consequences/checks, never generators for a missing V.
    vectors = sorted({tuple(c["V"][i] for i in range(2, s)) for c in choices})
    effective_vectors = sorted({v[:se - 1] for v in vectors})
    marginals = {i: finite_datum((v[i - 2] for v in effective_vectors),
                               basis="full necessary first-support routes")
                 for i in range(2, se + 1)}
    diagnostic_radii = []
    for choice in outer_choices:
        j = choice["first_nonzero"]
        e = delta[j]
        vector = tuple(choice["V"][i] for i in range(2, se + 1))
        metric = {i: vs - Q(us, 1) / delta[i] if i >= j else
                  vs - us - Q(us, 1) / e * (1 - delta[i])
                  for i in range(1, se + 1)}
        record = dict(V=vector, first_nonzero=j, delta=metric,
                      basis="local inverse map on the selected source discs")
        if us == 1:
            vp = {i: exact_int(vector[i - 2]) for i in range(2, se + 1)}
            vp[se + 1] = effective_d[se + 1]
            formula = def51_radii(np, effective_M, effective_d, vp, ell + 1)
            record["effective_formula_diagnostic"] = formula
            record["effective_formula_agrees"] = formula == metric
            if not dropped:
                assert formula == metric
        diagnostic_radii.append(record)
    retained_first = {c["first_nonzero"] for c in choices}
    child_radii = [r for r in diagnostic_radii if r["first_nonzero"] in retained_first]
    # The all-zero bottom branch is outside reduced source scope. Its formal
    # subtraction is recorded in route_steps, never exposed as own level-2 V.
    local[2] = {Q(V[2])}

    return dict(
        schema="jc2.descend-own/v1", source=dict(n=n, m=m, s=s, M=M, d=d,
                                               V=V, delta=delta),
        n=np, m=mp, ell=ell, us=us, vs=vs, ds=ds, scale=scale,
        s_raw=s - 1, raw_M=raw_M, raw_d=raw_d,
        s=se, M=effective_M, d=effective_d, dropped=dropped,
        characteristic_type="DETERMINED", characteristic_scope=(
            "effective complete chain" if us == 1 else "retained prefix only"),
        source_mu=mu, child_mu=child_mu,
        quasi_root_pi_degrees={i: -child_mu[i] for i in child_mu},
        descent_license=("DETERMINED_PROP6.4" if us == 1 else
                         "DETERMINED_SUPPLIED_RADIUS" if radius_licensed else
                         "CONDITIONAL_PROP6.3_RADIUS"),
        top_license=("NO_CHILD_PROP6.3_FINITE_POLE" if dropped else
                     "DETERMINED_COMPLETE_US1" if us == 1 else
                     "OPEN_CHILD_TERMINAL_IDENTIFICATION"),
        V_type="DETERMINED" if len(effective_vectors) == 1 else "SET-VALUED",
        V_scope="finite necessary alternatives; no source realization asserted",
        V=marginals, V_vectors=effective_vectors, raw_V_vectors=vectors,
        route_state=("EMPTY_PROP6.3_FINITE_POLE" if obstructions else
                     "NONEMPTY" if vectors else
                     "EMPTY_NECESSARY_FIRST_SUPPORT" if not outer_choices else
                     "EMPTY_NECESSARY_WHOLE_SOURCE_TREE"),
        routes=choices, route_steps=steps, zero_route_first_failure=first_failure,
        outer_routes=outer_choices, full_source_routes=full_choices,
        source_tree_rejected_first_support=rejected_routes,
        outer_V_vectors=sorted({tuple(c["V"][i] for i in range(2, se + 1))
                                for c in outer_choices}),
        licensed_obstructions=obstructions,
        local_V={i: finite_datum(local[i], basis="local inversion implication")
                 for i in local},
        level2_identity=finite_datum([V[2]], basis=(
            "Prop5.5/5.6 reduced source; invert its selected nonzero-centred D1")),
        copied_V={i: V[i] for i in range(2, se + 1)},
        u_negative=dict(type="DETERMINED", value=V[2] > raw_d[2],
                        scope="conditional own-D1 identity; requires licensed descent"),
        child_radii=child_radii, diagnostic_radii=diagnostic_radii,
    )
