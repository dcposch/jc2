#!/usr/bin/env python3
"""Regression checks for the degree-eight invariant-cell generator."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "cases" / "quartic_invariant_mu2_d8_20260831" / "generate_mu2_d8.py"
SPEC = importlib.util.spec_from_file_location("jc2_mu2_d8_generator", GENERATOR)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import machinery guard
    raise RuntimeError("could not load degree-eight generator")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class QuarticInvariantMu2D8GeneratorTests(unittest.TestCase):
    def test_actual_raw_and_unique_counts(self) -> None:
        text = MODULE.singular_text(32003, "actual", "std")
        self.assertIn("// raw_equation_count=57\n", text)
        self.assertIn("// ideal_generator_count=53\n", text)
        self.assertNotIn("ideal G=slimgb(I);", text)

    def test_target_mutation_adds_unit(self) -> None:
        text = MODULE.singular_text(32003, "target3", "slimgb")
        self.assertIn("// raw_equation_count=58\n", text)
        self.assertIn("// ideal_generator_count=54\n", text)
        self.assertIn("ideal G=slimgb(I);", text)

    def test_drop_last_removes_one_unique_generator(self) -> None:
        text = MODULE.singular_text(32003, "drop_last", "std")
        self.assertIn("// raw_equation_count=57\n", text)
        self.assertIn("// ideal_generator_count=52\n", text)


if __name__ == "__main__":
    unittest.main()
