"""DESIGNED, NOT RUN. Finite actual changed-payload controls; registered only."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import json, hashlib, copy
from fractions import Fraction
from execution_gate import authorize
from certificate import (ARTIFACT,ZERO,NAMES,Invalid,require,readwire,source_rows,readback,
                         check_certificate,parse_transcript,multiply,sha)

def main():
    require(len(sys.argv)==4,'semantic_tests AUTH ARTIFACT RECEIPT')
    execution=authorize(sys.argv[1],__file__,'check')
    require(sha(sys.argv[2])==ARTIFACT,'artifact hash')
    data=json.loads(Path(sys.argv[2]).read_text()); rows=source_rows(data); passed=[]
    def reject(label,action,reason):
        try: action()
        except Invalid as e:
            require(reason in str(e),'wrong rejection '+label+': '+str(e)); passed.append(label)
        else: raise Invalid('mutation passed '+label)
    actual={'ROW/'+str(i):p for i,p in enumerate(rows)}
    readback(rows,actual); passed.append('actual-twenty-row-readback')
    for index,label in [(0,'wrong-row'),(19,'wrong-guard')]:
        bad=copy.deepcopy(actual); bad['ROW/'+str(index)]={}
        require(bad!=actual,'actual row mutation unchanged')
        reject(label,lambda:readback(rows,bad),'source row read-back')
    bad=copy.deepcopy(data); bad['variables'][0],bad['variables'][1]=bad['variables'][1],bad['variables'][0]
    reject('swapped-variables',lambda:source_rows(bad),'variable/schema')
    x=(1,)+(0,)*11; y=(0,1)+(0,)*10; x2=(2,)+(0,)*11; xy=(1,1)+(0,)*10
    unitrows=[{ZERO:Fraction(1)}]+[{} for _ in range(19)]
    unit={'ROW/'+str(i):p for i,p in enumerate(unitrows)}
    unit.update({'U':{ZERO:Fraction(1)},**{'T/'+str(i):({ZERO:Fraction(1)} if i==0 else {}) for i in range(20)}})
    require(check_certificate(unitrows,'UNIT',unit)['verdict']=='VERIFIED-UNIT','positive unit')
    passed.append('positive-unit')
    def protocol(branch,polynomials):
        lines=['F10-DECISION/1','ARTIFACT|'+ARTIFACT,'RING|Q|dp|'+','.join(NAMES)]
        tags=['ROW/'+str(i) for i in range(20)]
        tail=['U']+['T/'+str(i) for i in range(20)] if branch=='UNIT' else ['G/'+str(i) for i in range(len(polynomials)-20)]
        for tag in tags+tail:
            if tag==tail[0]: lines.append('BRANCH|'+branch)
            lines.append('POLY|'+tag)
            for exponent,value in polynomials[tag].items():
                lines.append('TERM|'+','.join(map(str,exponent))+'|'+str(value.numerator)+'|'+str(value.denominator))
            lines.append('ENDPOLY')
        return '\n'.join(lines+['DONE'])+'\n'
    text=protocol('UNIT',unit); kind,parsed=parse_transcript(text)
    check_certificate(unitrows,kind,parsed); passed.append('positive-unit-machine-protocol')
    reject('truncated-protocol',lambda:parse_transcript(text[:-5]),'missing DONE')
    reject('trailing-warning',lambda:parse_transcript(text+'WARNING\n'),'trailing engine output')
    urows=[{x:Fraction(1)}]+[{} for _ in range(19)]
    for value,label in [({},'zero-residual-U-zero'),({x:Fraction(1)},'zero-residual-U-variable')]:
        bad=copy.deepcopy(unit); bad['ROW/0']=urows[0]; bad['U']=value
        bad['T/0']={ZERO:Fraction(1)} if value else {}
        require(multiply(urows[0],bad['T/0'])==value,'weak residual control must pass')
        reject(label,lambda:check_certificate(urows,'UNIT',bad),'nonzero rational unit')
    bad=copy.deepcopy(unit); bad['T/0']={}
    reject('bad-cofactor',lambda:check_certificate(unitrows,'UNIT',bad),'cofactor identity')
    large=2**80+1; rounded=int(float(large)); require(large!=rounded and abs(large)>2**53,'precision precondition')
    bigrows=[{ZERO:Fraction(large)}]+[{} for _ in range(19)]
    big=copy.deepcopy(unit); big['ROW/0']=bigrows[0]; big['U']={ZERO:Fraction(large)}
    check_certificate(bigrows,'UNIT',big); passed.append('positive-large-integer-unit')
    reject('float-rational',lambda:readwire([[list(ZERO),float(large),'1']]),'STRING syntax')
    bad=copy.deepcopy(big); bad['U']=readwire([[list(ZERO),str(rounded),'1']])
    reject('rounded-canonical-string',lambda:check_certificate(bigrows,'UNIT',bad),'cofactor identity')
    prows=[{x:Fraction(1)}]+[{} for _ in range(19)]
    proper={'ROW/'+str(i):p for i,p in enumerate(prows)}; proper['G/0']={x:Fraction(1)}
    require(check_certificate(prows,'PROPER',proper)['verdict']=='VERIFIED-PROPER','positive proper')
    passed.append('positive-proper')
    kind,parsed=parse_transcript(protocol('PROPER',proper))
    check_certificate(prows,kind,parsed); passed.append('positive-proper-machine-protocol')
    bad=copy.deepcopy(proper); bad['G/0']={x2:Fraction(1)}
    reject('failed-input-containment',lambda:check_certificate(prows,'PROPER',bad),'input containment')
    bad=copy.deepcopy(proper); bad['G/0']={x2:Fraction(1)}; bad['G/1']={xy:Fraction(1),ZERO:Fraction(1)}
    reject('failed-S-pair',lambda:check_certificate(prows,'PROPER',bad),'S-pair')
    reject('wrong-ring-framing',lambda:parse_transcript('F10-DECISION/1\nARTIFACT|'+ARTIFACT+'\nRING|32003|dp|wrong\nDONE\n'),'framing/ring')
    result={'status':'PASS-DESIGNED-SEMANTICS','execution':execution,'artifact_sha256':ARTIFACT,
            'certificate_sha256':sha(Path(__file__).with_name('certificate.py')),'tests_sha256':sha(__file__),
            'passed':passed,'scope':'Certificate semantic controls, not an actual ideal decision'}
    with Path(sys.argv[3]).open('x') as f: json.dump(result,f,sort_keys=True); f.write('\n')

if __name__=='__main__': main()
