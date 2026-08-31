#!/usr/bin/env python3
"""Exact next-rung delta-sequence/S4 replay.

This replay pins and reuses the already sealed arithmetic/permutation core in
``block_descent_a1_genus_ladder_s4_replay.py``.  It adds two independent
pieces:

* a recursive delta-sequence -> signed iterated-satellite braid compiler for
  arbitrary cabling winding; and
* an exact S4 transposition-coloring counter which factors S4 through
  ``V4 -> S4 -> S3``.  Fox 3-colorings are solved linearly over F3 and their
  lifts are solved affinely over F2, avoiding a 6^strands search.

The compiler is fail-closed against closure permutation, recursive Alexander
determinant, selected full Alexander-polynomial, direct 6^n coloring, and
signed/framing controls before its new counts are consumed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys


PINNED_CORE_SHA256 = "a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a"
CORE_PATH = Path(__file__).with_name("block_descent_a1_genus_ladder_s4_replay.py")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_core():
    source = CORE_PATH.read_bytes()
    require(hashlib.sha256(source).hexdigest() == PINNED_CORE_SHA256, "pinned genus-ladder core")
    specification = importlib.util.spec_from_file_location("_pinned_genus_ladder_core", CORE_PATH)
    require(specification is not None and specification.loader is not None, "core import specification")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


CORE = load_core()
Permutation = tuple[int, ...]
BraidWord = tuple[int, ...]


def writhe(word: BraidWord) -> int:
    return sum(1 if generator > 0 else -1 for generator in word)


def torus_word(strands: int, exponent: int) -> BraidWord:
    require(strands >= 2, "nontrivial torus braid")
    delta = tuple(range(1, strands))
    return CORE.signed_power(delta, exponent)


def offset_word(word: BraidWord, offset: int) -> BraidWord:
    return tuple((1 if generator > 0 else -1) * (abs(generator) + offset) for generator in word)


def parallel_cable_word(companion_strands: int, winding: int, word: BraidWord) -> BraidWord:
    """Replace every companion strand by ``winding`` blackboard parallels."""

    require(companion_strands >= 1 and winding >= 2, "parallel-cable dimensions")
    switch = CORE.block_switch_word(winding)
    result: list[int] = []
    for generator in word:
        index = abs(generator) - 1
        require(index + 1 < companion_strands, "companion generator range")
        positive = offset_word(switch, index * winding)
        result.extend(positive if generator > 0 else CORE.inverse_word(positive))
    return tuple(result)


def satellite_word(
    companion_strands: int,
    companion_word: BraidWord,
    winding: int,
    meridional: int,
) -> tuple[int, BraidWord]:
    """Zero-framed C_(winding,meridional) of a closed companion braid.

    Blackboard parallelization contributes ``winding*writhe(companion)`` to
    the pattern meridian.  The internal torus word on the first block removes
    precisely that contribution.
    """

    require(math.gcd(winding, meridional) == 1, "cable is a knot")
    parallel = parallel_cable_word(companion_strands, winding, companion_word)
    correction = meridional - winding * writhe(companion_word)
    pattern = torus_word(winding, correction)
    return companion_strands * winding, parallel + pattern


def prefix_gcd(sequence: tuple[int, ...]) -> int:
    result = sequence[0]
    for value in sequence[1:]:
        result = math.gcd(result, value)
    return result


def compile_delta_sequence(
    sequence: tuple[int, ...], signs: tuple[int, ...] | None = None
) -> tuple[int, BraidWord]:
    """Compile a reduced delta sequence to its signed iterated cable braid.

    ``signs[0]`` mirrors the base torus exponent and each later sign chooses
    the corresponding cable meridian.  All-positive signs are the canonical
    algebraic convention; exhausting signs is a dictionary-robustness check.
    """

    require(CORE.is_delta_sequence(sequence, drop_freeness=False, drop_ordering=False), "reduced delta sequence")
    stages = len(sequence) - 1
    if signs is None:
        signs = (1,) * stages
    require(len(signs) == stages and all(sign in (-1, 1) for sign in signs), "one sign per torus/cable stage")
    if len(sequence) == 2:
        strands = sequence[1]
        require(strands >= 2 and math.gcd(sequence[0], sequence[1]) == 1, "primitive base torus knot")
        return strands, torus_word(strands, signs[0] * sequence[0])
    winding = prefix_gcd(sequence[:-1])
    require(winding >= 2 and math.gcd(winding, sequence[-1]) == 1, "primitive final cable")
    normalized_prefix = tuple(value // winding for value in sequence[:-1])
    companion_strands, companion_word = compile_delta_sequence(normalized_prefix, signs[:-1])
    return satellite_word(
        companion_strands,
        companion_word,
        winding,
        signs[-1] * sequence[-1],
    )


def torus_determinant(first: int, second: int) -> int:
    first, second = abs(first), abs(second)
    require(math.gcd(first, second) == 1, "primitive torus knot")
    if first % 2 == 0:
        return second
    if second % 2 == 0:
        return first
    return 1


def recursive_alexander_determinant(sequence: tuple[int, ...]) -> int:
    if len(sequence) == 2:
        return torus_determinant(sequence[1], sequence[0])
    winding = prefix_gcd(sequence[:-1])
    pattern = torus_determinant(winding, sequence[-1])
    companion = recursive_alexander_determinant(tuple(value // winding for value in sequence[:-1]))
    return pattern * (companion if winding % 2 else 1)


def dense_polynomial(values: dict[int, int]) -> list[int]:
    maximum = max(values, default=0)
    result = [values.get(power, 0) for power in range(maximum + 1)]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for left_power, left_value in enumerate(left):
        for right_power, right_value in enumerate(right):
            result[left_power + right_power] += left_value * right_value
    return dense_polynomial(dict(enumerate(result)))


def polynomial_divide_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    require(denominator and denominator[-1] in (-1, 1), "monic exact polynomial divisor")
    remainder = numerator[:]
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    while len(remainder) >= len(denominator) and any(remainder):
        shift = len(remainder) - len(denominator)
        require(remainder[-1] % denominator[-1] == 0, "exact polynomial leading division")
        coefficient = remainder[-1] // denominator[-1]
        quotient[shift] += coefficient
        for power, value in enumerate(denominator):
            remainder[shift + power] -= coefficient * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    require(not any(remainder), "exact polynomial remainder")
    return dense_polynomial(dict(enumerate(quotient)))


def torus_alexander(first: int, second: int):
    first, second = abs(first), abs(second)
    require(math.gcd(first, second) == 1, "primitive torus Alexander polynomial")
    numerator = polynomial_multiply(
        dense_polynomial({0: 1, first * second: -1}),
        dense_polynomial({0: 1, 1: -1}),
    )
    denominator = polynomial_multiply(
        dense_polynomial({0: 1, first: -1}),
        dense_polynomial({0: 1, second: -1}),
    )
    quotient = polynomial_divide_exact(numerator, denominator)
    return CORE.Laurent.from_dict(dict(enumerate(quotient)))


def recursive_alexander_polynomial(sequence: tuple[int, ...]):
    if len(sequence) == 2:
        return torus_alexander(sequence[1], sequence[0])
    winding = prefix_gcd(sequence[:-1])
    prefix = tuple(value // winding for value in sequence[:-1])
    return torus_alexander(winding, sequence[-1]) * CORE.substitute_power(
        recursive_alexander_polynomial(prefix), winding
    )


def integer_determinant(matrix: list[list[int]]) -> int:
    """Fraction-free Bareiss determinant over Z."""

    size = len(matrix)
    if size == 0:
        return 1
    values = [row[:] for row in matrix]
    sign = 1
    denominator = 1
    for pivot_index in range(size - 1):
        if values[pivot_index][pivot_index] == 0:
            swap = next((row for row in range(pivot_index + 1, size) if values[row][pivot_index]), None)
            if swap is None:
                return 0
            values[pivot_index], values[swap] = values[swap], values[pivot_index]
            sign = -sign
        pivot = values[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = values[row][column] * pivot - values[row][pivot_index] * values[pivot_index][column]
                require(numerator % denominator == 0, "Bareiss exact division")
                values[row][column] = numerator // denominator
        denominator = pivot
        for row in range(pivot_index + 1, size):
            values[row][pivot_index] = 0
    return sign * values[-1][-1]


def integer_matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[row][middle] * right[middle][column] for middle in range(len(right))) for column in range(len(right[0]))]
        for row in range(len(left))
    ]


def burau_at_minus_one(strands: int, word: BraidWord) -> list[list[int]]:
    matrix = [[1 if row == column else 0 for column in range(strands)] for row in range(strands)]
    for generator in word:
        index = abs(generator) - 1
        block = ((2, -1), (1, 0)) if generator > 0 else ((0, 1), (-1, 2))
        factor = [[1 if row == column else 0 for column in range(strands)] for row in range(strands)]
        for row_offset in range(2):
            for column_offset in range(2):
                factor[index + row_offset][index + column_offset] = block[row_offset][column_offset]
        matrix = integer_matrix_multiply(matrix, factor)
    return [
        [matrix[row][column] - matrix[strands - 1][column] for column in range(strands - 1)]
        for row in range(strands - 1)
    ]


def braid_alexander_determinant(strands: int, word: BraidWord) -> int:
    reduced = burau_at_minus_one(strands, word)
    difference = [
        [(1 if row == column else 0) - reduced[row][column] for column in range(strands - 1)]
        for row in range(strands - 1)
    ]
    numerator = 2 * integer_determinant(difference)
    denominator = 1 - (-1) ** strands
    if denominator:
        require(numerator % denominator == 0, "Alexander numerator division at -1")
        return abs(numerator // denominator)
    # For even strand count both numerator and 1-t^n vanish at -1.  The
    # determinant of a knot can instead be read from any odd Markov
    # stabilization, which preserves closure and Alexander polynomial.
    stabilized = word + (strands,)
    return braid_alexander_determinant(strands + 1, stabilized)


def partitions_of_four() -> tuple[frozenset[frozenset[int]], ...]:
    return (
        frozenset((frozenset((0, 1)), frozenset((2, 3)))),
        frozenset((frozenset((0, 2)), frozenset((1, 3)))),
        frozenset((frozenset((0, 3)), frozenset((1, 2)))),
    )


PARTITIONS = partitions_of_four()


def quotient_action(permutation: Permutation) -> Permutation:
    images = []
    for partition in PARTITIONS:
        image = frozenset(frozenset(permutation[value] for value in pair) for pair in partition)
        images.append(PARTITIONS.index(image))
    return tuple(images)


def transposition_coordinates() -> tuple[dict[Permutation, tuple[int, int]], dict[tuple[int, int], Permutation]]:
    fibers: dict[int, list[Permutation]] = {color: [] for color in range(3)}
    for permutation in CORE.TRANSPOSITIONS:
        quotient = quotient_action(permutation)
        fixed = [index for index, image in enumerate(quotient) if index == image]
        require(len(fixed) == 1, "S4 transposition maps to S3 transposition")
        fibers[fixed[0]].append(permutation)
    require(all(len(fiber) == 2 for fiber in fibers.values()), "two transposition lifts per quotient color")
    forward: dict[Permutation, tuple[int, int]] = {}
    backward: dict[tuple[int, int], Permutation] = {}
    for color, fiber in fibers.items():
        for bit, permutation in enumerate(sorted(fiber)):
            forward[permutation] = (color, bit)
            backward[(color, bit)] = permutation
    return forward, backward


TRANS_TO_COORD, COORD_TO_TRANS = transposition_coordinates()


def affine_conjugation_table() -> dict[tuple[int, int], tuple[int, int, int]]:
    """Return alpha,beta,gamma with bit(A B A)=alpha*a+beta*b+gamma."""

    table: dict[tuple[int, int], tuple[int, int, int]] = {}
    for first_color in range(3):
        for second_color in range(3):
            values: dict[tuple[int, int], int] = {}
            output_colors = set()
            for first_bit in range(2):
                for second_bit in range(2):
                    first = COORD_TO_TRANS[(first_color, first_bit)]
                    second = COORD_TO_TRANS[(second_color, second_bit)]
                    output = CORE.conjugate(first, second)
                    output_color, output_bit = TRANS_TO_COORD[output]
                    output_colors.add(output_color)
                    values[(first_bit, second_bit)] = output_bit
            require(output_colors == {(2 * first_color - second_color) % 3}, "Fox quotient conjugation")
            gamma = values[(0, 0)]
            alpha = values[(1, 0)] ^ gamma
            beta = values[(0, 1)] ^ gamma
            require(
                all(values[(a, b)] == ((alpha & a) ^ (beta & b) ^ gamma) for a in range(2) for b in range(2)),
                "affine V4 lift table",
            )
            table[(first_color, second_color)] = (alpha, beta, gamma)
    return table


AFFINE_CONJUGATION = affine_conjugation_table()


def modular_rref(matrix: list[list[int]], modulus: int) -> tuple[list[list[int]], list[int]]:
    values = [[entry % modulus for entry in row] for row in matrix]
    if not values:
        return values, []
    rows, columns = len(values), len(values[0])
    pivots: list[int] = []
    pivot_row = 0
    for column in range(columns):
        selected = next((row for row in range(pivot_row, rows) if values[row][column]), None)
        if selected is None:
            continue
        values[pivot_row], values[selected] = values[selected], values[pivot_row]
        inverse = pow(values[pivot_row][column], -1, modulus)
        values[pivot_row] = [(entry * inverse) % modulus for entry in values[pivot_row]]
        for row in range(rows):
            if row == pivot_row or values[row][column] == 0:
                continue
            factor = values[row][column]
            values[row] = [(left - factor * right) % modulus for left, right in zip(values[row], values[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return values, pivots


def fox_action_vector(colors: tuple[int, ...], generator: int) -> tuple[int, ...]:
    index = abs(generator) - 1
    result = list(colors)
    first, second = result[index], result[index + 1]
    if generator > 0:
        result[index], result[index + 1] = (2 * first - second) % 3, first
    else:
        result[index], result[index + 1] = second, (2 * second - first) % 3
    return tuple(result)


def fox_fixed_basis(strands: int, word: BraidWord) -> tuple[tuple[int, ...], ...]:
    columns: list[tuple[int, ...]] = []
    for column in range(strands):
        unit = tuple(1 if index == column else 0 for index in range(strands))
        result = unit
        for generator in word:
            result = fox_action_vector(result, generator)
        columns.append(result)
    equations = [
        [(columns[column][row] - (1 if row == column else 0)) % 3 for column in range(strands)]
        for row in range(strands)
    ]
    rref, pivots = modular_rref(equations, 3)
    free = [column for column in range(strands) if column not in pivots]
    basis: list[tuple[int, ...]] = []
    for free_column in free:
        vector = [0] * strands
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-rref[row][free_column]) % 3
        basis.append(tuple(vector))
    require(all(all(sum(equations[row][column] * vector[column] for column in range(strands)) % 3 == 0 for row in range(strands)) for vector in basis), "Fox nullspace basis")
    return tuple(basis)


def fox_fixed_colorings(strands: int, word: BraidWord) -> tuple[tuple[int, ...], ...]:
    basis = fox_fixed_basis(strands, word)
    result = []
    for coefficients in itertools.product(range(3), repeat=len(basis)):
        vector = tuple(sum(coefficient * basis[index][column] for index, coefficient in enumerate(coefficients)) % 3 for column in range(strands))
        result.append(vector)
    return tuple(result)


AffineBit = tuple[int, int]  # coefficient mask, constant


def bit_parity(value: int) -> int:
    return bin(value).count("1") & 1


def affine_xor(*forms: AffineBit) -> AffineBit:
    mask = 0
    constant = 0
    for form_mask, form_constant in forms:
        mask ^= form_mask
        constant ^= form_constant
    return mask, constant


def scale_affine(bit: int, form: AffineBit) -> AffineBit:
    return form if bit else (0, 0)


def bit_lift_equations(quotient: tuple[int, ...], word: BraidWord) -> tuple[tuple[int, int], ...]:
    colors = list(quotient)
    forms: list[AffineBit] = [(1 << index, 0) for index in range(len(quotient))]
    for generator in word:
        index = abs(generator) - 1
        first_color, second_color = colors[index], colors[index + 1]
        first_form, second_form = forms[index], forms[index + 1]
        if generator > 0:
            alpha, beta, gamma = AFFINE_CONJUGATION[(first_color, second_color)]
            conjugated = affine_xor(scale_affine(alpha, first_form), scale_affine(beta, second_form), (0, gamma))
            colors[index], colors[index + 1] = (2 * first_color - second_color) % 3, first_color
            forms[index], forms[index + 1] = conjugated, first_form
        else:
            alpha, beta, gamma = AFFINE_CONJUGATION[(second_color, first_color)]
            conjugated = affine_xor(scale_affine(alpha, second_form), scale_affine(beta, first_form), (0, gamma))
            colors[index], colors[index + 1] = second_color, (2 * second_color - first_color) % 3
            forms[index], forms[index + 1] = second_form, conjugated
    require(tuple(colors) == quotient, "fixed Fox coloring before lift")
    return tuple(affine_xor(forms[index], (1 << index, 0)) for index in range(len(quotient)))


def affine_f2_solutions(variable_count: int, equations: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    rows = [mask | (constant << variable_count) for mask, constant in equations]
    pivot_for_column: dict[int, int] = {}
    pivot_row = 0
    for column in range(variable_count):
        selected = next((row for row in range(pivot_row, len(rows)) if (rows[row] >> column) & 1), None)
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        for row in range(len(rows)):
            if row != pivot_row and ((rows[row] >> column) & 1):
                rows[row] ^= rows[pivot_row]
        pivot_for_column[column] = pivot_row
        pivot_row += 1
    variable_mask = (1 << variable_count) - 1
    require(not any((row & variable_mask) == 0 and ((row >> variable_count) & 1) for row in rows), "consistent V4 lift equations")
    free = [column for column in range(variable_count) if column not in pivot_for_column]
    solutions: list[int] = []
    for free_assignment in range(1 << len(free)):
        solution = 0
        for position, column in enumerate(free):
            if (free_assignment >> position) & 1:
                solution |= 1 << column
        for column, row_index in reversed(tuple(pivot_for_column.items())):
            row = rows[row_index]
            right = (row >> variable_count) & 1
            parity = bit_parity(row & variable_mask & solution)
            if right ^ parity:
                solution |= 1 << column
        require(all(bit_parity(mask & solution) == constant for mask, constant in equations), "V4 lift solution")
        solutions.append(solution)
    return tuple(solutions)


def affine_f2_solution_count(variable_count: int, equations: tuple[tuple[int, int], ...]) -> int:
    rows = [mask | (constant << variable_count) for mask, constant in equations]
    rank = 0
    for column in range(variable_count):
        selected = next((row for row in range(rank, len(rows)) if (rows[row] >> column) & 1), None)
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        for row in range(len(rows)):
            if row != rank and ((rows[row] >> column) & 1):
                rows[row] ^= rows[rank]
        rank += 1
    variable_mask = (1 << variable_count) - 1
    require(not any((row & variable_mask) == 0 and ((row >> variable_count) & 1) for row in rows), "consistent V4 lift equations")
    return 1 << (variable_count - rank)


def lifted_full_s4_colorings(
    strands: int, word: BraidWord, *, validate_groups: bool = False
) -> tuple[int, int, int]:
    fox_colorings = fox_fixed_colorings(strands, word)
    full = 0
    lifts = 0
    nonconstant_fox = 0
    for quotient in fox_colorings:
        if len(set(quotient)) == 1:
            continue
        nonconstant_fox += 1
        equations = bit_lift_equations(quotient, word)
        solution_count = affine_f2_solution_count(strands, equations)
        require(solution_count >= 4, "four complement lifts exist")
        if not validate_groups:
            lifts += solution_count
            full += solution_count - 4
            continue
        solutions = affine_f2_solutions(strands, equations)
        require(len(solutions) == solution_count, "enumerated affine lift-space size")
        local_full = 0
        for solution in solutions:
            lifts += 1
            colors = tuple(COORD_TO_TRANS[(quotient[index], (solution >> index) & 1)] for index in range(strands))
            # Independent closure check uses the original S4 Hurwitz action.
            require(CORE.braid_action(colors, word) == colors, "lifted S4 coloring closes")
            if len(CORE.generated_subgroup(colors)) == 24:
                full += 1
                local_full += 1
        # A nonconstant Fox coloring is onto S3.  Its non-full lifts are
        # exactly the four sections into the four point-stabilizer complements
        # S3<S4.  Any other lift intersects V4 nontrivially; S3 permutes the
        # three nonidentity elements of V4 transitively, so that lift is S4.
        require(len(solutions) - local_full == 4, "four and only four complement lifts")
    return full, len(fox_colorings), lifts


def sign_vectors(stages: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.product((-1, 1), repeat=stages))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-framing", action="store_true")
    parser.add_argument("--mutate-quotient", action="store_true")
    parser.add_argument("--mutate-promote-zero", action="store_true")
    arguments = parser.parse_args()

    if arguments.mutate_framing:
        globals()["writhe"] = lambda word: 0
    if arguments.mutate_quotient:
        AFFINE_CONJUGATION[(0, 1)] = (0, 0, 0)

    # Together with the already sealed conductors 10 and 16, this is the
    # complete even-conductor ladder through 28.
    conductors = (12, 14, 18, 20, 22, 24, 26, 28)
    censuses = {conductor: CORE.delta_sequences_with_conductor(conductor, False, False) for conductor in conductors}

    # Compiler controls: the winding-two specialization must be byte-for-byte
    # the previously sealed compiler; every signed compiled closure is a knot;
    # and the braid determinant equals the recursive cable formula.
    old_two_cable = CORE.two_cable_of_two_braid_word(3, 7)
    new_strands, new_two_cable = compile_delta_sequence((6, 4, 7))
    require(new_strands == 4 and new_two_cable == old_two_cable, "winding-two compiler specialization")

    compiler_controls: dict[str, dict[str, int]] = {}
    all_rows = tuple(sequence for conductor in conductors for sequence in censuses[conductor])
    for sequence in all_rows:
        expected_determinant = recursive_alexander_determinant(sequence)
        sign_counts = []
        for signs in sign_vectors(len(sequence) - 1):
            strands, word = compile_delta_sequence(sequence, signs)
            require(strands == sequence[1], "compiled strand count equals r1")
            require(CORE.cycle_lengths(CORE.strand_permutation(strands, word)) == (strands,), "compiled braid closes to one knot")
            require(braid_alexander_determinant(strands, word) == expected_determinant, "recursive Alexander determinant")
            sign_counts.append((signs, strands, len(word)))
        compiler_controls[str(sequence)] = {
            "signed_variants": len(sign_counts),
            "strands": sequence[1],
            "alexander_determinant": expected_determinant,
        }

    # Exact full-polynomial controls cover a base 3-braid, winding two, and
    # winding three, with every independent sign choice.  These are stronger
    # than the determinant checks above and catch the blackboard-framing term.
    full_alexander_controls: dict[str, int] = {}
    full_control_signs = {
        (8, 3): sign_vectors(1),
        (6, 4, 9): sign_vectors(2),
        (9, 6, 4): sign_vectors(2),
        # A positive winding-four control reaches eight strands.  Winding
        # five and seven still receive all-sign determinant controls above.
        (12, 8, 3): ((1, 1),),
    }
    for sequence, selected_signs in full_control_signs.items():
        expected = recursive_alexander_polynomial(sequence)
        for signs in selected_signs:
            strands, word = compile_delta_sequence(sequence, signs)
            expected_numerator = expected * (CORE.ONE - CORE.Laurent.monomial(strands))
            require(
                CORE.unit_normalized(CORE.alexander_numerator(strands, word))
                == CORE.unit_normalized(expected_numerator),
                "full recursive cable Alexander polynomial",
            )
        full_alexander_controls[str(sequence)] = len(selected_signs)

    # Direct-coloring equivalence controls both the quotient/lift factorization
    # and its labelled normalization on tiny (at most four-strand) rows.  No
    # large 6^(n-1) search is performed by this replay.
    direct_controls: dict[str, int] = {}
    for sequence in all_rows:
        if sequence[1] > 4:
            continue
        strands, word = compile_delta_sequence(sequence)
        lifted, _, _ = lifted_full_s4_colorings(strands, word, validate_groups=True)
        direct = CORE.full_s4_colorings(strands, word)
        require(lifted == direct, "V4/S3 counter equals direct 6^n counter")
        direct_controls[str(sequence)] = direct

    counts: dict[str, dict[str, object]] = {}
    for conductor, sequences in censuses.items():
        for sequence in sequences:
            variants: dict[str, dict[str, int]] = {}
            for signs in sign_vectors(len(sequence) - 1):
                strands, word = compile_delta_sequence(sequence, signs)
                full, fox, lifts = lifted_full_s4_colorings(strands, word)
                variants["".join("+" if sign > 0 else "-" for sign in signs)] = {
                    "full_S4": full,
                    "fox_colorings": fox,
                    "nonconstant_S4_lifts": lifts,
                }
            counts[str(sequence)] = {
                "conductor": conductor,
                "strands": sequence[1],
                "variants": variants,
            }

    if arguments.mutate_promote_zero:
        first = next(iter(counts.values()))
        next(iter(first["variants"].values()))["full_S4"] = 1

    survivors = {
        sequence: sorted(sign for sign, data in row["variants"].items() if data["full_S4"])
        for sequence, row in counts.items()
        if any(data["full_S4"] for data in row["variants"].values())
    }

    expected_positive_counts = {
        "(6, 4, 9)": 72,
        "(9, 6, 4)": 72,
        "(8, 3)": 24,
        "(8, 6, 3)": 72,
        "(12, 8, 3)": 168,
        "(12, 8, 6, 3)": 360,
        "(15, 6, 4)": 24,
        "(8, 6, 9)": 72,
        "(9, 6, 8)": 72,
        "(12, 8, 6, 9)": 360,
        "(9, 4)": 24,
        "(9, 6, 10)": 144,
        "(12, 8, 10, 9)": 72,
        "(12, 9, 4)": 384,
        "(18, 4, 9)": 72,
        "(18, 12, 4, 9)": 72,
        "(18, 12, 9, 4)": 432,
        "(21, 6, 4)": 24,
        "(8, 6, 15)": 72,
        "(15, 6, 8)": 24,
        "(27, 6, 2)": 144,
        "(27, 18, 2)": 144,
        "(27, 18, 6, 2)": 1872,
    }
    observed_positive_counts = {
        sequence: row["variants"]["+" * (len(sequence.strip("()").split(",")) - 1)]["full_S4"]
        for sequence, row in counts.items()
        if row["variants"]["+" * (len(sequence.strip("()").split(",")) - 1)]["full_S4"]
    }
    require(observed_positive_counts == expected_positive_counts, "frozen next-rung survivor census")
    require(
        all(len({variant["full_S4"] for variant in row["variants"].values()}) == 1 for row in counts.values()),
        "all independent sign variants have the same count in the charged rows",
    )

    payload = {
        "status": "PASS-A1-GENUS-LADDER-NEXT-S4-CENSUS",
        "pinned_core_sha256": PINNED_CORE_SHA256,
        "conductors": list(conductors),
        "censuses": {str(conductor): [list(sequence) for sequence in sequences] for conductor, sequences in censuses.items()},
        "compiler_controls": compiler_controls,
        "full_alexander_polynomial_controls": full_alexander_controls,
        "direct_counter_controls": direct_controls,
        "all_family_criterion": {
            "quotient": "nonconstant Fox 3-coloring rho",
            "lift_space": "affine F2 solution space L_rho",
            "four_nonfull_lifts": "the four S3 complements in S4",
            "full_S4_iff": "some |L_rho| > 4",
            "labeled_count": "sum_rho (|L_rho|-4)",
        },
        "counts": counts,
        "survivors": survivors,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
