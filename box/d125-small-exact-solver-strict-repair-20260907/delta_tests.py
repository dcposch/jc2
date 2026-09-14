"""Two exact strict-stream regressions; only sealed tiny engine output is read."""
import importlib.util
import json
from pathlib import Path
import unittest
import exact as NEW
import driver

BASE=Path(__file__).resolve().parents[1]
OLD_PATH=BASE/'d125-small-exact-solver-code-prep-20260907/exact.py'
ACTUAL=BASE/'d125-small-exact-solver-engineering-20260907/evidence/control.stdout'
OLD_SHA='ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3'
ACTUAL_SHA='fff5dfd6b2be427844ea898b95c8e159937761085ec2905b0327dc6871939922'
NEW.need(NEW.digest(OLD_PATH.read_bytes())==OLD_SHA,'old code drift')
spec=importlib.util.spec_from_file_location('old_exact',OLD_PATH)
OLD=importlib.util.module_from_spec(spec);spec.loader.exec_module(OLD)
DATA=ACTUAL.read_bytes();NEW.need(NEW.digest(DATA)==ACTUAL_SHA,'sealed actual output drift')
SOURCE=DATA.decode().splitlines()[0].split()[2]
OBS=[]


class DeltaTests(unittest.TestCase):
    def refutation(self,name,data,stderr,variables=['x'],source=SOURCE):
        accepted=OLD.parse_result(data,stderr,variables,source)
        self.assertEqual(len(accepted),3)
        with self.assertRaises(ValueError):NEW.parse_result(data,stderr,variables,source)
        OBS.append({'control':name,'old_accepted':True,'new_rejected':True})

    def test_whitespace_stderr_actual(self):
        self.refutation('actual_whitespace_stderr',DATA,b' \n\t')

    def test_downward_size_actual(self):
        self.refutation('actual_size_3_to_0',DATA.replace(b'I_SIZE 3\n',b'I_SIZE 0\n'),b'')

    def test_downward_size_two_nonzero(self):
        from test_exact import result
        data=result(['x','1-x'],['1'],['1','1'],variables=['x'])
        self.refutation('two_nonzero_size_2_to_0',data.replace(b'I_SIZE 2\n',b'I_SIZE 0\n'),b'',source='a'*64)

    def test_actual_zero_duplicate_control_remains_valid(self):
        for module in (OLD,NEW):
            engine,basis,cofactors=module.parse_result(DATA,b'',['x'],SOURCE)
            self.assertEqual(len(engine),6);self.assertEqual(sum(bool(row) for row in engine),3)
            self.assertEqual(len(cofactors),6)
            rows=[module.polynomial(t,['x']) for t in driver.CONTROL_TEXT]
            verdict,mapping,lifted=module.unit_certificate(rows,engine,cofactors)
            self.assertEqual(mapping,[0,1,0,1,4,0]);self.assertEqual(len(lifted),6)
            self.assertIn('UNIT_COFACTOR',verdict)
        self.assertEqual(driver.check_control(DATA,b'')['original_rows'],6)


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(DeltaTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({'optimized':not __debug__,'tests':result.testsRun,'pass':result.wasSuccessful(),
                      'old_sha256':OLD_SHA,'new_sha256':NEW.digest(Path(NEW.__file__).read_bytes()),
                      'actual_stdout_sha256':ACTUAL_SHA,'observations':OBS},sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)
