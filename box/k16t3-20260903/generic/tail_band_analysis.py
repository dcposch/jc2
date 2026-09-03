#!/usr/bin/env python3
"""Reproducible generic-band checks for the gauged K=16 family.

The script compares fixed low h-levels after reverse-index renaming and
checks an exact witness showing that every fixed low cutoff is consistent
for all sufficiently large t.  It performs no standard-basis computation.
"""

import importlib.util
import re

import sympy as sp


DRIVER = "/home/ubuntu/jc2/box/k16t3-20260903/generic/generic_order_system.py"


def load_driver():
    spec = importlib.util.spec_from_file_location("generic_order_system", DRIVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_tail(data, equation):
    """Rename alpha_(e-s), beta_(q-r) coordinates by h powers s,r."""
    rename = {}
    for symbol in equation.free_symbols:
        match = re.fullmatch(r"a(\d+)_(\d+)", str(symbol))
        if match:
            deficit, coordinate = map(int, match.groups())
            rename[symbol] = sp.Symbol("p%d_%d" %
                                       (data["e"] - deficit, coordinate))
            continue
        match = re.fullmatch(r"q(\d+)_(\d+)", str(symbol))
        if match:
            deficit, coordinate = map(int, match.groups())
            rename[symbol] = sp.Symbol("r%d_%d" %
                                       (data["q"] - deficit, coordinate))
    return sp.expand(equation.xreplace(rename))


def canonical_level(data, h_level):
    return {
        monomial: canonical_tail(data, equation)
        for hp, monomial, equation in data["tagged"] if hp == h_level
    }


def witness_substitution(data):
    """Q=h^q+B, P=h^e+gamma+2z, c=-1, with b_i=0."""
    substitution = {parameter: 0 for parameter in data["params"]}
    substitution[data["c"]] = -1
    substitution[sp.Symbol("q%d_1" % data["q"])] = 1  # endpoint B
    substitution[sp.Symbol("a%d_0" % data["e"])] = 1  # endpoint gamma
    substitution[sp.Symbol("a%d_3" % data["e"])] = 2  # endpoint z
    return substitution


def main():
    driver = load_driver()
    gamma, pi = driver.gamma, driver.pi
    z = pi - gamma
    B = pi * z
    h = pi**3 * z
    p0 = gamma + 2 * z

    identities = {
        "J(B,p0)": sp.expand(driver.jac(B, p0)),
        "J(h,p0)": sp.factor(driver.jac(h, p0)),
        "J(B,h)": sp.factor(driver.jac(B, h)),
    }
    assert sp.expand(identities["J(B,p0)"] + gamma) == 0
    assert sp.expand(identities["J(h,p0)"] -
                     pi**2 * (-3 * gamma + 2 * pi)) == 0
    assert sp.expand(identities["J(B,h)"] + 2 * h) == 0
    print("SYMBOLIC_WITNESS_IDENTITIES", identities)
    print("FORMULA J(Q,P)=-gamma+q*pi^2*(2*pi-3*gamma)*h^(q-1)-2*e*h^e")

    systems = {t: driver.build(t, gauged=True) for t in (2, 3, 4)}
    for t, data in systems.items():
        residuals = []
        substitution = witness_substitution(data)
        for hp, monomial, equation in data["tagged"]:
            value = sp.expand(equation.subs(substitution))
            if value != 0:
                residuals.append((hp, monomial, value))
        expected = [
            (2 * t, (1, 2), -3 * data["q"]),
            (2 * t, (0, 3), 2 * data["q"]),
            (data["e"], (0, 0), -2 * data["e"]),
        ]
        assert residuals == expected
        print("WITNESS t=%d zero_levels=0..%d_except_rhs residuals=%s" %
              (t, 2 * t - 1, residuals))

        tagged_map = {(hp, monomial): equation
                      for hp, monomial, equation in data["tagged"]}
        first_a = sp.Symbol("a%d_1" % (t + 1))
        first_r = sp.Symbol("q%d_1" % (t + 1))
        second_a = sp.Symbol("a%d_1" % (t + 2))
        second_r = sp.Symbol("q%d_1" % (t + 2))
        alpha_one = sp.Symbol("a1_0")
        b4 = sp.Symbol("b4")
        leading = data["q"] * first_a - data["e"] * first_r
        next_equation = (data["q"] * second_a - data["e"] * second_r
                         - 3 * t * alpha_one * first_r - b4 * leading)
        assert sp.expand(tagged_map[(4 * t + 1, (0, 1))] - leading) == 0
        assert sp.expand(tagged_map[(4 * t, (0, 1))] - next_equation) == 0
        print("TOP_RECURRENCE_CHECK t=%d leading=%s next=%s" %
              (t, leading, next_equation))

    # A final level H uses reverse coefficients through h-power H+1.  Those
    # spaces stabilize when t >= H+1.  Verify the predicted comparisons.
    for earlier, later in ((2, 3), (3, 4)):
        first_difference = None
        equal_levels = []
        for level in range(0, earlier + 2):
            equal = (canonical_level(systems[earlier], level) ==
                     canonical_level(systems[later], level))
            if equal:
                equal_levels.append(level)
            elif first_difference is None:
                first_difference = level
        assert equal_levels[:earlier] == list(range(earlier))
        assert first_difference == earlier
        print("TAIL_COMPARE t=%d_vs_%d equal_levels=%s first_difference=%d" %
              (earlier, later, list(range(earlier)), first_difference))

        old = canonical_level(systems[earlier], first_difference)
        new = canonical_level(systems[later], first_difference)
        difference_symbols = set()
        for monomial in set(old) | set(new):
            difference = sp.expand(new.get(monomial, 0) - old.get(monomial, 0))
            difference_symbols.update(difference.free_symbols)
        boundary = sorted(
            (str(symbol) for symbol in difference_symbols
             if str(symbol).startswith("p%d_" % (earlier + 1))
             or str(symbol).startswith("r%d_" % (earlier + 1))))
        assert boundary == ["p%d_2" % (earlier + 1),
                            "r%d_1" % (earlier + 1)]
        print("TAIL_BOUNDARY_NEW_COORDINATES", boundary)

    # Highest nonzero level is 4t+1.  The first t high-side levels each
    # have one scalar remainder equation; at offset t a second coordinate
    # first appears.  This catches the same moving filtration boundary.
    for t, data in systems.items():
        top = 4 * t + 1
        counts = [len(canonical_level(data, top - offset))
                  for offset in range(0, t + 1)]
        assert counts[:-1] == [1] * t and counts[-1] == 2
        print("HIGH_BAND_COUNTS t=%d offsets_0_through_t=%s" % (t, counts))


if __name__ == "__main__":
    main()
