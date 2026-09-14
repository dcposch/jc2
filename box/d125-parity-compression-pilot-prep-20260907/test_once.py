"""Tiny control of sequencing, failure/expiry and no premature success."""
import ast
from pathlib import Path
from types import SimpleNamespace as NS
import time
import unittest
import run_once as X

class Tiny(unittest.TestCase):
    def fixture(self, failure=None, rows=803, expires=None):
        events=[]
        def build():
            events.append('build')
            if failure: raise ValueError('build failure')
        def replay(*args):
            events.append('replay')
            return {'status':'ALL_ORIGINAL_ROWS_TRANSPORTED','rows':rows}
        c=NS(main=build,Arithmetic=lambda *_:NS(stats={}))
        r=NS(replay_frozen=replay)
        a={'mode':'slice','expires_unix':expires or time.time()+10,'caps':{}}
        return c,r,a,events
    def test_success_and_order(self):
        c,r,a,events=self.fixture()
        result=X.pipeline(c,r,a,Path('unused'))
        self.assertEqual(events,['build','replay'])
        self.assertEqual(result['rows'],803)
    def test_failure_stops_before_replay(self):
        c,r,a,events=self.fixture(failure=True)
        with self.assertRaisesRegex(ValueError,'build failure'): X.pipeline(c,r,a,Path('unused'))
        self.assertEqual(events,['build'])
    def test_expired_shared_deadline(self):
        c,r,a,events=self.fixture(expires=time.time()-1)
        with self.assertRaisesRegex(ValueError,'before replay'): X.pipeline(c,r,a,Path('unused'))
        self.assertEqual(events,['build'])
    def test_incomplete_replay(self):
        c,r,a,events=self.fixture(rows=802)
        with self.assertRaisesRegex(ValueError,'incomplete'): X.pipeline(c,r,a,Path('unused'))
    def test_wrong_mode(self):
        c,r,a,events=self.fixture();a['mode']='full'
        with self.assertRaisesRegex(ValueError,'slice only'): X.pipeline(c,r,a,Path('unused'))
        self.assertEqual(events,[])
    def test_no_assert_or_spawn(self):
        nodes=list(ast.walk(ast.parse(Path(X.__file__).read_bytes())))
        self.assertFalse(any(isinstance(n,ast.Assert) for n in nodes))
        self.assertFalse(any(isinstance(n,ast.Name) and n.id in ('subprocess','fork','setsid') for n in nodes))

if __name__=='__main__': unittest.main()
