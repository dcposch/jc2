#!/usr/bin/env python3
"""Exact generic TD6 center gate for (c1,c2,c3)=(C,V,U).

The entire matrix-changing transport, first affine band, and genuine P12 are
rebuilt over Q(C,V,U).  This is a generic-open producer only: every printed
pivot/denominator divisor remains a raw specialization obligation.
"""

from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "replay.py"
SOURCE_SHA256 = "56df638aaa3ae02cf437a32258a920a8a66afb2781c089e30b1774a5b38e65db"
assert sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256
spec = importlib.util.spec_from_file_location("td6_c1_c2_c3_source", SOURCE)
r = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = r
spec.loader.exec_module(r)

flint = r.t.flint
CTX = flint.fmpq_mpoly_ctx.get(["C", "V", "U"], ordering="lex")
C, V, U = CTX.gens()
ZERO, ONE = CTX.constant(0), CTX.constant(1)
B_LOCAL3 = "--b-local-pivots3" in sys.argv
STRATUM_ARGUMENTS = [
    argument.split("=", 1)[1]
    for argument in sys.argv[1:]
    if argument.startswith("--stratum=")
]
assert len(STRATUM_ARGUMENTS) <= 1
STRATUM = STRATUM_ARGUMENTS[0] if STRATUM_ARGUMENTS else "generic"
assert STRATUM in {
    "generic", "u-zero", "h-zero", "v-zero", "u-h-zero", "origin",
    "v-h-zero", "v-cplus1-zero", "v-cplus5-zero",
}
assert not (B_LOCAL3 and STRATUM != "generic")
B3 = (
    4*C**2*U**2 - 4*C*V**2*U + 24*C*U**4
    + V**4 - 20*V**2*U**3 + 20*U**6
)
T3 = (
    4*C**2*U**2 - 4*C*V**2*U + 28*C*U**4
    + V**4 - 24*V**2*U**3 + 24*U**6
)
P3 = V**4 - 32*V**2*U**3 + 128*U**6


def polynomial(value):
    if isinstance(value, flint.fmpq_mpoly):
        assert value.context() == CTX
        return value
    if isinstance(value, Fraction):
        return CTX.constant(flint.fmpq(value.numerator, value.denominator))
    if isinstance(value, flint.fmpq):
        return CTX.constant(value)
    return CTX.constant(value)


