#!/usr/bin/env python3
"""Parse the modular dp leading ideals and summarize their finite staircases."""

from __future__ import annotations

import itertools
import pathlib
import re


HERE = pathlib.Path(__file__).resolve().parent
FILES = {
    3: HERE / "probe_t3_mod_b0.out",
    4: HERE / "probe_t4_mod_b0.out",
    5: HERE / "probe_t5_mod_b0_lm.out",
    6: HERE / "probe_t6_mod_b0.out",
}


def variables(t: int) -> list[str]:
    return ["b3", *[f"q{i}_0" for i in range(2, t)]]


def exponent_tuple(text: str, names: list[str]) -> tuple[int, ...]:
    exps = {name: 0 for name in names}
    for factor in text.strip().split("*"):
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_]*)(?:\^([0-9]+))?", factor)
        if not match or match.group(1) not in exps:
            raise ValueError(text)
        exps[match.group(1)] += int(match.group(2) or 1)
    return tuple(exps[name] for name in names)


def parse(t: int, path: pathlib.Path) -> list[tuple[int, ...]]:
    names = variables(t)
    lines = path.read_text(encoding="utf-8").splitlines()
    start = lines.index("PROBE_DIM") + 4
    raw = []
    for line in lines[start:]:
        if line == "PROBE_DONE":
            break
        if line and not line.startswith("PROBE"):
            raw.append(exponent_tuple(line, names))
    return raw


def main() -> None:
    for t, path in FILES.items():
        names = variables(t)
        leading = parse(t, path)
        bounds = []
        for index in range(len(names)):
            pure = [m[index] for m in leading if sum(m) == m[index]]
            if not pure:
                raise RuntimeError(f"no pure power for t={t}, {names[index]}")
            bounds.append(min(pure))
        standard = []
        for monomial in itertools.product(*(range(bound) for bound in bounds)):
            if not any(all(a >= b for a, b in zip(monomial, lm)) for lm in leading):
                standard.append(monomial)
        slices = []
        for exponent in range(bounds[-1]):
            slices.append(sum(m[-1] == exponent for m in standard))
        degree_counts: dict[int, int] = {}
        for monomial in standard:
            degree_counts[sum(monomial)] = degree_counts.get(sum(monomial), 0) + 1
        print(f"t={t} generators={len(leading)} bounds={dict(zip(names,bounds))}")
        generator_degrees: dict[int, int] = {}
        for monomial in leading:
            degree = sum(monomial)
            generator_degrees[degree] = generator_degrees.get(degree, 0) + 1
        print(f"  generator_degrees={generator_degrees}")
        print(f"  length={len(standard)} last_slices={slices}")
        print(f"  hilbert={','.join(f'{degree}:{count}' for degree,count in sorted(degree_counts.items()))}")


if __name__ == "__main__":
    main()
