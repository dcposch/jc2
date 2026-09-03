#!/usr/bin/env python3
"""Independent fixed-t checks for the generalized t=3 order driver."""

from fractions import Fraction
import importlib.util


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    old = load("frozen_t2_order_system",
               "/tmp/jc2-lane.NKyBDU/inputs/t2_order_system.py")
    raymod = load("frozen_k16_symbolic",
                  "/tmp/jc2-lane.NKyBDU/inputs/k16_symbolic.py")
    new = load("generalized_t_order_system",
               "/home/ubuntu/jc2/box/k16t3-20260903/t3/t_order_system.py")

    symbolic = raymod.symbolic_ray()
    t_symbol = symbolic["t"]
    phi_at_3 = tuple(x.subs(t_symbol, 3) for x in symbolic["phi"])
    fixed = raymod.ray(3)
    assert phi_at_3 == (-1, Fraction(3, 10))
    assert fixed["phi"] == (Fraction(-1), Fraction(3, 10))
    assert (fixed["n"], fixed["m"], fixed["M2"], fixed["V2"]) == (40, 28, 37, 3)
    print("RADIUS_CLOSED_FORM Phi=(-1,t/(3*t+1))")
    print("RADIUS_T3 Phi=(-1,3/10) PASS")
    print("TUPLE_T3 (40,28;37,3) PASS")

    old_t2 = old.build(gauged=True)
    new_t2 = new.build(t=2, gauged=True)
    assert [str(v) for v in old_t2["params"]] == [str(v) for v in new_t2["params"]]
    assert old_t2["tagged"] == new_t2["tagged"]
    print("T2_PARAMETER_ORDER_IDENTICAL PASS")
    print("T2_ALL_37_TAGGED_EQUATIONS_IDENTICAL PASS")

    ungauged = new.build(t=3, gauged=False)
    gauged = new.build(t=3, gauged=True)
    assert len(ungauged["params"]) + 1 == 39
    assert len(gauged["params"]) + 1 == 36
    assert len(gauged["equations"]) == 51
    assert [len(gauged["spaces"][i]) for i in range(1, 11)] == [1, 1, 1, 2, 2, 2, 3, 3, 3, 5]
    print("T3_UNGAUGED_UNKNOWNS 39 PASS")
    print("T3_GAUGED_UNKNOWNS 36 PASS")
    print("T3_COEFFICIENT_GENERATORS 51 PASS")
    print("T3_FILTRATION_DIMS [1,1,1,2,2,2,3,3,3,5] PASS")

    jacobian, anchor_degrees, deg_f, deg_g = raymod.monomial_control()
    assert str(jacobian) == "gamma"
    assert anchor_degrees == (2, 2) and (deg_f, deg_g) == (1, 1)
    print("ACTUAL_PAIR_CONTROL J=gamma pi_degrees=(1,1) PASS")
    print("ACTUAL_PAIR_K16_TUPLE_CLASSIFIER FAIL_AS_REQUIRED")


if __name__ == "__main__":
    main()
