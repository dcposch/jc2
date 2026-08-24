#!/usr/bin/env python3
"""Portable exact cache for the constant TD6 transport response.

The cache stores only the x-band and pole jets consumed by the staged B
pencil.  ``build_cache_data`` reconstructs them from the frozen 3,602-column
transport system; the fast replay deserializes the checked-in canonical JSON.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
REPO = Path(os.environ.get("JC2_REPO", HERE.parents[1]))
QDUAL_PATH = REPO / "cases/td6_jet_orbit_adjoint_20260824/replay.py"
QDUAL_SHA256 = "fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198"
CACHE_PATH = HERE / "transport_sections.json"
CACHE_FORMAT = "TD6-QB-AFFINE-TRANSPORT-SECTIONS-v1"


def load(name, path, expected):
    assert sha256(path.read_bytes()).hexdigest() == expected, path
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


qd = load("td6_qdual_cache", QDUAL_PATH, QDUAL_SHA256)
E, K, nr, fb = qd.E, qd.K, qd.nr, qd.fb
DUAL_CLASS = qd.Dual
NF = 16 * 61


def fraction_text(value):
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


def fraction_value(text):
    return Q(text)


def e_data(value):
    value = E(value)
    return [
        [fraction_text(coefficient) for coefficient in kvalue.coefficients]
        for kvalue in value.coefficients
    ]


def e_value(data):
    return E([K([fraction_value(value) for value in row]) for row in data])


def dual_parts(value):
    value = value if isinstance(value, DUAL_CLASS) else DUAL_CLASS(value)
    return value.value, value.derivative


def form_data(form):
    constant, coefficients = form
    base, linear = dual_parts(constant)
    return {
        "base": e_data(base),
        "linear": e_data(linear),
        "directions": [
            [parameter, fraction_text(coefficient)]
            for parameter, coefficient in sorted(coefficients.items())
        ],
    }


def form_value(data):
    return (
        e_value(data["base"]),
        e_value(data["linear"]),
        {
            int(parameter): fraction_value(coefficient)
            for parameter, coefficient in data["directions"]
        },
    )


def section_forms(forms132):
    bands = {
        f"{owner}{exponent}": nr.x_band_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            forms132,
            0 if owner == "f" else NF,
        )
        for owner in ("f", "g")
        for exponent in (1, 2, 3)
    }
    bands["pole_f1"] = [
        nr.combine_global_linear(
            nr.pole_coefficient(15, 60, -2, degree), forms132, 0
        )
        for degree in range(61)
    ]
    bands["pole_g1"] = [
        nr.combine_global_linear(
            nr.pole_coefficient(25, 100, -4, degree), forms132, NF
        )
        for degree in range(101)
    ]
    return bands


def build_cache_data():
    fb.CENTER = (Q(1), Q(1), Q(1))
    fb._X_POWER_CACHE.clear()
    nf, ng, transport = qd.build_transport_rows()
    pivots, records = qd.uniform.mu.factor_matrix(transport)
    rhs, compatibility = qd.propagate(records)
    assert not compatibility
    forms132, free132 = qd.direction_parameterization(nf + ng, pivots, rhs)
    assert (nf + ng, len(pivots), len(free132)) == (3602, 3470, 132)
    sections = section_forms(forms132)
    return {
        "format": CACHE_FORMAT,
        "source": {
            "qdual_path": "cases/td6_jet_orbit_adjoint_20260824/replay.py",
            "qdual_sha256": QDUAL_SHA256,
            "transport_rank": [3470, 3602],
            "transport_dimension": 132,
        },
        "sections": {
            key: [form_data(form) for form in forms]
            for key, forms in sorted(sections.items())
        },
    }


def canonical_bytes(data):
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode()


def load_cache(path=CACHE_PATH):
    raw = path.read_bytes()
    data = json.loads(raw)
    assert raw == canonical_bytes(data), "cache is not canonical JSON"
    assert data["format"] == CACHE_FORMAT
    assert data["source"]["qdual_sha256"] == QDUAL_SHA256
    assert data["source"]["transport_rank"] == [3470, 3602]
    assert data["source"]["transport_dimension"] == 132
    sections = {
        key: [form_value(form) for form in forms]
        for key, forms in data["sections"].items()
    }
    assert {key: len(value) for key, value in sections.items()} == {
        "f1": 16,
        "f2": 16,
        "f3": 16,
        "g1": 26,
        "g2": 26,
        "g3": 26,
        "pole_f1": 61,
        "pole_g1": 101,
    }
    return sections, sha256(raw).hexdigest()
