#!/usr/bin/env python3
"""Proof-carrying disjoint row shards for the V50 exhaustive source audit.

The frozen V43 certificate reduces the genuine 2,893-term P12 against the
post-transport first rows and gives

    first_source + M*N13 = P12 - (-k/50).

The frozen V34/V47 producer computes N13 through first, previous/pole, and
current echelon stages, but its compact report does not compose those stages
back to the post-transport source rows.  This producer performs that missing
composition.  It uses exact sparse polynomial division by every normalized
affine pivot, replays each lifted row, and finally substitutes the resulting
source expression for N13 into the V43 identity.

V48 correctly reached the staged N13 identity but then used the linear-row
packer on the genuinely quadratic pre-first previous/current source rows.
V55 partitions all 54 arbitrary-degree previous/pole originals.  V56
partitions all 40 arbitrary-degree current originals and lazily lifts every
previous-row ancestor used by each shard.  Each row is reduced and replayed
by the unchanged V53/V50 exact source code.  A separate union checker must
prove that the immutable shard outputs are disjoint and exhaustive before
they can supplement V53; no individual shard is a source identity or cover.

Scope is deliberately strict: the 132-variable transport parameterization is
retained, so this is a post-transport source-row certificate on the generic
center chart.  The output emits the actual coefficient and termwise common
denominators.  A generic-open repair is licensed only if their radicals have
no factors beyond U, H=C-3U^2, and B3.  Otherwise every extra divisor remains
charged.  No multivariate gcd is treated as a Bezout certificate.
"""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PARENT_PATH = (
    HERE.parent
    / "td6_c1_c2_c3_q2_full_p12_n13_unit_canonical_20260825"
    / "replay.py"
)
PARENT_SHA256 = "3cc0fc3bc4a55810c4d4320b53ff77a48341045c06f556cd6243119b8fe4c332"
assert sha256(PARENT_PATH.read_bytes()).hexdigest() == PARENT_SHA256
spec = importlib.util.spec_from_file_location("td6_v48_p12_parent", PARENT_PATH)
g = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = g
spec.loader.exec_module(g)

assert sys.argv[1:] == []
n, r, tri, b = g.n, g.r, g.tri, g.b
Rat3, E3, BetaPoly = g.Rat3, g.E3, g.BetaPoly
C, V, U, H, B3 = g.C, g.V, g.U, g.H, g.B3
qd, nr = g.qd, g.nr
SHARD_MODE = os.environ.get("TD6_SHARD_MODE", "")
SHARD_INDEX = int(os.environ.get("TD6_SHARD_INDEX", "-1"))
SHARD_COUNT = int(os.environ.get("TD6_SHARD_COUNT", "0"))
assert SHARD_MODE in {"previous", "current"}
assert SHARD_COUNT > 0 and 0 <= SHARD_INDEX < SHARD_COUNT


def row_polynomial(record):
    if len(record) == 2:
        return record[1]
    _, row, rhs = record
    return n.source_polynomial(row, rhs)


def source_records(family, polynomials):
    """Keep arbitrary-degree original equations, including exact zero rows."""
    return [
        ((family, degree), g.clean(polynomial))
        for degree, polynomial in enumerate(polynomials)
    ]


def total_degree(polynomial):
    return max((len(monomial) for monomial in polynomial), default=-1)


def remap_polynomial(polynomial, variable_map):
    """Rename variables through an injective integer map."""
    out = {}
    for monomial, coefficient in polynomial.items():
        mapped = tuple(sorted(variable_map[variable] for variable in monomial))
        value = out.get(mapped, BetaPoly()) + coefficient
        if value:
            out[mapped] = value
        else:
            out.pop(mapped, None)
    return out


def scalar_polynomial(value):
    value = BetaPoly.coerce(value)
    return {(): value} if value else {}


def add_scaled_product(target, left, right, scale=1):
    return g.add(target, g.multiply(left, right), scale)


def add_multiplier(target, index, polynomial, scale=1):
    value = g.add(target[index], polynomial, scale)
    target[index] = value