class Rat3:
    """Reduced exact rational function in Q(C,V,U)."""

    __slots__ = ("numerator", "denominator")
    inverse_count = 0

    def __init__(self, numerator=0, denominator=1, reduced=False):
        if isinstance(numerator, Rat3) and denominator == 1:
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator
            return
        numerator, denominator = polynomial(numerator), polynomial(denominator)
        if not denominator:
            raise ZeroDivisionError
        if not numerator:
            self.numerator, self.denominator = ZERO, ONE
            return
        if denominator.total_degree() == 0:
            scalar = denominator.leading_coefficient()
            self.numerator, self.denominator = numerator / scalar, ONE
            return
        if not reduced:
            common = numerator.gcd(denominator)
            if common.total_degree() > 0:
                numerator, denominator = numerator // common, denominator // common
        scalar = denominator.leading_coefficient()
        self.numerator = numerator / scalar
        self.denominator = denominator / scalar

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Rat3) else Rat3(value)

    def __add__(self, other):
        other = Rat3.coerce(other)
        if self.denominator == ONE and other.denominator == ONE:
            return Rat3(self.numerator + other.numerator, reduced=True)
        return Rat3(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    __radd__ = __add__

    def __neg__(self):
        return Rat3(-self.numerator, self.denominator, reduced=True)

    def __sub__(self, other):
        return self + (-Rat3.coerce(other))

    def __rsub__(self, other):
        return Rat3.coerce(other) - self

    def __mul__(self, other):
        other = Rat3.coerce(other)
        if not self or not other:
            return Rat3()
        if self.denominator == ONE and other.denominator == ONE:
            return Rat3(self.numerator * other.numerator, reduced=True)
        left_common = self.numerator.gcd(other.denominator)
        right_common = other.numerator.gcd(self.denominator)
        return Rat3(
            (self.numerator // left_common) * (other.numerator // right_common),
            (self.denominator // right_common) * (other.denominator // left_common),
            reduced=True,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.numerator:
            raise ZeroDivisionError
        Rat3.inverse_count += 1
        return Rat3(self.denominator, self.numerator, reduced=True)

    def __truediv__(self, other):
        return self * Rat3.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Rat3.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = Rat3(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.numerator)

    def __eq__(self, other):
        other = Rat3.coerce(other)
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __repr__(self):
        return f"Rat3(({self.numerator})/({self.denominator}))"


def polynomial_summary(value):
    canonical = tuple(
        (monomial, str(coefficient))
        for monomial, coefficient in sorted(value.to_dict().items())
    )
    return (
        value.total_degree(),
        len(canonical),
        sha256(repr(canonical).encode()).hexdigest(),
    )


def choose_b_local_pivot(row):
    """Prefer a first-band chart whose divisor is a unit on B3 off U,V,H."""
    candidates = []
    for variable, coefficient in row.items():
        coordinate = r.scalar_coordinate(coefficient)
        if coordinate is None:
            continue
        resultant = B3.resultant(coordinate.numerator, 0)
        if not resultant:
            residual_degree = 10**9
        else:
            _, factors = resultant.factor()
            residual_degree = sum(
                factor.total_degree() * multiplicity
                for factor, multiplicity in factors
                if factor not in (U, V, P3)
            )
        candidates.append((
            residual_degree,
            coordinate.numerator.total_degree(),
            coordinate.denominator.total_degree(),
            len(str(coordinate.numerator)) + len(str(coordinate.denominator)),
            variable,
        ))
    assert candidates, "no scalar-coefficient B-local pivot candidate"
    return min(candidates)[-1]


def center_coordinates():
    if STRATUM == "generic":
        return Rat3(C), Rat3(V), Rat3(U), "C,V,U independent"
    if STRATUM == "u-zero":
        return Rat3(C), Rat3(V), Rat3(0), "U=0 over Q(C,V)"
    if STRATUM == "h-zero":
        return Rat3(3*U**2), Rat3(V), Rat3(U), "C=3U^2 over Q(V,U)"
    if STRATUM == "v-zero":
        return Rat3(C), Rat3(0), Rat3(U), "V=0 over Q(C,U)"
    if STRATUM == "u-h-zero":
        return Rat3(0), Rat3(V), Rat3(0), "C=U=0 over Q(V)"
    if STRATUM == "origin":
        return Rat3(0), Rat3(0), Rat3(0), "C=V=U=0"
    if STRATUM == "v-h-zero":
        return Rat3(3*U**2), Rat3(0), Rat3(U), "V=H=0 over Q(U)"
    if STRATUM == "v-cplus1-zero":
        return Rat3(-U**2), Rat3(0), Rat3(U), "V=C+U^2=0 over Q(U)"
    if STRATUM == "v-cplus5-zero":
        return Rat3(-5*U**2), Rat3(0), Rat3(U), "V=C+5U^2=0 over Q(U)"
    raise AssertionError(STRATUM)


def factor_transport(rows):
    pivots, records, events = {}, [], []
    determinant = Rat3(1)
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: Rat3(value) for variable, value in original_row.items()}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            for variable, coefficient in pivots[pivot].items():
                value = row.get(variable, Rat3()) - multiplier * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        determinant *= lead
        if lead.numerator.total_degree() or lead.denominator.total_degree():
            events.append((row_index, key, pivot, lead.numerator, lead.denominator))
        inverse = lead.inverse()
        pivots[pivot] = {
            variable: coefficient * inverse
            for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 250 == 0:
            print(
                f"trivariate_transport rows={row_index};pivots={len(pivots)};"
                f"events={len(events)}",
                flush=True,
            )
    return pivots, records, events, determinant


class RTShim:
    Rat = Rat3

    @staticmethod
    def rational(value):
        return r.cp.rt.rational(value)


class CPShim:
    rt = RTShim
    qd = r.cp.qd
    K = r.cp.K
    E = r.cp.E
    Frac = r.cp.Frac
    fast_evec = r.cp.fast_evec


FIELD = r.cp.fast_efield.EFieldFactory(CPShim)
EField = r.cp.fast_efield.EField


class E3:
    __slots__ = ("value",)

    def __init__(self, value=0):
        if isinstance(value, E3):
            self.value = value.value
        elif isinstance(value, EField):
            assert value.factory is FIELD
            self.value = value
        elif isinstance(value, Rat3):
            self.value = FIELD.scalar(value)
        else:
            self.value = FIELD.from_e(r.cp.E(value))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, E3) else E3(value)

    def __add__(self, other):
        return E3(self.value + E3.coerce(other).value)

    __radd__ = __add__

    def __neg__(self):
        return E3(-self.value)

    def __sub__(self, other):
        return self + (-E3.coerce(other))

    def __rsub__(self, other):
        return E3.coerce(other) - self

    def __mul__(self, other):
        return E3(self.value * E3.coerce(other).value)

    __rmul__ = __mul__

    def inverse(self):
        result = E3(self.value.inverse())
        assert self * result == E3(1)
        return result

    def __truediv__(self, other):
        return self * E3.coerce(other).inverse()

    def __rtruediv__(self, other):
        return E3.coerce(other) / self

    def __pow__(self, exponent):
        return E3(self.value**exponent)

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == E3.coerce(other).value


def configure():
    r.t.CTX = CTX
    r.t.C, r.t.U = C, U
    r.t.ZERO, r.t.ONE = ZERO, ONE
    r.t.Rat2 = Rat3
    r.t.factor = factor_transport
    r.b.FIELD = FIELD
    r.b.EField = EField
    r.b.E2 = E3
    r.E2 = E3
    r.REVERSE_PIVOTS = False
    r.SPARSE_PIVOTS = False
    r.B_LOCAL_PIVOTS = False
    r.b.REVERSE_PIVOTS = False
    r.b.SPARSE_PIVOTS = False
    r.b.B_LOCAL_PIVOTS = False
    if B_LOCAL3:
        r.choose_new_pivot = choose_b_local_pivot


def exact_source_replay(polynomial, remainder, relations, first_rows):
    source_identity = {}
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_identity = r.add(
            source_identity,
            r.multiply(relation, r.source_polynomial(row, rhs)),
        )
    source_target = r.add(polynomial, remainder, E3(-1))
    assert r.clean(source_identity) == r.clean(source_target)
    assert r.clean(source_identity) != r.clean(r.add(source_target, {(): E3(1)}))


def emit_first_incompatibilities(incompatibilities, first_rows, events):
    """Emit exact original-row certificates and their full localization."""
    transport_chart = r.transport_chart_polynomial(events)
    first_source_denominator = r.denominator_lcm(
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    )
    print(f"transport_chart_denominator=({transport_chart})")
    print(f"transport_chart_denominator_factor={transport_chart.factor()}")
    print(f"first_source_denominator=({first_source_denominator})")
    print(f"first_source_denominator_factor={first_source_denominator.factor()}")
    whole_stratum = False
    for index, (row_index, key, residual, combination) in enumerate(
        incompatibilities
    ):
        residual_denominator, residual_gcd = r.cleared_scalar_gcd(residual)
        combination_denominator = r.denominator_lcm(combination.values())
        certificate_chart = r.monic_polynomial(
            transport_chart
            * first_source_denominator
            * combination_denominator
            * residual_denominator
        )
        exact_combination = tuple(
            (
                source_index,
                first_rows[source_index][0],
                r.scalar_exact(coefficient),
            )
            for source_index, coefficient in sorted(combination.items())
        )
        residual_unit = residual_gcd.total_degree() == 0
        this_whole_stratum = (
            residual_unit and certificate_chart.total_degree() == 0
        )
        whole_stratum = whole_stratum or this_whole_stratum
        print(f"first_incompatibility[{index}]_row_index={row_index}")
        print(f"first_incompatibility[{index}]_key={key}")
        print(
            f"first_incompatibility[{index}]_residual_sha256="
            f"{r.scalar_digest(residual)}"
        )
        print(
            f"first_incompatibility[{index}]_residual_coordinates="
            f"{r.scalar_exact(residual)}"
        )
        print(
            f"first_incompatibility[{index}]_source_row_count="
            f"{len(combination)}"
        )
        print(
            f"first_incompatibility[{index}]_source_certificate_sha256="
            f"{sha256(repr(exact_combination).encode()).hexdigest()}"
        )
        print(
            f"first_incompatibility[{index}]_source_certificate_exact="
            f"{exact_combination}"
        )
        print(
            f"first_incompatibility[{index}]_residual_denominator="
            f"({residual_denominator})"
        )
        print(
            f"first_incompatibility[{index}]_cleared_numerator_gcd="
            f"({residual_gcd})"
        )
        print(
            f"first_incompatibility[{index}]_combination_denominator="
            f"({combination_denominator})"
        )
        print(
            f"first_incompatibility[{index}]_certificate_chart_denominator="
            f"({certificate_chart})"
        )
        print(
            f"first_incompatibility[{index}]_certificate_chart_factor="
            f"{certificate_chart.factor()}"
        )
        print(
            f"first_incompatibility[{index}]_residual_unit_on_chart="
            f"{str(residual_unit).lower()}"
        )
        print(
            f"first_incompatibility[{index}]_whole_stratum_empty="
            f"{str(this_whole_stratum).lower()}"
        )
    print("first_incompatibility_original_row_replay=true")
    print("P12_compile_skipped_first_band_empty=true")
    print("stratum_localization_killed=true")
    print(f"whole_stratum_killed={str(whole_stratum).lower()}")
    print("full_three_center_family_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-C1-C2-C3-FIRST-BAND-INCONSISTENT-STRATUM PASS")


def rat_denominator_lcm(values):
    out = ONE
    for value in values:
        denominator = Rat3.coerce(value).denominator
        common = out.gcd(denominator)
        out = (out // common) * denominator
        if out:
            out /= out.leading_coefficient()
    return out


def transport_source_combination(records, target_index):
    """Lift one dependent transport row through the exact raw echelon."""
    pivot_record = {
        pivot: row_index
        for row_index, (_, kind, pivot, _, _) in enumerate(records)
        if kind == "pivot"
    }
    needed, stack = {target_index}, [target_index]
    while stack:
        row_index = stack.pop()
        for old_pivot, _ in records[row_index][4]:
            old_index = pivot_record[old_pivot]
            assert old_index < row_index
            if old_index not in needed:
                needed.add(old_index)
                stack.append(old_index)
    combinations = {}
    for row_index in sorted(needed):
        _, kind, _, lead, factors = records[row_index]
        combination = {row_index: Rat3(1)}
        for old_pivot, multiplier in factors:
            old_combination = combinations[pivot_record[old_pivot]]
            for source_index, coefficient in old_combination.items():
                value = combination.get(source_index, Rat3()) - multiplier*coefficient
                if value:
                    combination[source_index] = value
                else:
                    combination.pop(source_index, None)
        if kind == "pivot":
            inverse = lead.inverse()
            combination = {
                source_index: coefficient*inverse
                for source_index, coefficient in combination.items()
            }
        combinations[row_index] = combination
    return combinations[target_index], len(needed)


def transport_incompatibility_records(rows, records):
    pivot_rhs, out = {}, []
    for row_index, ((source_key, _, _), record) in enumerate(zip(rows, records)):
        key, kind, pivot, lead, factors = record
        assert source_key == key
        value = r.t.source_vector(key)
        for old_pivot, multiplier in factors:
            value = r.t.vector_sub(
                value, r.t.vector_scale(pivot_rhs[old_pivot], multiplier)
            )
        if kind == "pivot":
            pivot_rhs[pivot] = r.t.vector_scale(value, lead.inverse())
        elif any(value):
            out.append((row_index, key, value))
    return out


def replay_transport_combination(rows, combination):
    matrix, rhs = {}, None
    for source_index, multiplier in combination.items():
        key, row, _ = rows[source_index]
        for variable, coefficient in row.items():
            value = matrix.get(variable, Rat3()) + multiplier*Rat3.coerce(coefficient)
            if value:
                matrix[variable] = value
            else:
                matrix.pop(variable, None)
        source_rhs = r.t.source_vector(key)
        if rhs is None:
            rhs = tuple(Rat3() for _ in source_rhs)
        rhs = tuple(
            old + multiplier*coordinate
            for old, coordinate in zip(rhs, source_rhs)
        )
    return matrix, rhs


def emit_transport_incompatibilities(rows, records, events, compatibility):
    """Emit exact original-row witnesses for an empty transport stratum."""
    indexed = transport_incompatibility_records(rows, records)
    assert tuple((key, value) for _, key, value in indexed) == tuple(compatibility)
    transport_chart = r.transport_chart_polynomial(events)
    print(f"transport_chart_denominator=({transport_chart})")
    print(f"transport_chart_denominator_factor={transport_chart.factor()}")
    whole_stratum = False
    for index, (row_index, key, residual) in enumerate(indexed):
        combination, ancestor_count = transport_source_combination(
            records, row_index
        )
        matrix_replay, rhs_replay = replay_transport_combination(rows, combination)
        assert not matrix_replay
        assert rhs_replay == residual
        exact_combination = tuple(
            (
                source_index,
                rows[source_index][0],
                str(coefficient.numerator),
                str(coefficient.denominator),
            )
            for source_index, coefficient in sorted(combination.items())
        )
        combination_denominator = rat_denominator_lcm(combination.values())
        residual_denominator = rat_denominator_lcm(residual)
        cleared = [
            value.numerator*(residual_denominator // value.denominator)
            for value in residual if value
        ]
        assert cleared
        residual_gcd = cleared[0]
        for numerator in cleared[1:]:
            residual_gcd = residual_gcd.gcd(numerator)
        residual_gcd = r.monic_polynomial(residual_gcd)
        certificate_chart = r.monic_polynomial(
            transport_chart*combination_denominator*residual_denominator
        )
        residual_unit = residual_gcd.total_degree() == 0
        this_whole_stratum = (
            residual_unit and certificate_chart.total_degree() == 0
        )
        whole_stratum = whole_stratum or this_whole_stratum
        negative = dict(combination)
        first_source = min(negative)
        negative[first_source] = negative[first_source] + Rat3(1)
        bad_matrix, bad_rhs = replay_transport_combination(rows, negative)
        assert bad_matrix or bad_rhs != residual
        residual_exact = tuple(
            (str(value.numerator), str(value.denominator)) for value in residual
        )
        print(f"transport_incompatibility[{index}]_row_index={row_index}")
        print(f"transport_incompatibility[{index}]_key={key}")
        print(f"transport_incompatibility[{index}]_ancestor_count={ancestor_count}")
        print(f"transport_incompatibility[{index}]_source_row_count={len(combination)}")
        print(
            f"transport_incompatibility[{index}]_source_certificate_sha256="
            f"{sha256(repr(exact_combination).encode()).hexdigest()}"
        )
        print(
            f"transport_incompatibility[{index}]_source_certificate_exact="
            f"{exact_combination}"
        )
        print(
            f"transport_incompatibility[{index}]_residual_exact="
            f"{residual_exact}"
        )
        print(
            f"transport_incompatibility[{index}]_residual_sha256="
            f"{sha256(repr(residual_exact).encode()).hexdigest()}"
        )
        print(
            f"transport_incompatibility[{index}]_combination_denominator="
            f"({combination_denominator})"
        )
        print(
            f"transport_incompatibility[{index}]_residual_denominator="
            f"({residual_denominator})"
        )
        print(
            f"transport_incompatibility[{index}]_cleared_numerator_gcd="
            f"({residual_gcd})"
        )
        print(
            f"transport_incompatibility[{index}]_certificate_chart_denominator="
            f"({certificate_chart})"
        )
        print(
            f"transport_incompatibility[{index}]_residual_unit_on_chart="
            f"{str(residual_unit).lower()}"
        )
        print(
            f"transport_incompatibility[{index}]_whole_stratum_empty="
            f"{str(this_whole_stratum).lower()}"
        )
        print(f"transport_incompatibility[{index}]_plus_one_negative_control=true")
    print("transport_incompatibility_original_row_replay=true")
    print(f"whole_stratum_killed={str(whole_stratum).lower()}")
    print("first_band_and_P12_skipped_transport_empty=true")
    print("full_three_center_family_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-C1-C2-C3-TRANSPORT-INCONSISTENT-STRATUM PASS")


def main():
    configure()
    print(
        "trivariate_first_pivot_order="
        + ("B3-local-scalar" if B_LOCAL3 else "ascending"),
        flush=True,
    )
    center_c, center_v, center_u, center_label = center_coordinates()
    print(f"center_stratum={center_label}", flush=True)
    r.fb.CENTER = (center_c, center_v, center_u)
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)}, r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN
    )
    ng, rows_g = r.fb.build_transport(
        25, 100, 5, {1: r.b.Q(1), 25: r.b.Q(1)},
        r.fb.F1_G_PATTERN, r.fb.POLE_G_PATTERN,
    )
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (
            ('g',) + key,
            {nf + variable: coefficient for variable, coefficient in row.items()},
            rhs,
        )
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in rows if row[0][1] != 'X'] + [
        row for row in rows if row[0][1] == 'X'
    ]
    transport_pivots, records, events, transport_determinant = r.t.factor(ordered)
    pivot_rhs, compatibility = r.t.propagate(ordered, records)
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}", flush=True)
    print(f"transport_compatibility_count={len(compatibility)}", flush=True)
    if compatibility:
        emit_transport_incompatibilities(
            ordered, records, events, compatibility
        )
        return
    assert len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("TD6 trivariate transport PASS", flush=True)
    print(f"transport_event_count={len(events)}")
    for index, (row_index, key, pivot, numerator, denominator) in enumerate(events):
        print(
            f"transport_event[{index}]={row_index},{key},{pivot};"
            f"num=({numerator});den=({denominator})"
        )
    print(f"transport_minor_num_summary={polynomial_summary(transport_determinant.numerator)}")
    print(f"transport_minor_den_summary={polynomial_summary(transport_determinant.denominator)}")
    print("transport_global_factorization_deferred=true", flush=True)

    bands = {}
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
                forms.append(r.b.restrict_row(
                    row, transport_pivots, pivot_rhs, free_parameter
                ))
            bands[(owner, exponent)] = forms

    r.qd.Dual = E3
    r.qd.Q_PRIME = {0: E3(1), 24: E3(25)}
    first_rows = r.qd.pack(
        'X-2', r.qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    first_pivots, first_factors, incompatibilities = r.solve_cert(first_rows)
    if STRATUM == "generic":
        assert not incompatibilities
        assert len(first_pivots) == 38
    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_incompatibility_count={len(incompatibilities)}")
    first_determinant = Rat3(1)
    for _, _, _, lead in first_factors:
        coordinate = r.scalar_coordinate(lead)
        assert coordinate is not None
        first_determinant *= coordinate
    print(f"first_minor_num_summary={polynomial_summary(first_determinant.numerator)}")
    print(f"first_minor_den_summary={polynomial_summary(first_determinant.denominator)}")
    print("first_global_factorization_deferred=true", flush=True)
    if incompatibilities:
        emit_first_incompatibilities(incompatibilities, first_rows, events)
        return

    raw = r.qd.compile_current(
        *[bands[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands[('g', exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial_value = {
        monomial: E3.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    assert max(map(len, polynomial_value)) == 2
    if STRATUM == "generic":
        assert len(polynomial_value) == 2893
    print("TD6 trivariate genuine P12 PASS", flush=True)
    remainder, quotients = r.divide(polynomial_value, first_pivots)
    relations = r.lift_relations(quotients, first_pivots, len(first_rows))
    exact_source_replay(polynomial_value, remainder, relations, first_rows)
    S = E3(r.qd.uniform.S_FIELD)
    k = E3(252) - 342*S + 144*S**2 - 36*S**3
    expected = -k / 50
    expected_remainder = remainder == {(): expected}
    constant_unit = False
    if set(remainder) == {()} and remainder[()]:
        inverse = remainder[()].inverse()
        assert remainder[()] * inverse == E3(1)
        constant_unit = True
        print(f"remainder_inverse_sha256={r.scalar_digest(inverse)}")

    relations_denominator = r.denominator_lcm(r.polynomial_values(relations))
    raw_denominator = r.denominator_lcm(polynomial_value.values())
    first_denominator = r.denominator_lcm(
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    )
    termwise_denominator = relations_denominator * first_denominator
    termwise_denominator /= termwise_denominator.leading_coefficient()
    source_nonzero_rows = sum(bool(relation) for relation in relations)
    source_multiplier_terms = sum(len(relation) for relation in relations)
    if B_LOCAL3:
        expected_relation_denominator = U**2*T3/4
        expected_termwise_denominator = U**3*(C-3*U**2)*T3/4
        print(
            "B3_local_precharged_relation_denominator_match="
            f"{str(relations_denominator == expected_relation_denominator).lower()}"
        )
        print(
            "B3_local_precharged_termwise_denominator_match="
            f"{str(termwise_denominator == expected_termwise_denominator).lower()}"
        )
        print(
            "B3_local_precharged_source_count_match="
            f"{str((source_nonzero_rows, source_multiplier_terms) == (28, 1564)).lower()}"
        )
    print(f"raw_terms={len(polynomial_value)}")
    print(f"raw_sha256={r.polynomial_digest(polynomial_value)}")
    print(f"remainder_terms={len(remainder)}")
    print(f"remainder_degree={max(map(len, remainder), default=-1)}")
    print(f"remainder_sha256={r.polynomial_digest(remainder)}")
    print(f"expected_sha256={r.scalar_digest(expected)}")
    print(f"remainder_is_expected_constant={str(expected_remainder).lower()}")
    print(f"remainder_is_constant_unit={str(constant_unit).lower()}")
    print(f"source_nonzero_rows={source_nonzero_rows}")
    print(f"source_multiplier_terms={source_multiplier_terms}")
    print("source_relation_original_row_replay=true")
    print("source_relation_plus_one_negative_control=true")
    print(f"raw_denominator=({raw_denominator})")
    print(f"raw_denominator_summary={polynomial_summary(raw_denominator)}")
    print(f"first_denominator=({first_denominator})")
    print(f"first_denominator_summary={polynomial_summary(first_denominator)}")
    print(f"relation_denominator=({relations_denominator})")
    print(f"relation_denominator_summary={polynomial_summary(relations_denominator)}")
    print(f"termwise_denominator=({termwise_denominator})")
    print(f"termwise_denominator_summary={polynomial_summary(termwise_denominator)}")
    print("denominator_factorizations_deferred=" + str(not B_LOCAL3).lower())
    if B_LOCAL3:
        charged_resultant = B3.resultant(T3, 0)
        assert charged_resultant == 64*V**4*U**10
        assert B3.subs({"U": 0}) == V**4
        actual_resultant = B3.resultant(relations_denominator, 0)
        assert actual_resultant
        _, actual_resultant_factors = actual_resultant.factor()
        unit_off_uhv = all(
            factor in (U, V)
            for factor, _ in actual_resultant_factors
        )
        print(f"relation_denominator_factor={relations_denominator.factor()}")
        print(f"termwise_denominator_factor={termwise_denominator.factor()}")
        print(f"B3_local_T3_resultant=({charged_resultant})")
        print(f"B3_local_actual_resultant=({actual_resultant})")
        print(f"B3_local_actual_resultant_factor={actual_resultant.factor()}")
        print(f"B3_at_U_zero=({B3.subs({'U': 0})})")
        print(
            "B3_local_denominator_unit_off_UHV="
            f"{str(unit_off_uhv).lower()}"
        )
    certificate_chart = r.monic_polynomial(
        r.transport_chart_polynomial(events)
        * raw_denominator
        * first_denominator
        * termwise_denominator
    )
    whole_stratum_killed = constant_unit and certificate_chart.total_degree() == 0
    print(f"certificate_chart_denominator=({certificate_chart})")
    print(f"certificate_chart_denominator_factor={certificate_chart.factor()}")
    print(f"stratum_localization_killed={str(constant_unit).lower()}")
    print(f"whole_stratum_killed={str(whole_stratum_killed).lower()}")
    print(f"Rat3_inverse_count={Rat3.inverse_count}")
    print(f"generic_open_killed={str(constant_unit and STRATUM == 'generic').lower()}")
    print("full_three_center_family_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print(
        "TD6-C1-C2-C3-TRIVARIATE-GENERIC PASS"
        if STRATUM == "generic"
        else "TD6-C1-C2-C3-RAW-STRATUM PASS"
    )


if __name__ == '__main__':
    main()
