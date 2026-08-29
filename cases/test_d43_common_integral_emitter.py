#!/usr/bin/env python3
"""Light tests for the fail-closed D43 common-integral preflight core."""

import json
import os
import sys
import unittest
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d43_common_integral_emitter as E


class RadicalRingTests(unittest.TestCase):
    def test_literal_relations_and_rank(self):
        z = E.RadicalCoefficient.generator("zeta42")
        r = E.RadicalCoefficient.generator("r3")
        a1 = E.RadicalCoefficient.generator("A1")
        a2 = E.RadicalCoefficient.generator("A2")
        h = E.RadicalCoefficient.generator("h")
        phi = sum((coefficient * z ** exponent
                   for exponent, coefficient in enumerate(E.PHI42)),
                  E.RadicalCoefficient())
        self.assertFalse(phi)
        self.assertEqual(r ** 2, 3)
        self.assertEqual(a1 ** 3, 3 + r)
        self.assertEqual(a2 ** 3, 3 - r)
        self.assertEqual(2 * h ** 2, 3)
        self.assertEqual(E.BASIS_RANK, 432)

    def test_registered_specializations_and_atlas_frame(self):
        for prime, frame in E.REGISTERED_FRAMES.items():
            gates = E.validate_registered_prime(prime)
            self.assertEqual(gates["order_tests"][42], 1)
            atlas_path = os.path.join(HERE, "d23_atlas_p%d.json" % prime)
            with open(atlas_path) as handle:
                fiber = json.load(handle)["fibers"]["a00pp"]["fiber"]
            self.assertEqual(frame.A1, int(fiber["A1"]))
            self.assertEqual(frame.A2, int(fiber["A2"]))
            self.assertEqual(frame.h, int(fiber["HW1_over_W1"]))
            self.assertEqual(frame.h, int(fiber["HW2_over_W2"]))

    def test_hensel_frame_reduces_to_registered_frame(self):
        prime = 105337
        modulus = prime ** 2
        E.validate_specialization(modulus, E.REGISTERED_P2_FRAME_105337,
                                  E.SOURCE_NEWTON_DENOMINATORS)
        self.assertEqual(E.REGISTERED_P2_FRAME_105337.reduced(prime),
                         E.REGISTERED_FRAMES[prime])

    def test_negative_specialization_controls(self):
        frame = E.REGISTERED_FRAMES[105337]
        with self.assertRaises(E.SpecializationError):
            E.validate_specialization(105337,
                                      E.RootFrame(1, frame.r3, frame.A1,
                                                  frame.A2, frame.h))
        with self.assertRaises(E.SpecializationError):
            E.validate_specialization(105337, frame, [105337])
        with self.assertRaises(E.SpecializationError):
            E.validate_registered_prime(105337,
                                        E.RootFrame(frame.zeta42, frame.r3,
                                                    frame.A1 + 1, frame.A2,
                                                    frame.h))

    def test_r1_ring_collapse_is_literal_a00pp_substitution(self):
        source = {
            # z^5*A1^2*A2*W1^3*HW1*W2^4 * (1/2 + 2*r3/3)
            (5, 2, 1, 3, 1, 4, 0, 0):
                (Fraction(1, 2), Fraction(2, 3)),
        }
        collapsed = E.collapse_r1_ring_element(source)
        self.assertEqual(set(collapsed), {(4, 4)})
        for prime, frame in E.REGISTERED_FRAMES.items():
            w1, w2 = 7, 11
            got = collapsed[(4, 4)].specialize(prime, frame)
            got = got * pow(w1, 4, prime) * pow(w2, 4, prime) % prime
            scalar = (pow(2, -1, prime) +
                      2 * frame.r3 * pow(3, -1, prime)) % prime
            want = scalar * pow(frame.zeta42, 5, prime) % prime
            want = want * pow(frame.A1, 2, prime) * frame.A2 % prime
            want = want * pow(w1, 3, prime) * (frame.h * w1) % prime
            want = want * pow(w2, 4, prime) % prime
            self.assertEqual(got, want)
        with self.assertRaises(ValueError):
            E.collapse_r1_ring_element({(0, 0, 0, 0, 0, 0, 0, 1): (1, 0)})

    def test_bundle_is_fail_closed(self):
        bundle = E.CertificationBundle()
        self.assertIn(
            "missing source gate "
            "common_coordinate_registry_and_source_descent",
            bundle.source_readiness_errors())
        with self.assertRaises(E.BundleNotReady):
            bundle.seal_source()
        with self.assertRaises(E.BundleNotReady):
            bundle.seal_presentation_equivalence()
        digest = "0" * 64
        with self.assertRaises(ValueError):
            bundle.add("reducers", "G0", digest, digest)
        with self.assertRaises(ValueError):
            bundle.add("parked", "g0", digest, digest, digest,
                       kind="d23_compat")
        with self.assertRaises(KeyError):
            bundle.add_source_gate("common_coordinate_registry", digest)


if __name__ == "__main__":
    unittest.main()
