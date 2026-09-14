"""Mock host facts and filesystem only; execute actual gate comparisons.
No production constructor, full input, subprocess fixture or AWS access.
"""
import ast
import copy
import hashlib
import importlib.util
from pathlib import Path
import sys
import time
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import host_control as H

HERE=Path(__file__).resolve().parent
FROZEN=HERE.parent/'d125-parity-compression-code-prep-20260907'
sys.path.insert(0,str(FROZEN))
import construct as C


class Tiny(unittest.TestCase):
    def fixture(self):
        host=dict(system='Linux',vendor='Amazon EC2',instance=H.INSTANCE,boot='MOCK-BOOT',
                  cwd=str(H.WORK),hostname='DECLARED-MOCK',now=time.time())
        registration=hashlib.sha256((HERE/'REGISTRATION.md').read_bytes()).hexdigest()
        code={**H.PINS,'host_control.py':H.sha(HERE/'host_control.py')}
        authority=dict(schema='jc2.d125-parity-engineering-authority/v1',engineering_control_only=True,
                       control='authorize',root_green=True,construction_only=True,boot_id=host['boot'],
                       mode='slice',symmetry_gate_accepted=True,symmetry_gate_sha256=H.GATE,
                       registration_sha256=registration,job='DECLARED-LOCAL-MOCK',source_sha256=H.SOURCE,
                       code_sha256=code,caps=H.CAPS,expires_unix=host['now']+9)
        return authority,host,registration,code

    def test_exact_gate_positive(self):
        H.validate(*self.fixture(),'authorize')

    def test_actual_changed_authority_fields(self):
        for field,value,reason in [('boot_id','WRONG','boot mismatch'),
                ('symmetry_gate_sha256','0'*64,'wrong mathematical gate'),
                ('registration_sha256','0'*64,'wrong registration'),
                ('root_green',False,'GREEN absent'),('schema','production','engineering-only')]:
            a,h,r,c=self.fixture();a[field]=value
            with self.assertRaisesRegex(ValueError,reason):H.validate(a,h,r,c,'authorize')

    def test_missing_authority_and_wrong_host(self):
        a,h,r,c=self.fixture()
        with self.assertRaisesRegex(ValueError,'engineering-only'):H.validate({},h,r,c,'authorize')
        for field in ('boot','instance','cwd'):
            bad=dict(h);bad[field]='WRONG'
            with self.assertRaises(ValueError):H.validate(a,bad,r,c,'authorize')

    def test_changed_caps_and_code(self):
        a,h,r,c=self.fixture();a=copy.deepcopy(a);a['caps']['wall_seconds']=11
        with self.assertRaisesRegex(ValueError,'caps/deadline'):H.validate(a,h,r,c,'authorize')
        a,h,r,c=self.fixture();c=dict(c);c['run_once.py']='0'*64
        with self.assertRaisesRegex(ValueError,'frozen code'):H.validate(a,h,r,c,'authorize')

    def test_calls_real_authorize_only(self):
        # Exact real C.authorize with mocked host/authority reads and only its
        # OS-limit setters mocked. All arithmetic remains tiny, production=False.
        a,h,r,code=self.fixture();a['symmetry_sha256']=C.SYMMETRY
        import json
        def read_text(path,*args,**kwargs):
            return {'authority.fixture.json':json.dumps(a),'/sys/class/dmi/id/sys_vendor':'Amazon EC2',
                    '/sys/class/dmi/id/board_asset_tag':H.INSTANCE,
                    '/proc/sys/kernel/random/boot_id':h['boot']}[str(path)]
        original_read_bytes=Path.read_bytes
        def read_bytes(path):return original_read_bytes(FROZEN/path.name)
        with patch.object(C.Path,'read_text',read_text),patch.object(C.Path,'read_bytes',read_bytes),\
             patch.object(C.platform,'system',lambda:'Linux'),patch.object(C.os,'getcwd',lambda:str(H.WORK)),\
             patch.object(C.resource,'setrlimit') as limits,patch.object(C.signal,'setitimer') as timer,\
             patch.object(C,'main',side_effect=RuntimeError('FORBIDDEN CONSTRUCTOR')) as main,\
             patch.object(C,'reconstruct',side_effect=RuntimeError('FORBIDDEN RECONSTRUCTION')) as reconstruct:
            H.tiny(C,Path('authority.fixture.json'))
            self.assertEqual(limits.call_count,4);self.assertEqual(timer.call_count,1)
            main.assert_not_called();reconstruct.assert_not_called()
            a['boot_id']='WRONG'
            with self.assertRaisesRegex(ValueError,'boot mismatch'):H.tiny(C,Path('authority.fixture.json'))
            a['boot_id']=h['boot'];a['root_green']=False
            with self.assertRaisesRegex(ValueError,'authority absent'):H.tiny(C,Path('authority.fixture.json'))

    def test_no_assert_or_production_call(self):
        nodes=list(ast.walk(ast.parse((HERE/'host_control.py').read_bytes())))
        self.assertFalse(any(isinstance(n,ast.Assert) for n in nodes))
        self.assertFalse(any(isinstance(n,ast.Attribute) and n.attr in ('reconstruct','replay_frozen') for n in nodes))


if __name__=='__main__':unittest.main()
