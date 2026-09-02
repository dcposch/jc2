#!/usr/bin/env python3
"""Fail-closed encoding preflight for ``N >= 6`` realization jobs.

The JSON contract is the output of :func:`manifest_to_dict`.  A generator
emits one manifest beside its solver ideal, then launch code runs::

    python3 box/preflight.py job.preflight.json job.ms

Exit zero means that the declared QQ/GRevLex ring and explicit ring map, the
entire reduced approximate root, every ordered ideal generator, the
Rabinowitsch open, the source ``EQ2_even`` identity, the typed output, the
built-in 86A/96B controls, and the pinned solver stack all passed.  The second
path is mandatory: its exact SHA-256 and its parsed ring/characteristic/rows
must match the manifest, which prevents approving one ideal and launching
another.  Missing or unknown data is an error.  No solver is launched here.

The exact corrected ``G86``/``G96`` expansions are reused from
``box/qq_oracle_jobs.py`` (encoding-faithfulness audit r2, section 7.1).
Only the standard library is imported at module load; qqideal and msolveio are
checked by distribution metadata, and msolve is queried only by the default
launch-stack probe.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, replace
from enum import Enum
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence, Tuple

try:  # package import (tests / ``python -m box.preflight``)
    from box import qq_oracle_jobs as algebra
except ImportError:  # direct ``python box/preflight.py``
    import qq_oracle_jobs as algebra  # type: ignore[no-redef]


EXPECTED_PACKAGES = {"qqideal": "0.2.0", "msolveio": "0.2.1"}
EXPECTED_MSOLVE = "0.10.1"
SCHEMA_VERSION = 1


class Artifact(str, Enum):
    NUMERICAL_PROFILE = "NUMERICAL_PROFILE"
    FORMAL_EO_SERIES = "FORMAL_EO_SERIES"
    SUBSYSTEM_POINT = "SUBSYSTEM_POINT"
    FULL_EO_POINT = "FULL_EO_POINT"
    CURVE = "CURVE"
    REPRESENTATION = "REPRESENTATION"
    FULL_COVER = "FULL_COVER"
    POLYNOMIAL_PAIR = "POLYNOMIAL_PAIR"


class Attainment(str, Enum):
    NECESSARY = "NECESSARY"
    REALIZED = "REALIZED"
    ADMISSIBLE_PULLBACK = "ADMISSIBLE_PULLBACK"
    ACTUAL_MAP = "ACTUAL_MAP"
    COUNTEREXAMPLE_CERTIFIED = "COUNTEREXAMPLE_CERTIFIED"


class Arrow(str, Enum):
    FULL_EO_EQUATIONS = "FULL_EO_EQUATIONS"
    DECLARED_QUOTIENT = "DECLARED_QUOTIENT"
    EO_ALL_OPENS = "EO_ALL_OPENS"
    BOUNDARY_DATA = "BOUNDARY_DATA"
    GENERAL_FIBRE_DATA = "GENERAL_FIBRE_DATA"
    FIELD_DEGREE_FOUR = "FIELD_DEGREE_FOUR"
    SOURCE_CHART = "SOURCE_CHART"
    NONINVERTIBILITY = "NONINVERTIBILITY"
    GEOMETRIC_DEGREE = "GEOMETRIC_DEGREE"


@dataclass(frozen=True)
class TypedOutput:
    artifact: Artifact
    attainment: Attainment


@dataclass(frozen=True)
class Transition:
    source: TypedOutput
    target: TypedOutput
    source_domain: str
    target_domain: str
    source_scope: str = "GLOBAL"
    target_scope: str = "GLOBAL"
    claim: str = "POINT"
    arrows: Tuple[Arrow, ...] = ()


@dataclass(frozen=True)
class PolynomialSlot:
    name: str
    expression: str


@dataclass(frozen=True)
class RootCoefficient:
    degree: int
    expression: str


@dataclass(frozen=True)
class OpenFactor:
    name: str
    expression: str
    inverse: str
    equation_name: str


@dataclass(frozen=True)
class SourceFidelity:
    """Data needed to derive corrected EQ2_even, rather than trust a label."""

    ring_generators: Tuple[str, ...]
    old_eq2: str
    q: str
    e1: str
    encoded_eq2_even: str


@dataclass(frozen=True)
class StackObservation:
    package_versions: Mapping[str, Optional[str]]
    msolve_version: Optional[str]
    msolve_binary: Optional[str] = None


@dataclass(frozen=True)
class Manifest:
    schema_version: int
    job_id: str
    degree_n: int
    cell: str
    coefficient_field: str
    monomial_order: str
    ring_generators: Tuple[str, ...]
    map_source_order: Tuple[str, ...]
    map_images: Tuple[str, ...]
    reduced_root: Tuple[RootCoefficient, ...]
    ideal_generators: Tuple[PolynomialSlot, ...]
    generator_order: Tuple[str, ...]
    solver_input_sha256: str
    open_factors: Tuple[OpenFactor, ...]
    source_fidelity: SourceFidelity
    output: TypedOutput
    transitions: Tuple[Transition, ...]
    package_versions: Mapping[str, str]
    msolve_version: str


@dataclass(frozen=True)
class PreflightResult:
    ok: bool
    job_id: str
    checks: Tuple[str, ...]
    errors: Tuple[str, ...]
    output: Optional[TypedOutput]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ok": self.ok,
            "job_id": self.job_id,
            "checks": list(self.checks),
            "errors": list(self.errors),
            "artifact": self.output.artifact.value if self.output else None,
            "attainment": self.output.attainment.value if self.output else None,
        }


@dataclass(frozen=True)
class _Cell:
    family: str
    delta: Tuple[int, int, int]
    auxiliary: Tuple[str, ...]
    closed_hi: int
    closed_lo: int
    open_degree: int


CELLS: Mapping[str, _Cell] = {
    "86A": _Cell("86", (8, 6, 11), algebra.AUX_A, 22, 12, 11),
    "86B": _Cell("86", (8, 6, 9), algebra.AUX_B, 22, 10, 9),
    "86C": _Cell("86", (8, 6, 7), algebra.AUX_C, 22, 8, 7),
    "86D": _Cell("86", (8, 6, 3), algebra.AUX_D, 22, 4, 3),
    "96A": _Cell("96", (9, 6, 4), algebra.AUX_96, 16, 5, 4),
    "96B": _Cell("96", (9, 6, 2), algebra.AUX_96, 16, 3, 2),
}


_OUTPUTS: Mapping[Artifact, frozenset[Attainment]] = {
    Artifact.NUMERICAL_PROFILE: frozenset({Attainment.NECESSARY}),
    Artifact.FORMAL_EO_SERIES: frozenset({Attainment.NECESSARY}),
    Artifact.SUBSYSTEM_POINT: frozenset({Attainment.REALIZED}),
    Artifact.FULL_EO_POINT: frozenset(
        {Attainment.REALIZED, Attainment.ADMISSIBLE_PULLBACK}
    ),
    Artifact.CURVE: frozenset({Attainment.REALIZED}),
    Artifact.REPRESENTATION: frozenset(
        {Attainment.NECESSARY, Attainment.REALIZED}
    ),
    Artifact.FULL_COVER: frozenset({Attainment.REALIZED}),
    Artifact.POLYNOMIAL_PAIR: frozenset(
        {
            Attainment.REALIZED,
            Attainment.ACTUAL_MAP,
            Attainment.COUNTEREXAMPLE_CERTIFIED,
        }
    ),
}

_PULLBACK_ARROWS = frozenset(
    {
        Arrow.EO_ALL_OPENS,
        Arrow.BOUNDARY_DATA,
        Arrow.GENERAL_FIBRE_DATA,
        Arrow.FIELD_DEGREE_FOUR,
    }
)
_FULL_EO_ARROWS = frozenset({Arrow.FULL_EO_EQUATIONS, Arrow.DECLARED_QUOTIENT})
_MAP_ARROWS = _PULLBACK_ARROWS | {Arrow.SOURCE_CHART}
_ALLOWED_DOMAINS = frozenset({"A2", "B3", "CURVE", "REPRESENTATION", "COVER", "MAP"})
_ALLOWED_SCOPES = frozenset({"LOCAL", "GLOBAL"})
_ALLOWED_CLAIMS = frozenset({"POINT", "KILL", "TORSION", "TORSION_ORDER"})
_TRANSITIONS: Mapping[Tuple[TypedOutput, TypedOutput], frozenset[Arrow]] = {
    (
        TypedOutput(Artifact.SUBSYSTEM_POINT, Attainment.REALIZED),
        TypedOutput(Artifact.FULL_EO_POINT, Attainment.REALIZED),
    ): _FULL_EO_ARROWS,
    (
        TypedOutput(Artifact.FULL_EO_POINT, Attainment.REALIZED),
        TypedOutput(Artifact.FULL_EO_POINT, Attainment.ADMISSIBLE_PULLBACK),
    ): _PULLBACK_ARROWS,
    (
        TypedOutput(Artifact.FULL_EO_POINT, Attainment.ADMISSIBLE_PULLBACK),
        TypedOutput(Artifact.POLYNOMIAL_PAIR, Attainment.ACTUAL_MAP),
    ): frozenset({Arrow.SOURCE_CHART}),
    (
        TypedOutput(Artifact.FULL_EO_POINT, Attainment.REALIZED),
        TypedOutput(Artifact.POLYNOMIAL_PAIR, Attainment.ACTUAL_MAP),
    ): _MAP_ARROWS,
    (
        TypedOutput(Artifact.POLYNOMIAL_PAIR, Attainment.ACTUAL_MAP),
        TypedOutput(Artifact.POLYNOMIAL_PAIR, Attainment.COUNTEREXAMPLE_CERTIFIED),
    ): frozenset({Arrow.NONINVERTIBILITY, Arrow.GEOMETRIC_DEGREE}),
}


class PreflightError(ValueError):
    pass


def _expand(cell: _Cell):
    if cell.family == "86":
        return algebra.expand_g86(cell.auxiliary)
    return algebra.expand_g96(cell.auxiliary)


def _mv_constant(names: Tuple[str, ...], value: object):
    coefficient = Fraction(value)  # corrected roots are over QQ
    if not coefficient:
        return algebra.MV(names, {})
    return algebra.MV(names, {(0,) * len(names): coefficient})


def _mv_power(poly, exponent: int):
    result = _mv_constant(poly.names, 1)
    base = poly
    while exponent:
        if exponent & 1:
            result = result * base
        base = base * base
        exponent >>= 1
    return result


def _map_mv(poly, source_names, images, target_names):
    if poly.names != tuple(source_names):
        raise PreflightError("internal source-ring mismatch")
    result = _mv_constant(target_names, 0)
    for exponents, coefficient in poly.terms.items():
        term = _mv_constant(target_names, coefficient)
        for image, exponent in zip(images, exponents):
            if exponent:
                term = term * _mv_power(image, exponent)
        result = result + term
    return result


def _variable_index(poly) -> Optional[int]:
    if len(poly.terms) != 1:
        return None
    exponent, coefficient = next(iter(poly.terms.items()))
    if Fraction(coefficient) != 1 or sum(exponent) != 1:
        return None
    try:
        return exponent.index(1)
    except ValueError:
        return None


def validate_typed_output(output: TypedOutput) -> None:
    if output.attainment not in _OUTPUTS.get(output.artifact, frozenset()):
        raise PreflightError(
            f"invalid artifact/attainment pair: "
            f"{output.artifact.value}/{output.attainment.value}"
        )


def validate_transition(transition: Transition) -> None:
    """Apply the explicit, fail-closed semantic transition table."""
    validate_typed_output(transition.source)
    validate_typed_output(transition.target)
    source_domain = transition.source_domain
    target_domain = transition.target_domain
    source_scope = transition.source_scope
    target_scope = transition.target_scope
    claim = transition.claim
    if source_domain not in _ALLOWED_DOMAINS or target_domain not in _ALLOWED_DOMAINS:
        raise PreflightError("unknown or non-canonical transition domain")
    if source_scope not in _ALLOWED_SCOPES or target_scope not in _ALLOWED_SCOPES:
        raise PreflightError("unknown or non-canonical transition scope")
    if claim not in _ALLOWED_CLAIMS:
        raise PreflightError("unknown or non-canonical transition claim")
    if (
        source_domain == "A2"
        and target_domain == "B3"
        and claim == "KILL"
    ):
        raise PreflightError("forbidden transition: A2 cell -> B3 kill")
    if (
        "TORSION" in claim
        and source_scope == "LOCAL"
        and target_scope == "GLOBAL"
    ):
        raise PreflightError("forbidden transition: local torsion -> global torsion")
    if source_domain != target_domain:
        raise PreflightError("cross-domain transition has no declared object map")
    if transition.source == transition.target:
        raise PreflightError("transition source and target are identical")
    required = _TRANSITIONS.get((transition.source, transition.target))
    if required is None:
        raise PreflightError("transition is absent from the checked table")
    supplied = frozenset(transition.arrows)
    missing = required - supplied
    extra = supplied - required
    if missing or extra:
        detail = []
        if missing:
            detail.append("missing=" + ",".join(sorted(a.value for a in missing)))
        if extra:
            detail.append("unexpected=" + ",".join(sorted(a.value for a in extra)))
        raise PreflightError("transition arrow mismatch: " + " ".join(detail))


def _validate_source_fidelity(source: SourceFidelity) -> None:
    names = source.ring_generators
    canonical_names = ("oldEQ2", "q", "E1")
    if names != canonical_names:
        raise PreflightError("source-fidelity generator order must be oldEQ2,q,E1")
    try:
        old = algebra.parse_mv(source.old_eq2, names)
        q = algebra.parse_mv(source.q, names)
        e1 = algebra.parse_mv(source.e1, names)
        encoded = algebra.parse_mv(source.encoded_eq2_even, names)
    except (TypeError, ValueError) as exc:
        raise PreflightError(f"EQ2_even parse/ring failure: {exc}") from exc
    canonical = tuple(algebra.parse_mv(name, names) for name in canonical_names)
    if (old, q, e1) != canonical:
        raise PreflightError("source-fidelity aliases are not the canonical source images")
    correction = 2 * q * e1
    if q.is_zero() or e1.is_zero() or correction.is_zero():
        raise PreflightError("source-fidelity correction -2*q*E1 is vacuous")
    expected = old - 2 * q * e1
    if encoded != expected:
        difference = encoded - expected
        raise PreflightError(
            "EQ2_even source-fidelity mismatch (expected old_EQ2-2*q*E1; "
            f"exact diff {algebra.render_mv(difference)})"
        )


def _validate_manifest(manifest: Manifest, checks: list[str]) -> None:
    if type(manifest.schema_version) is not int or manifest.schema_version != SCHEMA_VERSION:
        raise PreflightError("unsupported manifest schema")
    if type(manifest.degree_n) is not int or manifest.degree_n < 6:
        raise PreflightError("this hard launch gate requires declared N >= 6")
    if not isinstance(manifest.job_id, str) or not manifest.job_id:
        raise PreflightError("job_id must be a nonempty string")
    if manifest.cell not in CELLS:
        raise PreflightError(f"unknown corrected cell {manifest.cell!r}")
    if manifest.coefficient_field != "QQ" or manifest.monomial_order != "GRevLex":
        raise PreflightError("coefficient ring must be QQ with GRevLex order")

    cell = CELLS[manifest.cell]
    source_names, root = _expand(cell)
    expected_source_order = source_names + ("u",)
    if manifest.map_source_order != expected_source_order:
        raise PreflightError("ring-map source generator order mismatch")
    target_names = manifest.ring_generators
    if len(target_names) != len(expected_source_order) or len(set(target_names)) != len(target_names):
        raise PreflightError("declared coefficient-ring generator mismatch")
    try:
        images = tuple(algebra.parse_mv(expr, target_names) for expr in manifest.map_images)
    except (TypeError, ValueError) as exc:
        raise PreflightError(f"ring-map image failure: {exc}") from exc
    if len(images) != len(expected_source_order):
        raise PreflightError("ring-map image count mismatch")
    image_indices = tuple(_variable_index(image) for image in images)
    if None in image_indices or set(image_indices) != set(range(len(target_names))):
        raise PreflightError("ring map must be an explicit generator isomorphism")
    checks.append("ring-field-order-map")

    mapped_root = {
        degree: _map_mv(coefficient, source_names, images[:-1], target_names)
        for degree, coefficient in root.items()
    }
    emitted_degrees = tuple(slot.degree for slot in manifest.reduced_root)
    expected_degrees = tuple(sorted(mapped_root, reverse=True))
    if emitted_degrees != expected_degrees:
        raise PreflightError("reduced-root coefficient degree/order mismatch")
    emitted_root = {}
    for slot in manifest.reduced_root:
        try:
            emitted_root[slot.degree] = algebra.parse_mv(slot.expression, target_names)
        except (TypeError, ValueError) as exc:
            raise PreflightError(f"reduced-root coefficient parse failure: {exc}") from exc
        if emitted_root[slot.degree] != mapped_root[slot.degree]:
            raise PreflightError(f"reduced-root exact diff failed at t^{slot.degree}")
    checks.append("reduced-approximate-root")

    closed_names = tuple(
        f"g_{degree}" for degree in range(cell.closed_hi, cell.closed_lo - 1, -1)
    )
    open_name = f"open_g_{cell.open_degree}"
    expected_order = closed_names + (open_name,)
    if manifest.generator_order != expected_order:
        raise PreflightError("ideal generator-order mismatch")
    if tuple(slot.name for slot in manifest.ideal_generators) != expected_order:
        raise PreflightError("ideal emission order does not match generator_order")
    condition_by_name = {slot.name: slot.expression for slot in manifest.ideal_generators}
    if len(condition_by_name) != len(manifest.ideal_generators):
        raise PreflightError("duplicate ideal generator name")
    for degree, name in zip(
        range(cell.closed_hi, cell.closed_lo - 1, -1), closed_names
    ):
        try:
            encoded = algebra.parse_mv(condition_by_name[name], target_names)
        except (TypeError, ValueError) as exc:
            raise PreflightError(f"encoded condition {name} failed to parse: {exc}") from exc
        if encoded != emitted_root.get(degree) or encoded != mapped_root.get(degree):
            raise PreflightError(f"exact coefficient diff failed for {name}")
    checks.append("encoded-coefficient-exact-diff")

    if len(manifest.open_factors) != 1:
        raise PreflightError("exactly one corrected leading-coefficient open is required")
    opened = manifest.open_factors[0]
    if opened.name != f"g_{cell.open_degree}" or opened.equation_name != open_name:
        raise PreflightError("open-factor name/degree mismatch")
    try:
        factor = algebra.parse_mv(opened.expression, target_names)
        inverse = algebra.parse_mv(opened.inverse, target_names)
        open_equation = algebra.parse_mv(condition_by_name[open_name], target_names)
    except (TypeError, ValueError) as exc:
        raise PreflightError(f"open-factor parse/ring failure: {exc}") from exc
    expected_factor = emitted_root.get(cell.open_degree)
    if expected_factor is None or factor != expected_factor or factor.is_zero():
        raise PreflightError("open factor is not the corrected leading coefficient")
    if inverse != images[-1]:
        raise PreflightError("open inverse does not match the declared ring map")
    if open_equation != inverse * factor - 1:
        raise PreflightError("Rabinowitsch open equation mismatch")
    checks.append("open-factor-rabinowitsch")

    _validate_source_fidelity(manifest.source_fidelity)
    checks.append("source-fidelity-EQ2_even")
    validate_typed_output(manifest.output)
    for transition in manifest.transitions:
        validate_transition(transition)
    subsystem = TypedOutput(Artifact.SUBSYSTEM_POINT, Attainment.REALIZED)
    full_eo = TypedOutput(Artifact.FULL_EO_POINT, Attainment.REALIZED)
    pullback = TypedOutput(Artifact.FULL_EO_POINT, Attainment.ADMISSIBLE_PULLBACK)
    actual_map = TypedOutput(Artifact.POLYNOMIAL_PAIR, Attainment.ACTUAL_MAP)
    counterexample = TypedOutput(
        Artifact.POLYNOMIAL_PAIR, Attainment.COUNTEREXAMPLE_CERTIFIED
    )
    required_paths = {
        full_eo: (subsystem, full_eo),
        pullback: (subsystem, full_eo, pullback),
        actual_map: (subsystem, full_eo, pullback, actual_map),
        counterexample: (subsystem, full_eo, pullback, actual_map, counterexample),
    }
    if not manifest.transitions:
        if manifest.output in required_paths:
            raise PreflightError("advanced output has no checked provenance path")
    else:
        for previous, following in zip(manifest.transitions, manifest.transitions[1:]):
            if previous.target != following.source:
                raise PreflightError("transition path is not contiguous in typed state")
            if previous.target_domain != following.source_domain:
                raise PreflightError("transition path is not contiguous in domain")
            if previous.target_scope != following.source_scope:
                raise PreflightError("transition path is not contiguous in scope")
        if manifest.transitions[-1].target != manifest.output:
            raise PreflightError("manifest output is not the end of its transition path")
        required_states = required_paths.get(manifest.output)
        if required_states is not None:
            actual_states = (manifest.transitions[0].source,) + tuple(
                transition.target for transition in manifest.transitions
            )
            if actual_states != required_states:
                raise PreflightError(
                    "advanced output does not follow the complete subsystem-to-output ladder"
                )
            if any(
                transition.source_domain != "A2"
                or transition.target_domain != "A2"
                or transition.source_scope != "GLOBAL"
                or transition.target_scope != "GLOBAL"
                for transition in manifest.transitions
            ):
                raise PreflightError(
                    "advanced output provenance must remain in the global A2 workflow"
                )
    checks.append("typed-output-transitions")


def run_builtin_canaries() -> Tuple[bool, Tuple[str, ...]]:
    """Run exact 86A-negative, 96B-positive, and EQ2 omission controls."""
    messages = []
    try:
        names86, g86 = algebra.expand_g86(algebra.AUX_A)
        point86 = algebra._charged_a_point()
        raw_names86, raw86 = algebra.expand_g86(())
        old_closed = [
            algebra.subst_mv(
                algebra.coeff_t(raw86, degree, raw_names86), point86
            ).as_constant()
            for degree in (21, 19, 17, 15, 13)
        ]
        old_open = algebra.subst_mv(
            algebra.coeff_t(raw86, 11, raw_names86), point86
        ).as_constant()
        if any(value != 0 for value in old_closed) or old_open == 0:
            raise PreflightError("charged (8,6,19) point is not an old-86A positive")
        corrected_point = {**point86, "a22": Fraction(4), "a20": Fraction(6)}
        corrected_top = [
            algebra.subst_mv(
                algebra.coeff_t(g86, degree, names86), corrected_point
            ).as_constant()
            for degree in (22, 21, 20)
        ]
        residual = algebra.subst_mv(
            algebra.coeff_t(g86, 19, names86),
            corrected_point,
        ).as_constant()
        if any(value != 0 for value in corrected_top) or residual != 11:
            raise PreflightError(
                f"86A canary did not reduce to degree 19 with residual 11: "
                f"top={corrected_top!r}, g19={residual!r}"
            )
        messages.append("86A-rejects-old-(8,6,19)")

        names96, g96 = algebra.expand_g96(algebra.AUX_96)
        point96 = {
            "A": 0, "P6": 0, "B": 12, "P4": 0, "C": 0, "P2": 0,
            "D": 24, "a": 0, "Q3": 0, "b": 8, "Q1": 0,
            "a15": 0, "a12": 0, "a9": 0, "a6": -64,
        }
        closed = [
            algebra.subst_mv(algebra.coeff_t(g96, degree, names96), point96).as_constant()
            for degree in range(16, 2, -1)
        ]
        leading = algebra.subst_mv(
            algebra.coeff_t(g96, 2, names96), point96
        ).as_constant()
        if any(value != 0 for value in closed) or leading != 64:
            raise PreflightError("96B four-node curve failed corrected membership")
        messages.append("96B-accepts-four-node-(9,6,2)")

        corrected = SourceFidelity(
            ("oldEQ2", "q", "E1"), "oldEQ2", "q", "E1",
            "oldEQ2-2*q*E1",
        )
        stale = SourceFidelity(
            ("oldEQ2", "q", "E1"), "oldEQ2", "q", "E1", "oldEQ2"
        )
        _validate_source_fidelity(corrected)
        try:
            _validate_source_fidelity(stale)
        except PreflightError:
            pass
        else:
            raise PreflightError("missing -2*q*E1 source canary was accepted")
        messages.append("EQ2_even-omission-rejected")
    except Exception as exc:
        return False, tuple(messages + [f"{type(exc).__name__}: {exc}"])
    return True, tuple(messages)


def probe_default_stack() -> StackObservation:
    packages: Dict[str, Optional[str]] = {}
    for package in EXPECTED_PACKAGES:
        try:
            packages[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            packages[package] = None
    binary = shutil.which("msolve")
    version = None
    if binary:
        try:
            completed = subprocess.run(
                [binary, "--version"], capture_output=True, text=True,
                timeout=2.0, check=False,
            )
            line = (completed.stdout or completed.stderr).strip().splitlines()
            if completed.returncode == 0 and line:
                version = line[0]
        except (OSError, subprocess.SubprocessError):
            version = None
    return StackObservation(packages, version, binary)


def _validate_stack(manifest: Manifest, observed: StackObservation) -> None:
    if dict(manifest.package_versions) != EXPECTED_PACKAGES:
        raise PreflightError("manifest package pins differ from the default stack")
    if manifest.msolve_version != EXPECTED_MSOLVE:
        raise PreflightError("manifest msolve pin differs from the default stack")
    if dict(observed.package_versions) != EXPECTED_PACKAGES:
        raise PreflightError(
            f"package version gate failed: observed={dict(observed.package_versions)!r}"
        )
    if observed.msolve_version != EXPECTED_MSOLVE:
        raise PreflightError(
            f"msolve version gate failed: observed={observed.msolve_version!r}"
        )


def render_solver_input(manifest: Manifest) -> bytes:
    """Render the canonical msolve payload represented by a manifest."""
    lines = [",".join(manifest.ring_generators), "0"]
    for index, generator in enumerate(manifest.ideal_generators):
        suffix = "," if index + 1 < len(manifest.ideal_generators) else ""
        lines.append(generator.expression + suffix)
    return ("\n".join(lines) + "\n").encode("utf-8")


def _validate_solver_input(manifest: Manifest, payload: Optional[bytes]) -> None:
    if payload is None:
        raise PreflightError("solver input bytes/path are required for launch approval")
    if not isinstance(payload, bytes):
        raise PreflightError("solver input must be supplied as exact bytes")
    declared = manifest.solver_input_sha256
    if (
        not isinstance(declared, str)
        or len(declared) != 64
        or declared != declared.lower()
        or any(character not in "0123456789abcdef" for character in declared)
    ):
        raise PreflightError("solver_input_sha256 is not canonical lowercase SHA-256")
    observed = hashlib.sha256(payload).hexdigest()
    if observed != declared:
        raise PreflightError(
            f"solver input SHA-256 mismatch: observed={observed} declared={declared}"
        )
    if not payload.endswith(b"\n") or b"\r" in payload or b"\x00" in payload:
        raise PreflightError("solver input must be NUL-free POSIX text with a final LF")
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise PreflightError(f"solver input is not UTF-8: {exc}") from exc
    lines = text.splitlines()
    if len(lines) < 3:
        raise PreflightError("solver input is missing ring, characteristic, or generators")
    if tuple(lines[0].split(",")) != manifest.ring_generators:
        raise PreflightError("solver input variable line/order differs from manifest")
    if lines[1] != "0":
        raise PreflightError("solver input characteristic is not declared QQ/0")
    encoded_rows = lines[2:]
    if len(encoded_rows) != len(manifest.ideal_generators):
        raise PreflightError("solver input generator count differs from manifest")
    parsed_rows = []
    for index, line in enumerate(encoded_rows):
        if not line or line != line.strip():
            raise PreflightError(f"solver input generator row {index} is empty/padded")
        is_last = index + 1 == len(encoded_rows)
        if is_last:
            if line.endswith(","):
                raise PreflightError("final solver generator must not have a trailing comma")
            expression = line
        else:
            if not line.endswith(",") or line.endswith(",,"):
                raise PreflightError("nonfinal solver generator must have one trailing comma")
            expression = line[:-1]
        try:
            parsed_rows.append(algebra.parse_mv(expression, manifest.ring_generators))
        except (TypeError, ValueError) as exc:
            raise PreflightError(f"solver input generator {index} failed to parse: {exc}") from exc
    for index, (parsed, declared_generator) in enumerate(
        zip(parsed_rows, manifest.ideal_generators)
    ):
        try:
            expected = algebra.parse_mv(
                declared_generator.expression, manifest.ring_generators
            )
        except (TypeError, ValueError) as exc:
            raise PreflightError(
                f"manifest solver generator {index} failed to parse: {exc}"
            ) from exc
        if parsed != expected:
            raise PreflightError(
                f"solver input generator {index} differs polynomially from manifest"
            )



def preflight(
    manifest: Manifest,
    *,
    solver_input: Optional[bytes] = None,
    stack_observation: Optional[StackObservation] = None,
) -> PreflightResult:
    """Validate a manifest against exact solver bytes; probe the real stack by default."""
    checks: list[str] = []
    try:
        _validate_manifest(manifest, checks)
        _validate_solver_input(manifest, solver_input)
        checks.append("solver-input-sha256-and-rows")
        canaries_ok, canary_messages = run_builtin_canaries()
        if not canaries_ok:
            raise PreflightError("built-in semantic canary failed: " + "; ".join(canary_messages))
        checks.extend(canary_messages)
        observed = stack_observation if stack_observation is not None else probe_default_stack()
        _validate_stack(manifest, observed)
        checks.append("default-stack-pins")
    except Exception as exc:
        return PreflightResult(
            False, getattr(manifest, "job_id", "<unparsed>"), tuple(checks),
            (f"{type(exc).__name__}: {exc}",), getattr(manifest, "output", None),
        )
    return PreflightResult(True, manifest.job_id, tuple(checks), (), manifest.output)


def _open_equation(factor: str, inverse: str, names: Tuple[str, ...]) -> str:
    fpoly = algebra.parse_mv(factor, names)
    ipoly = algebra.parse_mv(inverse, names)
    return algebra.render_mv(ipoly * fpoly - 1)


def build_reference_manifest(
    cell_name: str = "96B",
    *,
    degree_n: int = 6,
    output: TypedOutput = TypedOutput(Artifact.CURVE, Attainment.REALIZED),
) -> Manifest:
    """Construct a faithful in-memory manifest; useful to generators/tests."""
    cell = CELLS[cell_name]
    source_names, root = _expand(cell)
    target_names = source_names + ("u",)
    reduced_root = tuple(
        RootCoefficient(degree, algebra.render_mv(root[degree]))
        for degree in sorted(root, reverse=True)
    )
    ideal = []
    order = []
    for degree in range(cell.closed_hi, cell.closed_lo - 1, -1):
        name = f"g_{degree}"
        order.append(name)
        ideal.append(PolynomialSlot(name, algebra.render_mv(root[degree])))
    factor_name = f"g_{cell.open_degree}"
    factor = algebra.render_mv(root[cell.open_degree])
    equation_name = f"open_g_{cell.open_degree}"
    order.append(equation_name)
    ideal.append(
        PolynomialSlot(equation_name, _open_equation(factor, "u", target_names))
    )
    draft = Manifest(
        SCHEMA_VERSION, f"reference-{cell_name}", degree_n, cell_name, "QQ",
        "GRevLex", target_names, target_names, target_names, reduced_root,
        tuple(ideal), tuple(order), "",
        (OpenFactor(factor_name, factor, "u", equation_name),),
        SourceFidelity(
            ("oldEQ2", "q", "E1"), "oldEQ2", "q", "E1",
            "oldEQ2-2*q*E1",
        ),
        output, (), dict(EXPECTED_PACKAGES), EXPECTED_MSOLVE,
    )
    return replace(
        draft,
        solver_input_sha256=hashlib.sha256(render_solver_input(draft)).hexdigest(),
    )


def manifest_to_dict(manifest: Manifest) -> Dict[str, Any]:
    def typed(value: TypedOutput) -> Dict[str, str]:
        return {"artifact": value.artifact.value, "attainment": value.attainment.value}

    return {
        "schema_version": manifest.schema_version,
        "job_id": manifest.job_id,
        "degree_n": manifest.degree_n,
        "cell": manifest.cell,
        "coefficient_field": manifest.coefficient_field,
        "monomial_order": manifest.monomial_order,
        "ring_generators": list(manifest.ring_generators),
        "ring_map": {
            "source_order": list(manifest.map_source_order),
            "images": list(manifest.map_images),
        },
        "reduced_root": [
            {"degree": slot.degree, "expression": slot.expression}
            for slot in manifest.reduced_root
        ],
        "ideal_generators": [
            {"name": slot.name, "expression": slot.expression}
            for slot in manifest.ideal_generators
        ],
        "generator_order": list(manifest.generator_order),
        "solver_input_sha256": manifest.solver_input_sha256,
        "open_factors": [vars(item) for item in manifest.open_factors],
        "source_fidelity": {
            "ring_generators": list(manifest.source_fidelity.ring_generators),
            "old_eq2": manifest.source_fidelity.old_eq2,
            "q": manifest.source_fidelity.q,
            "e1": manifest.source_fidelity.e1,
            "encoded_eq2_even": manifest.source_fidelity.encoded_eq2_even,
        },
        "output": typed(manifest.output),
        "transitions": [
            {
                "source": typed(item.source), "target": typed(item.target),
                "source_domain": item.source_domain,
                "target_domain": item.target_domain,
                "source_scope": item.source_scope, "target_scope": item.target_scope,
                "claim": item.claim,
                "arrows": [arrow.value for arrow in item.arrows],
            }
            for item in manifest.transitions
        ],
        "stack": {
            "packages": dict(manifest.package_versions),
            "msolve": manifest.msolve_version,
        },
    }


def _json_object(value: Any, keys: Iterable[str], label: str) -> Mapping[str, Any]:
    expected = set(keys)
    if not isinstance(value, Mapping) or any(not isinstance(k, str) for k in value):
        raise PreflightError(f"{label} must be a JSON object")
    actual = set(value)
    if actual != expected:
        raise PreflightError(
            f"{label} keys mismatch: missing={sorted(expected-actual)} "
            f"extra={sorted(actual-expected)}"
        )
    return value


def _json_array(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise PreflightError(f"{label} must be a JSON array")
    return value


def _json_string(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise PreflightError(f"{label} must be a string")
    return value


def _json_integer(value: Any, label: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise PreflightError(f"{label} must be an integer")
    return value


def _json_strings(value: Any, label: str) -> Tuple[str, ...]:
    return tuple(
        _json_string(item, f"{label}[{index}]")
        for index, item in enumerate(_json_array(value, label))
    )


def _typed_from_json(value: Any, label: str) -> TypedOutput:
    item = _json_object(value, {"artifact", "attainment"}, label)
    return TypedOutput(
        Artifact(_json_string(item["artifact"], f"{label}.artifact")),
        Attainment(_json_string(item["attainment"], f"{label}.attainment")),
    )


def manifest_from_dict(raw: Mapping[str, Any]) -> Manifest:
    """Parse the strict JSON contract without primitive-value coercions."""
    required = {
        "schema_version", "job_id", "degree_n", "cell", "coefficient_field",
        "monomial_order", "ring_generators", "ring_map", "reduced_root",
        "ideal_generators", "generator_order", "solver_input_sha256", "open_factors",
        "source_fidelity", "output", "transitions", "stack",
    }
    top = _json_object(raw, required, "manifest")
    try:
        ring_map = _json_object(
            top["ring_map"], {"source_order", "images"}, "ring_map"
        )
        source = _json_object(
            top["source_fidelity"],
            {"ring_generators", "old_eq2", "q", "e1", "encoded_eq2_even"},
            "source_fidelity",
        )
        stack = _json_object(top["stack"], {"packages", "msolve"}, "stack")
        packages_raw = _json_object(
            stack["packages"], set(EXPECTED_PACKAGES), "stack.packages"
        )
        packages = {
            name: _json_string(packages_raw[name], f"stack.packages.{name}")
            for name in EXPECTED_PACKAGES
        }
        roots = []
        for index, value in enumerate(_json_array(top["reduced_root"], "reduced_root")):
            item = _json_object(value, {"degree", "expression"}, f"reduced_root[{index}]")
            roots.append(
                RootCoefficient(
                    _json_integer(item["degree"], f"reduced_root[{index}].degree"),
                    _json_string(item["expression"], f"reduced_root[{index}].expression"),
                )
            )
        ideals = []
        for index, value in enumerate(_json_array(top["ideal_generators"], "ideal_generators")):
            item = _json_object(value, {"name", "expression"}, f"ideal_generators[{index}]")
            ideals.append(
                PolynomialSlot(
                    _json_string(item["name"], f"ideal_generators[{index}].name"),
                    _json_string(item["expression"], f"ideal_generators[{index}].expression"),
                )
            )
        opens = []
        open_keys = {"name", "expression", "inverse", "equation_name"}
        for index, value in enumerate(_json_array(top["open_factors"], "open_factors")):
            item = _json_object(value, open_keys, f"open_factors[{index}]")
            opens.append(
                OpenFactor(*(
                    _json_string(item[name], f"open_factors[{index}].{name}")
                    for name in ("name", "expression", "inverse", "equation_name")
                ))
            )
        transitions = []
        transition_keys = {
            "source", "target", "source_domain", "target_domain",
            "source_scope", "target_scope", "claim", "arrows",
        }
        for index, value in enumerate(_json_array(top["transitions"], "transitions")):
            label = f"transitions[{index}]"
            item = _json_object(value, transition_keys, label)
            transitions.append(
                Transition(
                    _typed_from_json(item["source"], f"{label}.source"),
                    _typed_from_json(item["target"], f"{label}.target"),
                    _json_string(item["source_domain"], f"{label}.source_domain"),
                    _json_string(item["target_domain"], f"{label}.target_domain"),
                    _json_string(item["source_scope"], f"{label}.source_scope"),
                    _json_string(item["target_scope"], f"{label}.target_scope"),
                    _json_string(item["claim"], f"{label}.claim"),
                    tuple(
                        Arrow(value)
                        for value in _json_strings(item["arrows"], f"{label}.arrows")
                    ),
                )
            )
        return Manifest(
            _json_integer(top["schema_version"], "schema_version"),
            _json_string(top["job_id"], "job_id"),
            _json_integer(top["degree_n"], "degree_n"),
            _json_string(top["cell"], "cell"),
            _json_string(top["coefficient_field"], "coefficient_field"),
            _json_string(top["monomial_order"], "monomial_order"),
            _json_strings(top["ring_generators"], "ring_generators"),
            _json_strings(ring_map["source_order"], "ring_map.source_order"),
            _json_strings(ring_map["images"], "ring_map.images"),
            tuple(roots), tuple(ideals),
            _json_strings(top["generator_order"], "generator_order"),
            _json_string(top["solver_input_sha256"], "solver_input_sha256"),
            tuple(opens),
            SourceFidelity(
                _json_strings(source["ring_generators"], "source_fidelity.ring_generators"),
                _json_string(source["old_eq2"], "source_fidelity.old_eq2"),
                _json_string(source["q"], "source_fidelity.q"),
                _json_string(source["e1"], "source_fidelity.e1"),
                _json_string(source["encoded_eq2_even"], "source_fidelity.encoded_eq2_even"),
            ),
            _typed_from_json(top["output"], "output"), tuple(transitions),
            packages, _json_string(stack["msolve"], "stack.msolve"),
        )
    except (KeyError, TypeError, ValueError) as exc:
        if isinstance(exc, PreflightError):
            raise
        raise PreflightError(f"invalid manifest structure: {exc}") from exc


def _reject_duplicate_json_keys(pairs: Sequence[Tuple[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise PreflightError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def manifest_from_json(source: str) -> Manifest:
    """Load the strict contract, rejecting duplicate keys at every depth."""
    try:
        raw = json.loads(source, object_pairs_hook=_reject_duplicate_json_keys)
    except (json.JSONDecodeError, TypeError) as exc:
        raise PreflightError(f"invalid JSON: {exc}") from exc
    return manifest_from_dict(raw)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", help="preflight JSON emitted by the generator")
    parser.add_argument("solver_input", nargs="?", help="exact .ms file that would be launched")
    parser.add_argument(
        "--self-test", action="store_true",
        help="run the pure exact built-in canaries only (does not approve launch)",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        ok, messages = run_builtin_canaries()
        print(json.dumps({"ok": ok, "checks": messages}, indent=2))
        return 0 if ok else 1
    if not args.manifest or not args.solver_input:
        parser.error("manifest and solver_input are required unless --self-test is used")
    try:
        manifest = manifest_from_json(Path(args.manifest).read_text(encoding="utf-8"))
        result = preflight(
            manifest, solver_input=Path(args.solver_input).read_bytes()
        )
    except Exception as exc:
        result = PreflightResult(False, "<unparsed>", (), (f"{type(exc).__name__}: {exc}",), None)
    print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
