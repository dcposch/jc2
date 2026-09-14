"""Declared tiny hybrid streams only; no production stream/CAS or worker."""
import ast,copy,json
from pathlib import Path
import unittest
import exact as E
import hybrid as H
import driver as D
from test_exact import result
V=['x','y','k','z']
def wire(p):return [[[[str(c.numerator),str(c.denominator)],['0','1']],list(m)] for m,c in sorted(p.items())]
def pack(records):
    r=copy.deepcopy(records);prefix=b''.join(E.canonical(x) for x in r[:-1]);r[-1]['prefix_sha256']=E.digest(prefix)
    return prefix+E.canonical(r[-1])
def fixture(texts):
    rec=[dict(type='header',schema='jc2.hybrid-affine/v1',field='Q',order='dp',target=H.TARGET,source_sha256=H.ORIGINAL_SHA,variables=V,original_variables=V)]
    rec.append(dict(type='coefficient_map',member='A',source_entry={'name':'TOY'},terms=wire(E.polynomial('x',V))))
    rec.append(dict(type='graph',member='A',degree=1,pivots=[[0,1]],inverse=[[['1','1']]]))
    rows=[E.polynomial(t,V) for t in texts]
    for i,p in enumerate(rows):rec.append(dict(type='row',original_index=i if i<len(rows)-1 else None,label='R/'+str(i) if i<len(rows)-1 else 'UNIT/kz',terms=wire(p),old_from_new_ell_power=0,guard_power=1 if i==len(rows)-1 else 0,guard_cofactor=wire(E.ONE if i==len(rows)-1 else {})))
    rec.append(dict(type='footer',complete=True,rows=len(rows),original_rows=len(rows)-1,terms=sum(map(len,rows)),zero_original_rows=sum(not p for p in rows[:-1]),coefficient_map_terms=1))
    return pack(rec)
def certificate(data,engine,basis,cofactors=None):return result(engine,basis,cofactors,variables=V,source=E.digest(data))
class HybridTests(unittest.TestCase):
    def test_literal_all_slots_and_roundtrip(self):
        texts=['0','x','0','x','1-x','0','k*z-1'];data=fixture(texts)
        v,rows,labels,prefix=H.read_hybrid(data)
        self.assertEqual(v,V);self.assertEqual(len(rows),7);self.assertEqual(prefix.count('// '),7)
        pieces=prefix.split('ideal I=\n')[1][:-2].split(',\n')
        for piece,row,label in zip(pieces,rows,labels):
            self.assertTrue(piece.startswith('// '+label+'\n'));self.assertEqual(E.polynomial(piece.split('\n',1)[1],v),row)
        self.assertEqual(E.polynomial(H.ordinary(E.polynomial('-x^2/2+3*y/7-k*z',v),v),v),E.polynomial('-x^2/2+3*y/7-k*z',v))
    def test_unit_zero_duplicate_and_guards(self):
        ts=['0','x','0','x','1-x','0','k*z-1'];data=fixture(ts)
        output=certificate(data,ts,['1'],['0','1/2','0','1/2','1','0','0'])
        verdict,mapping,labels=H.checked_certificate(data,output,b'')
        self.assertIn('UNIT_COFACTOR',verdict);self.assertEqual(mapping,[0,1,0,1,4,0,6]);self.assertEqual(len(labels),7)
        with self.assertRaisesRegex(ValueError,'not one'):H.checked_certificate(data,output.replace(b'T 5 1',b'T 5 2'),b'')
        with self.assertRaises(ValueError):H.checked_certificate(data,certificate(data,ts[:-1],['1'],['0','1/2','0','1/2','1','0']),b'')
    def test_proper_superideal_and_falseproper(self):
        ts=['0','x^2','x*y','0','k*z-1'];data=fixture(ts)
        self.assertIn('PROPER',H.checked_certificate(data,certificate(data,ts,['x','k*z-1']),b'')[0])
        with self.assertRaisesRegex(ValueError,'original equation missing'):H.checked_certificate(data,certificate(data,ts,['x']),b'')
        bad=['0','x^2','x*y-1','k*z-1'];data=fixture(bad)
        with self.assertRaisesRegex(ValueError,'Buchberger'):H.checked_certificate(data,certificate(data,bad,bad),b'')
    def test_strict_new_stream_mutations(self):
        data=fixture(['0','x','1-x','k*z-1']);base=[json.loads(x) for x in data.splitlines()]
        changes=[]
        for field,value in [('field','Q(rho)'),('order','lp'),('target','J-5*k^3*g^2/9'),('source_sha256','a'*64)]:
            r=copy.deepcopy(base);r[0][field]=value;changes.append(pack(r))
        r=copy.deepcopy(base);r[3]['original_index']=1;changes.append(pack(r))
        r=copy.deepcopy(base);r[3]['terms']=[[[['1','1'],['1','1']],[]]];changes.append(pack(r))
        r=copy.deepcopy(base);r.pop(3);changes.append(pack(r))
        r=copy.deepcopy(base);r[-2]['label']='GUARD/missing-unit';changes.append(pack(r))
        r=copy.deepcopy(base);r[-1]['terms']+=1;changes.append(pack(r))
        changes.extend([data+b'{}\n',data.replace(b'"field":"Q"',b'"field":"Q","field":"Q"',1)])
        for changed in changes:
            with self.subTest(changed=changed[-90:]),self.assertRaises((ValueError,KeyError)):H.read_hybrid(changed)
    def test_resynced_source_drift_cannot_reuse_certificate(self):
        ts=['0','x','1-x','k*z-1'];data=fixture(ts);out=certificate(data,ts,['1'],['0','1','1','0'])
        rec=[json.loads(x) for x in data.splitlines()]
        rec[3]['terms']=wire(E.ONE);rec[-1]['terms']+=1;rec[-1]['zero_original_rows']-=1
        changed=pack(rec);H.read_hybrid(changed)
        with self.assertRaisesRegex(ValueError,'header mismatch'):H.checked_certificate(changed,out,b'')
        rec=[json.loads(x) for x in data.splitlines()];rec[1]['terms']=wire(E.polynomial('y',V));changed=pack(rec)
        with self.assertRaisesRegex(ValueError,'header mismatch'):H.checked_certificate(changed,out,b'')
    def test_strict_old_certificate_guards_preserved(self):
        ts=['0','x','1-x','k*z-1'];data=fixture(ts);out=certificate(data,ts,['1'],['0','1','1','0'])
        for bad,stderr in [(out,b' \n\t'),(out.replace(b'I_SIZE 3',b'I_SIZE 0'),b''),(out+b'EXTRA\n',b''),(out.replace(b'END UNIT\n',b''),b'')]:
            with self.assertRaises(ValueError):H.checked_certificate(data,bad,stderr)
    def test_schema_binding_unchanged_footer(self):
        text=D.footer(V,'a'*64);self.assertTrue('JC2CERT 1 '+'a'*64 in text)
        self.assertEqual(text.count('slimgb(I)'),1);self.assertNotIn('slimgb',D.control_input())
        self.assertEqual(E.digest(Path(E.__file__).read_bytes()),'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9')
        self.assertEqual(D.CAPS['decision_seconds'],300);self.assertEqual(D.CAPS['verify_seconds'],120)
        with self.assertRaisesRegex(ValueError,'pin drift'):H.read_hybrid(fixture(['0','k*z-1']),production=True)
    def test_no_assert_gates(self):
        for module in (E,H,D):self.assertFalse(any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(module.__file__).read_text()))))
if __name__=='__main__':unittest.main()
