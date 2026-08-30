#!/usr/bin/env python3
"""Desk replay for the exact R4-CYCLE-1 pseudo-plane threat map.

This verifies only finite permutation, Euler-ledger, and explicit curve-control
claims.  It deliberately does not encode any surface-classification theorem,
existence of a finite-flat cover, or the Jacobian conjecture.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json


Perm = tuple[int, int, int, int]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(4))  # type: ignore[return-value]


def inverse(p: Perm) -> Perm:
    out = [0, 0, 0, 0]
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)  # type: ignore[return-value]


def conjugate(g: Perm, p: Perm) -> Perm:
    return compose(compose(g, p), inverse(g))


def transposition(i: int, j: int) -> Perm:
    out = [0, 1, 2, 3]
    out[i], out[j] = out[j], out[i]
    return tuple(out)  # type: ignore[return-value]


def closure(generators: tuple[Perm, ...]) -> set[Perm]:
    identity: Perm = (0, 1, 2, 3)
    group = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            nxt = compose(current, generator)
            if nxt not in group:
                group.add(nxt)
                frontier.append(nxt)
    return group


def fixed_pair(p: Perm) -> tuple[int, int]:
    fixed = tuple(i for i in range(4) if p[i] == i)
    require(len(fixed) == 2, "charged inertia is not a transposition")
    return fixed  # type: ignore[return-value]


def bijection_parity(g: Perm, source: tuple[int, int], target: tuple[int, int]) -> int:
    image = (g[source[0]], g[source[1]])
    require(set(image) == set(target), "transporter does not map companion pairs")
    return 0 if image == target else 1


def curve_control() -> dict[str, object]:
    # x=t^2, y=t^3(t^2-1), hence y^2=x^3(x-1)^2.
    for t in range(-7, 8):
        x = t * t
        y = t**3 * (t * t - 1)
        require(y * y == x**3 * (x - 1) ** 2, "parametrization identity failed")

    # dx/dt=2t and dy/dt=t^2(5t^2-3) vanish together only at t=0.
    common_integer_zeros = [
        t for t in range(-20, 21) if 2 * t == 0 and t * t * (5 * t * t - 3) == 0
    ]
    require(common_integer_zeros == [0], "unexpected derivative common zero")

    # The only distinct normalization collision is t=1 with t=-1.
    collisions: set[tuple[int, int]] = set()
    values: dict[tuple[int, int], list[int]] = {}
    for t in range(-12, 13):
        key = (t * t, t**3 * (t * t - 1))
        values.setdefault(key, []).append(t)
    for preimages in values.values():
        if len(preimages) > 1:
            for a, b in itertools.combinations(preimages, 2):
                collisions.add(tuple(sorted((a, b))))
    require(collisions == {(-1, 1)}, "unexpected sampled normalization collision")

    tangent_plus = (2, 2)
    tangent_minus = (-2, 2)
    tangent_det = tangent_plus[0] * tangent_minus[1] - tangent_plus[1] * tangent_minus[0]
    require(tangent_det == 8, "node tangents are not transverse")

    return {
        "equation": "y^2=x^3(x-1)^2",
        "normalization_euler": 1,
        "node_collision": [-1, 1],
        "node_tangent_determinant": tangent_det,
        "reduced_curve_euler": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-force-companion-parity", action="store_true")
    args = parser.parse_args()

    permutations: tuple[Perm, ...] = tuple(itertools.permutations(range(4)))  # type: ignore[assignment]
    transpositions = tuple(transposition(i, j) for i in range(4) for j in range(i + 1, 4))

    tau = transposition(0, 1)      # (12)
    cusp_mate = transposition(1, 2)  # (23), overlapping with tau
    node_mate = transposition(2, 3)  # (34), disjoint from tau

    require(compose(compose(tau, cusp_mate), tau) == compose(compose(cusp_mate, tau), cusp_mate),
            "cusp braid relation failed")
    require(compose(tau, node_mate) == compose(node_mate, tau),
            "node commuting relation failed")
    require(len(closure((tau, cusp_mate))) == 6, "cusp packet should generate S3")
    require(len(closure((tau, cusp_mate, node_mate))) == 24,
            "cusp-plus-node packet should generate S4")

    transporter_profiles: dict[str, dict[str, object]] = {}
    for source in transpositions:
        for target in transpositions:
            transporters = tuple(g for g in permutations if conjugate(g, source) == target)
            require(len(transporters) == 4, "wrong transposition-transporter count")
            parities = [bijection_parity(g, fixed_pair(source), fixed_pair(target)) for g in transporters]
            if args.mutate_force_companion_parity:
                parities = [0 for _ in parities]
            require(sorted(parities) == [0, 0, 1, 1],
                    "local inertia labels falsely force a companion parity")
            key = f"{source}->{target}"
            transporter_profiles[key] = {
                "count": len(transporters),
                "companion_parities": sorted(parities),
            }

    # R4-CYCLE-1: e(B)=0; remove the distinct cusp and node; companion
    # fibre counts are respectively 2 on the remainder, 1 at the cusp, 0 at
    # the node.  The ruling gives e(U)=1.
    e_b = 0
    e_b_remainder = e_b - 2
    e_t = 2 * e_b_remainder + 1
    e_u = 1
    e_w_by_deletion = e_u - e_t
    e_w_by_cover = 4 * (1 - e_b)
    require(e_t == -3, "wrong companion-divisor Euler number")
    require(e_w_by_deletion == e_w_by_cover == 4, "two complement Euler ledgers disagree")

    # Abstract class-lattice consistency control: boundary classes e_i are
    # free; the different is their sum; companion closures have classes
    # -2e_i; quotienting by the boundary leaves arbitrary Z/M torsion.
    sample_boundary_rank = 3
    different = tuple(1 for _ in range(sample_boundary_rank))
    companion_classes = tuple(
        tuple(-2 if i == j else 0 for i in range(sample_boundary_rank))
        for j in range(sample_boundary_rank)
    )
    require(any(value != 0 for value in different), "different class vanished")
    for j, cls in enumerate(companion_classes):
        require(cls[j] == -2 and sum(abs(value) for value in cls) == 2,
                "componentwise pullback class relation failed")

    control = curve_control()
    charged = {
        "class_control": {
            "boundary_rank": sample_boundary_rank,
            "companion_classes": companion_classes,
            "different": different,
            "quotient_torsion": "Z/M",
        },
        "companion_euler": e_t,
        "complement_euler_by_cover": e_w_by_cover,
        "complement_euler_by_deletion": e_w_by_deletion,
        "control_curve": control,
        "cusp_group_order": len(closure((tau, cusp_mate))),
        "full_packet_group_order": len(closure((tau, cusp_mate, node_mate))),
        "transposition_pair_count": len(transporter_profiles),
        "transporter_profile_digest": hashlib.sha256(
            json.dumps(transporter_profiles, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }
    payload = json.dumps(charged, sort_keys=True, separators=(",", ":"))
    output = {
        **charged,
        "payload_sha256": hashlib.sha256(payload.encode()).hexdigest(),
        "status": "PASS-QUARTIC-CYCLE1-PSEUDOPLANE-THREAT-MAP",
    }
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
