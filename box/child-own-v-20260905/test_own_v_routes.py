#!/usr/bin/env python3
"""Source-image and stabilizer controls for necessary-tree compatibility."""
import sys,unittest,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];sys.path.insert(0,str(ROOT/'box/lib'))
from own_v_routes import OwnVRouteTree
spec=importlib.util.spec_from_file_location('test_source_route_B','/tmp/jc2-lane.wwyG4k/inputs/moh_skeleton_full.py');B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)

def tree(n,m,Ms,V):return OwnVRouteTree(B.Skel(n,m,Ms,V))

class OwnRouteTests(unittest.TestCase):
    def test_moh_five(self):
        rows=[(64,48,[52,62],{2:3,3:3}),(84,56,[64,82],{2:2,3:3}),
              (84,56,[72,82],{2:5,3:3}),(75,50,[55,73],{2:3,3:4}),
              (75,50,[55,73],{2:2,3:4})]
        for row in rows:
            with self.subTest(row=row):self.assertIsNotNone(tree(*row).compatible_first_support(2))
    def test_gate180_zero_sheds_no_denominator(self):
        T=tree(180,120,[132,150,178],{2:2,3:4,4:5})
        a=T.compatible_first_support(2)
        self.assertIsNotNone(a);self.assertEqual(a['mode'],'zero');self.assertEqual(a['A'],6)
        b=a['selected_child'];self.assertEqual(b['centre_L'],1);self.assertEqual(b['A'],5)
        c=b['selected_child'];self.assertEqual(c['centre_L'],5);self.assertEqual(c['A1'],3)
        self.assertIsNone(T.compatible_first_support(3))
    def test_gate180_alternate(self):
        self.assertIsNotNone(tree(180,120,[132,150,178],{2:3,3:4,4:5}).compatible_first_support(2))
    def test_gate96_incompatible_full_stabilizer(self):
        T=tree(96,72,[36,78,94],{2:4,3:3,4:5})
        self.assertIsNone(T.compatible_first_support(2));self.assertIsNone(T.compatible_first_support(3))
    def test_168_compulsory_zero_sibling(self):
        T=tree(168,112,[84,156,166],{2:1,3:5,4:3})
        self.assertIsNone(T.compatible_first_support(2));self.assertIsNone(T.compatible_first_support(3))
    def test_192_no_complete_necessary_tree(self):
        T=tree(192,128,[160,172,190],{2:3,3:3,4:3})
        self.assertIsNone(T.compatible_first_support(2));self.assertIsNone(T.compatible_first_support(3))

if __name__=='__main__':unittest.main()