def source_replay(multiplier_families, row_families):
    replay = {}
    for multipliers, rows in zip(multiplier_families, row_families):
        assert len(multipliers) == len(rows)
        for multiplier, row in zip(multipliers, rows):
            if multiplier:
                replay = add_scaled_product(replay, multiplier, row_polynomial(row))
    return g.clean(replay)


def parameterize_with_pivots(nvariables, rows, stage):
    pivots, _, factors, dependent = n.solve_stage(nvariables, rows, stage)
    assert all(not rhs for _, _, rhs, _ in dependent), (stage, dependent)
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (
                BetaPoly(), {parameter_of[variable]: BetaPoly(1)}
            )
            continue
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other == variable:
                continue
            assert other > variable and forms[other] is not None
            form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for key, row, rhs in rows:
        got = (BetaPoly(), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (BetaPoly.coerce(rhs), {}), (stage, key, got, rhs)
    print(f"{stage}_affine_parameterization_replay=true", flush=True)
    return pivots, forms, free, factors, dependent


def factor_strings(polynomial):
    if not polynomial or polynomial.total_degree() == 0:
        return []
    unit, factors = polynomial.factor()
    assert unit
    return sorted((str(factor), exponent) for factor, exponent in factors)


def write_denominator(outdir, label, polynomial):
    text = str(polynomial) + "\n"
    factor_text = "\n".join(
        f"{exponent}\t{factor}" for factor, exponent in factor_strings(polynomial)
    ) + "\n"
    polynomial_path = outdir / f"{label}.txt"
    factors_path = outdir / f"{label}.factors.txt"
    polynomial_path.write_text(text)
    factors_path.write_text(factor_text)
    print(f"{label}_path={polynomial_path}")
    print(f"{label}_sha256={sha256(text.encode()).hexdigest()}")
    print(f"{label}_summary={tri.polynomial_summary(polynomial)}")
    print(f"{label}_factor_count={len(factor_strings(polynomial))}")
    print(f"{label}_factors_sha256={sha256(factor_text.encode()).hexdigest()}")


def beta_values(polynomial_families):
    for family in polynomial_families:
        for polynomial in family:
            yield from polynomial.values()


def termwise_values(multiplier_families, row_families):
    slots = 0
    values = []
    for multipliers, rows in zip(multiplier_families, row_families):
        for multiplier, row in zip(multipliers, rows):
            source = row_polynomial(row)
            for left in multiplier.values():
                for right in source.values():
                    values.append(left * right)
                    slots += 1
    return values, slots


def denominators_divide_beta(value, common):
    value = BetaPoly.coerce(value)
    for coefficient in value.coefficients:
        for coordinate in tri.e3_rat3_coordinates(coefficient):
            if common % coordinate.denominator:
                return False
    return True


def build_transport_and_rows():
    r.fb.CENTER = (Rat3(C), Rat3(V), Rat3(U))
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)},
        r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN,
    )
    ng, rows_g = r.fb.build_transport(
        25, 100, 5, {1: r.b.Q(1), 25: r.b.Q(1)},
        r.fb.F1_G_PATTERN, r.fb.POLE_G_PATTERN,
    )
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (
            ('g',) + key,
            {nf + variable: coefficient for variable, coefficient in row.items()},
            rhs,
        )
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in transport if row[0][1] != 'X'] + [
        row for row in transport if row[0][1] == 'X'
    ]
    transport_pivots, records, events, _ = tri.factor_transport(ordered)
    pivot_rhs_dual, compatibility = b.propagate_beta(ordered, records)
    assert not compatibility and len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    assert len(free) == 132
    free_parameter = {variable: index for index, variable in enumerate(free)}

    def restrict(row):
        return n.convert_form(b.restrict_row_beta(
            row, transport_pivots, pivot_rhs_dual, free_parameter
        ))

    bands132 = {}
    for owner, imax, jmax, offset in (
        ('f', 15, 60, 0), ('g', 25, 100, nf)
    ):
        for exponent in (1, 2, 3):
            forms = []
            for degree in range(16 if owner == 'f' else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in r.fb.x_chart_coefficient(
                        imax, jmax, exponent, degree
                    ).items()
                }
                forms.append(restrict(row))
            bands132[(owner, exponent)] = forms

    pole_f132 = []
    for degree in range(61):
        row = {
            variable: Rat3.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                15, 60, -2, degree
            ).items()
        }
        pole_f132.append(restrict(row))
    pole_g132 = []
    for degree in range(101):
        row = {
            nf + variable: Rat3.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                25, 100, -4, degree
            ).items()
        }
        pole_g132.append(restrict(row))
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_event_count={len(events)}")
    print("transport_matrix_beta_independent=true")
    print("transport_rhs_beta_affine_exact=true")
    print("transport_x_and_pole_sections_exact=true", flush=True)
    return bands132, pole_f132, pole_g132


