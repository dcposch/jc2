"""Tiny stdlib checks only. Fixture is reused; no CAS or host authorization."""
import ast,copy,importlib.util,inspect,json,sys,unittest
from pathlib import Path
from unittest.mock import patch
HERE=Path(__file__).resolve().parent
REPAIR=HERE.parent/'d125-hybrid81-caller-repair-20260907'
sys.path.insert(0,str(REPAIR));sys.path.insert(0,str(HERE))
import engine as N
import driver as D
import exact as E
import hybrid as H
sys.path.insert(0,str(HERE.parent/'d125-hybrid81-solver-prep-20260907'))
from test_exact import result
SOL=HERE.parent/'d125-hybrid81-solver-gate-sol56-20260907'
DATA=(SOL/'tiny-engine-fixture.jsonl').read_bytes()
V=['x','y','k','z'];ROWS=['0','x/2','0','x/2','1-x','0','k*z-1']
class EngineeringTests(unittest.TestCase):
    def test_only_fixed_control_binding(self):
        binding={'operation':'hybrid','helper_sha256':'a'*64,'fixture_sha256':N.FIXTURE_SHA,'root_green_sha256':'b'*64}
        a={'mode':'engineering_control','engineering':binding}
        N.control_binding(a,'hybrid','a'*64,'b'*64)
        for op in ('decision','verify','solver','control','../alarm'):
            with self.assertRaises(ValueError):N.control_binding(a,op,'a'*64,'b'*64)
        for bad in ({**a,'mode':'solver'},{**a,'engineering':{}},{**a,'engineering':{**binding,'operation':'alarm'}},{**a,'engineering':{**binding,'helper_sha256':'c'*64}},{**a,'engineering':{**binding,'fixture_sha256':'d'*64}}):
            with self.assertRaises(ValueError):N.control_binding(bad,'hybrid','a'*64,'b'*64)
    def test_exact_fixture_control_footer(self):
        script=N.hybrid_script(DATA);self.assertNotIn('slimgb',script);self.assertIn('ideal G=ideal(1);',script)
        self.assertIn('1+-1*x',script);self.assertEqual(script.count('// '),7)
        v,rows,labels,prefix=H.read_hybrid(DATA);self.assertEqual(script,prefix+D.footer(v,N.FIXTURE_SHA,control=True))
        production=(SOL/'tiny-engine-fixture.sing').read_bytes();self.assertIn(b'slimgb(I)',production)
        self.assertNotEqual(script.encode(),production)
        with self.assertRaises(ValueError):N.hybrid_script(DATA.replace(b'"1","2"',b'"1","3"',1))
    def test_complete_indexed_replay_and_corruptions(self):
        good=result(ROWS,['1'],['0','1','0','1','1','0','0'],variables=V,source=N.FIXTURE_SHA)
        self.assertEqual(N.check_hybrid(DATA,good,b'')['mapping'],[0,1,0,1,4,0,6])
        for changed,stderr in [(good.replace(b'T 5 1',b'T 5 2'),b''),(good.replace(b'I_SIZE 4',b'I_SIZE 0'),b''),(good,b' \n'),(good+b'EXTRA\n',b''),(result(ROWS[:-1],['1'],['0','1','0','1','1','0'],variables=V,source=N.FIXTURE_SHA),b'')]:
            with self.assertRaises(ValueError):N.check_hybrid(DATA,changed,stderr)
    def test_alarm_script_is_small_distinct_and_unexecuted(self):
        s=N.alarm_script();self.assertIn('JC2_HYBRID81_ALARM_READY',s);self.assertIn('while(1)',s)
        self.assertLess(len(s),256)
        for forbidden in ('slimgb','std(','lift(','system(','write(','LIB '):self.assertNotIn(forbidden,s)
    def test_real_local_entry_rejects_before_write(self):
        with patch.object(D,'context',side_effect=RuntimeError('SHOULD_NOT_CONTEXT')),patch.object(D,'write_new') as write:
            for op in ('hybrid','alarm','decision'):
                with self.assertRaises(ValueError):N.payload(op,'NO_AUTHORITY')
            write.assert_not_called()
    def test_no_production_read_or_new_lifecycle(self):
        tree=ast.parse(Path(N.__file__).read_text());self.assertFalse(any(isinstance(x,ast.Assert) for x in ast.walk(tree)))
        text=Path(N.__file__).read_text();self.assertNotIn('D.SOURCE',text);self.assertNotIn('production=True',text)
        for word in ('subprocess','fork(','setsid(','Popen','setitimer('):self.assertNotIn(word,text)
        self.assertEqual(text.count('D.arm_deadline('),1);self.assertEqual(text.count("D.context(authority_path,'control')"),1)
        self.assertIn("min(duration,1.0) if operation=='alarm'",text)
        self.assertEqual(E.digest((REPAIR/'driver.py').read_bytes()),N.PINS['driver.py'])
        for name,pin in N.PINS.items():self.assertEqual(E.digest((REPAIR/name).read_bytes()),pin)
if __name__=='__main__':unittest.main()