def main():
    outdir = Path(os.environ.get("TD6_OUTPUT_DIR", ".")).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-A3-Q2-SOURCE-ROW-SHARDS-V55-V56")
    print(f"shard_mode={SHARD_MODE}")
    print(f"shard_index={SHARD_INDEX}")
    print(f"shard_count={SHARD_COUNT}")
    print("V48_failure_class=linear_packer_rejected_genuine_quadratic_source_rows")
    print("arbitrary_degree_original_rows_preserved=true")
    print("dependency_closed_fast_discriminator=true")
    print("full_unused_row_audit_deferred_to_V50=true")
    print("beta_parameter_name=beta")
    print("q_beta=t+beta*t^2+t^25")
    print("q_beta_prime=1+2*beta*t+25*t^24")
    print("source_center=(C,V,U)")
    print("scope=post_transport_132_variable_source_rows")
    print("transport_chart=D(U*H*B3)")
    print("multivariate_gcd_used_as_bezout=false")
    print("two_chart_glue_required_form=a*d1+b*d2=(U*H*B3)^N")
    print(f"parent_sha256={PARENT_SHA256}", flush=True)

    bands132, pole_f132, pole_g132 = build_transport_and_rows()
    n.configure_qd(direct_qprime=True)
    first_rows = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands132[('f', 1)], bands132[('g', 1)]
        )
    )
    first_pivots, forms94, free94, first_factors, first_dependent = (
        parameterize_with_pivots(132, first_rows, "first_v50")
    )
    assert len(first_pivots) == 38 and len(free94) == 94
    map132_to_94 = {variable: index for index, variable in enumerate(free94)}
    map94_to_132 = {index: variable for index, variable in enumerate(free94)}

    bands94 = {key: n.compose(forms, forms94) for key, forms in bands132.items()}
    pole_f94 = n.compose(pole_f132, forms94)
    pole_g94 = n.compose(pole_g132, forms94)
    previous_rows = qd.pack(
        'X-1', qd.compile_previous(
            bands94[('f', 1)], bands94[('f', 2)],
            bands94[('g', 1)], bands94[('g', 2)],
        )
    )
    previous_rows += qd.pack(
        'P1', qd.compile_pole_previous(pole_f94, pole_g94)
    )
    previous_pivots, forms56, free56, previous_factors, previous_dependent = (
        parameterize_with_pivots(94, previous_rows, "previous_pole_v50")
    )
    assert len(previous_pivots) == 38 and len(free56) == 56
    map94_to_56 = {variable: index for index, variable in enumerate(free56)}
    map56_to_132 = {
        index: free94[variable] for index, variable in enumerate(free56)
    }

    bands56 = {key: n.compose(forms, forms56) for key, forms in bands94.items()}
    current_rows = qd.pack('X0', qd.compile_current(
        *[bands56[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands56[('g', exponent)] for exponent in (1, 2, 3)],
    ))
    current_pivots, _, current_factors, current_dependent = n.solve_stage(
        56, current_rows, "current_v50"
    )
    assert len(current_pivots) == 25
    n13_records = [
        record for record in current_dependent
        if record[1] == ('X0', 13) and record[2]
    ]
    assert len(n13_records) == 1
    _, _, n13, n13_weights = n13_records[0]
    S = E3(qd.uniform.S_FIELD)
    k = E3(252) - 342*S + 144*S**2 - 36*S**3
    expected_n13 = BetaPoly([0, k/25])
    assert n13 == expected_n13 and k * k.inverse() == E3(1)
    print(f"N13_equals_k_beta_over_25={str(n13 == expected_n13).lower()}")
    print(f"N13_left_null_support={len(n13_weights)}")
    print(f"N13_left_null_sha256={n.digest(tuple(sorted(n13_weights.items())))}")
    print(f"k_inverse_sha256={n.digest(k.inverse())}", flush=True)

    raw_previous_rows = source_records(
        'X-1', qd.compile_previous(
            bands132[('f', 1)], bands132[('f', 2)],
            bands132[('g', 1)], bands132[('g', 2)],
        )
    )
    raw_previous_rows += source_records(
        'P1', qd.compile_pole_previous(pole_f132, pole_g132)
    )
    raw_previous_index = {
        record[0]: index for index, record in enumerate(raw_previous_rows)
    }
    assert len(raw_previous_index) == len(raw_previous_rows)
    previous_reduced = {
        record[0]: row_polynomial(record) for record in previous_rows
    }
    assert set(previous_reduced) <= set(raw_previous_index)

    previous_first_relations_by_key = {}

    def lift_previous_key(key):
        if key in previous_first_relations_by_key:
            return previous_first_relations_by_key[key]
        raw_record = raw_previous_rows[raw_previous_index[key]]
        raw_polynomial = row_polynomial(raw_record)
        remainder132, quotients = g.divide_polynomial(raw_polynomial, first_pivots)
        relation = g.lift_relations(quotients, first_pivots, len(first_rows))
        remainder94 = remap_polynomial(remainder132, map132_to_94)
        expected = previous_reduced.get(key, {})
        assert g.clean(remainder94) == g.clean(expected), (
            "previous exact source reduction", key,
            g.clean(remainder94), g.clean(expected),
        )
        replay = source_replay((relation,), (first_rows,))
        target = g.add(raw_polynomial, remap_polynomial(remainder94, map94_to_132), -1)
        assert replay == g.clean(target)
        previous_first_relations_by_key[key] = relation
        return relation

    quadratic_previous = [
        record for record in raw_previous_rows
        if total_degree(row_polynomial(record)) == 2
    ]
    assert quadratic_previous
    quadratic_key = quadratic_previous[0][0]
    quadratic_relation = lift_previous_key(quadratic_key)
    quadratic_raw = row_polynomial(quadratic_previous[0])
    quadratic_remainder, _ = g.divide_polynomial(quadratic_raw, first_pivots)
    assert source_replay((quadratic_relation,), (first_rows,)) == g.clean(
        g.add(quadratic_raw, quadratic_remainder, -1)
    )
    print(f"previous_raw_row_count_available={len(raw_previous_rows)}")
    print(f"previous_raw_quadratic_row_count={len(quadratic_previous)}")
    print(f"quadratic_source_positive_control_key={quadratic_key}")
    print("quadratic_source_positive_control_exact=true")
    print("dependency_selected_previous_rows_reduced_exactly=true", flush=True)

    if SHARD_MODE == "previous":
        selected_indices = [
            index for index in range(len(raw_previous_rows))
            if index % SHARD_COUNT == SHARD_INDEX
        ]
        selected_keys = []
        row_digests = []
        relation_digests = []
        for ordinal, row_index in enumerate(selected_indices):
            record = raw_previous_rows[row_index]
            key = record[0]
            relation = lift_previous_key(key)
            raw_digest = n.digest(row_polynomial(record))
            relation_digest = n.digest(relation)
            selected_keys.append(key)
            row_digests.append(raw_digest)
            relation_digests.append(relation_digest)
            print(f"previous_shard_row[{ordinal}]_index={row_index}")
            print(f"previous_shard_row[{ordinal}]_key={key}")
            print(f"previous_shard_row[{ordinal}]_raw_sha256={raw_digest}")
            print(
                f"previous_shard_row[{ordinal}]_relation_sha256="
                f"{relation_digest}",
                flush=True,
            )
        print(f"previous_total_original_row_count={len(raw_previous_rows)}")
        print(f"previous_shard_selected_count={len(selected_indices)}")
        print(f"previous_shard_indices={selected_indices}")
        print(f"previous_shard_keys={selected_keys}")
        print(f"previous_shard_indices_sha256={n.digest(tuple(selected_indices))}")
        print(f"previous_shard_rows_sha256={n.digest(tuple(row_digests))}")
        print(
            f"previous_shard_relations_sha256="
            f"{n.digest(tuple(relation_digests))}"
        )
        print("previous_shard_original_row_replay=true")
        print("shard_union_required_before_completeness=true")
        print("full_source_identity_replayed=false")
        print("full_A3_beta_family_killed=false")
        print("whole_TD6_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-A3-Q2-SOURCE-ROW-SHARD-V55 PASS")
        return

    raw_current_rows = source_records('X0', qd.compile_current(
        *[bands132[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands132[('g', exponent)] for exponent in (1, 2, 3)],
    ))
    raw_current_index = {
        record[0]: index for index, record in enumerate(raw_current_rows)
    }
    assert len(raw_current_index) == len(raw_current_rows)
    current_reduced = {
        record[0]: row_polynomial(record) for record in current_rows
    }
    assert set(current_reduced) <= set(raw_current_index)
    current_stage_index = {
        record[0]: index for index, record in enumerate(current_rows)
    }

    current_lift_cache = {}

    def lift_current_key(key):
        if key in current_lift_cache:
            return current_lift_cache[key]
        raw_polynomial = row_polynomial(raw_current_rows[raw_current_index[key]])
        remainder132, first_quotients = g.divide_polynomial(
            raw_polynomial, first_pivots
        )
        first_only_relation = g.lift_relations(
            first_quotients, first_pivots, len(first_rows)
        )
        remainder94 = remap_polynomial(remainder132, map132_to_94)
        remainder94_after, previous_quotients = g.divide_polynomial(
            remainder94, previous_pivots
        )
        previous_relation94 = g.lift_relations(
            previous_quotients, previous_pivots, len(previous_rows)
        )
        remainder56 = remap_polynomial(remainder94_after, map94_to_56)
        expected = current_reduced.get(key, {})
        assert g.clean(remainder56) == g.clean(expected), (
            "current exact source reduction", key,
            g.clean(remainder56), g.clean(expected),
        )

        first_relation = [dict(polynomial) for polynomial in first_only_relation]
        previous_relation132 = [{} for _ in raw_previous_rows]
        for previous_index, polynomial in enumerate(previous_relation94):
            multiplier132 = remap_polynomial(polynomial, map94_to_132)
            if not multiplier132:
                continue
            previous_key = previous_rows[previous_index][0]
            previous_relation132[raw_previous_index[previous_key]] = multiplier132
            for first_index, nested in enumerate(
                lift_previous_key(previous_key)
            ):
                if nested:
                    first_relation[first_index] = g.add(
                        first_relation[first_index],
                        g.multiply(multiplier132, nested),
                        -1,
                    )

        replay = source_replay(
            (first_relation, previous_relation132),
            (first_rows, raw_previous_rows),
        )
        embedded56 = remap_polynomial(remainder56, map56_to_132)
        target = g.add(raw_polynomial, embedded56, -1)
        assert replay == g.clean(target)
        record = (
            raw_polynomial, remainder94, remainder56,
            first_only_relation, first_relation, previous_relation132,
        )
        current_lift_cache[key] = record
        return record

    def lift_current(row_index):
        return lift_current_key(current_rows[row_index][0])

    if SHARD_MODE == "current":
        selected_indices = [
            index for index in range(len(raw_current_rows))
            if index % SHARD_COUNT == SHARD_INDEX
        ]
        selected_keys = []
        row_digests = []
        lift_digests = []
        for ordinal, row_index in enumerate(selected_indices):
            key = raw_current_rows[row_index][0]
            lift = lift_current_key(key)
            raw_digest = n.digest(row_polynomial(raw_current_rows[row_index]))
            lift_digest = n.digest(lift)
            selected_keys.append(key)
            row_digests.append(raw_digest)
            lift_digests.append(lift_digest)
            print(f"current_shard_row[{ordinal}]_index={row_index}")
            print(f"current_shard_row[{ordinal}]_key={key}")
            print(f"current_shard_row[{ordinal}]_raw_sha256={raw_digest}")
            print(
                f"current_shard_row[{ordinal}]_lift_sha256={lift_digest}",
                flush=True,
            )
        print(f"current_total_original_row_count={len(raw_current_rows)}")
        print(f"current_shard_selected_count={len(selected_indices)}")
        print(f"current_shard_indices={selected_indices}")
        print(f"current_shard_keys={selected_keys}")
        print(f"current_shard_indices_sha256={n.digest(tuple(selected_indices))}")
        print(f"current_shard_rows_sha256={n.digest(tuple(row_digests))}")
        print(f"current_shard_lifts_sha256={n.digest(tuple(lift_digests))}")
        print(
            f"current_shard_previous_ancestor_count="
            f"{len(previous_first_relations_by_key)}"
        )
        print(
            f"current_shard_previous_ancestor_keys="
            f"{sorted(previous_first_relations_by_key)}"
        )
        print("current_shard_original_row_replay=true")
        print("shard_union_required_before_completeness=true")
        print("full_source_identity_replayed=false")
        print("full_A3_beta_family_killed=false")
        print("whole_TD6_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-A3-Q2-SOURCE-ROW-SHARD-V56 PASS")
        return

    required_current = sorted(set(n13_weights) | {12})
    for row_index in required_current:
        lift_current(row_index)
    print(f"current_rows_source_lifted={len(required_current)}")
    print(f"current_rows_source_lifted_indices={required_current}")
    print(
        f"previous_rows_source_lifted={len(previous_first_relations_by_key)}"
    )
    print(
        "previous_rows_source_lifted_keys="
        f"{sorted(previous_first_relations_by_key)}"
    )
    print("dependency_closed_original_rows_reduced_exactly=true")
    print("current_through_previous_and_first_source_replay=true", flush=True)

    n13_first = [{} for _ in first_rows]
    n13_previous = [{} for _ in raw_previous_rows]
    n13_current = [{} for _ in raw_current_rows]
    for row_index, weight in n13_weights.items():
        key = current_rows[row_index][0]
        _, _, _, _, first_relation, previous_relation = lift_current(row_index)
        for index, multiplier in enumerate(first_relation):
            if multiplier:
                add_multiplier(n13_first, index, multiplier, weight)
        for index, multiplier in enumerate(previous_relation):
            if multiplier:
                add_multiplier(n13_previous, index, multiplier, weight)
        add_multiplier(
            n13_current, raw_current_index[key], scalar_polynomial(weight), -1
        )

    n13_replay = source_replay(
        (n13_first, n13_previous, n13_current),
        (first_rows, raw_previous_rows, raw_current_rows),
    )
    assert n13_replay == {(): n13}
    assert source_replay(
        (n13_first, n13_current), (first_rows, raw_current_rows)
    ) != {(): n13}
    print("N13_full_first_previous_current_source_identity_exact=true")
    print("N13_previous_ancestry_omission_negative_control=true")
    print(f"N13_source_identity_sha256={g.canonical_digest(n13_replay)}", flush=True)

    p12_stage_index = current_stage_index[('X0', 12)]
    p12_raw, p12_remainder94, _, p12_first_relation, _, _ = lift_current(
        p12_stage_index
    )
    raw_base = g.projection(p12_raw, 0)
    assert len(raw_base) == 2893
    assert g.polynomial_digest(raw_base) == (
        "8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da"
    )
    unit = -k/50
    assert g.projection(p12_remainder94, 0) == {(): unit}
    tail94 = g.beta_tail(p12_remainder94, unit)
    tail132 = remap_polynomial(tail94, map94_to_132)
    n13_multiplier = g.scale_polynomial(tail132, E3(25)/k)
    assert n13_multiplier

    unit_first = [g.scale_polynomial(value, -1) for value in p12_first_relation]
    unit_previous = [{} for _ in raw_previous_rows]
    unit_current = [{} for _ in raw_current_rows]
    add_multiplier(
        unit_current, raw_current_index[('X0', 12)], {(): BetaPoly(1)}
    )
    for target_family, n13_family in (
        (unit_first, n13_first),
        (unit_previous, n13_previous),
        (unit_current, n13_current),
    ):
        for index, multiplier in enumerate(n13_family):
            if multiplier:
                target_family[index] = g.add(
                    target_family[index],
                    g.multiply(n13_multiplier, multiplier),
                    -1,
                )

    row_families = (first_rows, raw_previous_rows, raw_current_rows)
    multiplier_families = (unit_first, unit_previous, unit_current)
    unit_replay = source_replay(multiplier_families, row_families)
    assert unit_replay == {(): BetaPoly(unit)}
    without_n13 = g.add(p12_raw, source_replay(
        (p12_first_relation,), (first_rows,)
    ), -1)
    assert without_n13 != {(): BetaPoly(unit)}
    assert g.add(unit_replay, {(): BetaPoly(1)}) != {(): BetaPoly(unit)}
    print("genuine_P12_2893_term_control=true")
    print("P12_N13_full_source_composition_exact=true")
    print("P12_without_N13_negative_control=true")
    print("plus_one_negative_control=true")
    print("combined_unit_residual_is_minus_k_over_50=true", flush=True)

    coefficient_denominator = n.denominator_lcm_beta(
        list(beta_values(multiplier_families))
    )
    term_values, term_slots = termwise_values(multiplier_families, row_families)
    termwise_denominator = n.denominator_lcm_beta(term_values + [BetaPoly(unit)])
    write_denominator(outdir, "COMBINED_COEFFICIENT_DENOMINATOR", coefficient_denominator)
    write_denominator(outdir, "COMBINED_TERMWISE_DENOMINATOR", termwise_denominator)
    coefficient_allowed = b.factors_only_allowed(coefficient_denominator)
    termwise_allowed = b.factors_only_allowed(termwise_denominator)
    print(f"combined_source_multiplier_slots={sum(len(p) for f in multiplier_families for p in f)}")
    print(f"combined_termwise_slots={term_slots}")
    print(f"coefficient_denominator_radical_subset_U_H_B3={str(coefficient_allowed).lower()}")
    print(f"termwise_denominator_radical_subset_U_H_B3={str(termwise_allowed).lower()}")
    assert all(denominators_divide_beta(value, termwise_denominator) for value in term_values)
    assert denominators_divide_beta(BetaPoly(unit), termwise_denominator)
    clear_scalar = E3(Rat3(termwise_denominator))
    cleared_replay = g.scale_polynomial(unit_replay, clear_scalar)
    cleared_target = {(): BetaPoly(unit * clear_scalar)}
    assert cleared_replay == cleared_target
    print("termwise_common_denominator_divisibility_exact=true")
    print("cleared_full_source_identity_exact=true")
    print(f"generic_open_localization_repaired={str(coefficient_allowed and termwise_allowed).lower()}")
    print("raw_U_H_B3_strata_still_separate=true")
    print("full_A3_beta_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("full_unused_previous_current_row_audit_complete=false")
    print("V50_full_audit_required_before_promotion=true")
    print("TD6-A3-Q2-FULL-SOURCE-GLUE-FAST-V53 PASS")


if __name__ == "__main__":
    main()
