# Toy test of certificate.py FUNCTIONS only (no main); synthetic inputs only.
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,sys.argv[1])
import certificate as C
from fractions import Fraction as F
Z=C.ZERO
def m(*pairs):
    d={}
    for e,c in pairs:
        v=[0]*12
        for i,x in e.items(): v[i]=x
        d[tuple(v)]=F(c)
    return d
x={0:1}; y={1:1}; z={2:1}
res=[]
def case(label,fn,expect=None,reason=None):
    try:
        out=fn()
    except C.Invalid as e:
        ok=(expect=='REJECT' and reason in str(e)); res.append((label,'REJECT:'+str(e),ok)); return
    except Exception as e:
        res.append((label,'EXC:'+type(e).__name__+':'+str(e)[:60],False)); return
    ok=(expect=='PASS' and (out is None or out.get('verdict')==(expect and (reason or out.get('verdict')))))
    if expect=='PASS' and reason: ok=(out.get('verdict')==reason)
    res.append((label,'PASS:'+str(out)[:80],ok))
E=lambda:[{} for _ in range(19)]
# 1 unit pass, rational U
rows=[m(({0:1},2),({},3)),m(({0:1},1))]+[{} for _ in range(18)]
P={'ROW/%d'%i:r for i,r in enumerate(rows)}
P['U']=m(({},F(3,7))); P['T/0']=m(({},F(1,7))); P['T/1']=m(({},F(-2,7)))
for i in range(2,20): P['T/%d'%i]={}
case('unit-rational-U',lambda:C.check_certificate(rows,'UNIT',P),'PASS','VERIFIED-UNIT')
# 2 U=0 vacuous
r=[m(({0:1},1))]+E(); Q={'ROW/%d'%i:v for i,v in enumerate(r)}; Q['U']={}; 
for i in range(20): Q['T/%d'%i]={}
case('U-zero-vacuous',lambda:C.check_certificate(r,'UNIT',Q),'REJECT','nonzero rational unit')
# 3 U variable
Q2=dict(Q); Q2['U']=m(({0:1},1)); Q2['T/0']=m(({},1))
case('U-variable-vacuous',lambda:C.check_certificate(r,'UNIT',Q2),'REJECT','nonzero rational unit')
# 4 U constant plus variable term
r4=[m(({0:1},1),({},1))]+E(); Q4={'ROW/%d'%i:v for i,v in enumerate(r4)}; Q4['U']=m(({0:1},1),({},1)); Q4['T/0']=m(({},1))
for i in range(1,20): Q4['T/%d'%i]={}
case('U-const-plus-var',lambda:C.check_certificate(r4,'UNIT',Q4),'REJECT','nonzero rational unit')
# 5 bad cofactor
r5=[m(({},1))]+E(); Q5={'ROW/%d'%i:v for i,v in enumerate(r5)}; Q5['U']=m(({},1)); Q5['T/0']=m(({},2))
for i in range(1,20): Q5['T/%d'%i]={}
case('bad-cofactor',lambda:C.check_certificate(r5,'UNIT',Q5),'REJECT','cofactor identity')
# 6 readback mismatch
Q6=dict(Q5); Q6['ROW/0']=m(({},2))
case('readback-mismatch',lambda:C.check_certificate(r5,'UNIT',Q6),'REJECT','source row read-back 0')
# 7 proper pass, multi-step reduction GB {x^2-y, xy-x, y^2-y}; rows x^3-xy, x^2-y, y^3-y, y^2-y, x^2y-x^2 (deg<=3)
G=[m(({0:2},1),({1:1},-1)),m(({0:1,1:1},1),({0:1},-1)),m(({1:2},1),({1:1},-1))]
r7=[m(({0:3},1),({0:1,1:1},-1)),G[0],m(({1:3},1),({1:1},-1)),G[2],m(({0:2,1:1},1),({0:2},-1))]+[{} for _ in range(15)]
P7={'ROW/%d'%i:v for i,v in enumerate(r7)}; P7.update({'G/%d'%i:g for i,g in enumerate(G)})
case('proper-GB-3-elements',lambda:C.check_certificate(r7,'PROPER',P7),'PASS','VERIFIED-PROPER')
# 8 failed S-pair {x^2, xy+1}
P8={'ROW/%d'%i:v for i,v in enumerate([m(({0:1},1))]+E())}; P8['G/0']=m(({0:2},1)); P8['G/1']=m(({0:1,1:1},1),({},1))
case('failed-S-pair',lambda:C.check_certificate([m(({0:1},1))]+E(),'PROPER',P8),'REJECT','failed S-pair')
# 9 failed containment {x^2} vs row x
P9={'ROW/%d'%i:v for i,v in enumerate([m(({0:1},1))]+E())}; P9['G/0']=m(({0:2},1))
case('failed-containment',lambda:C.check_certificate([m(({0:1},1))]+E(),'PROPER',P9),'REJECT','failed input containment')
# 10 leading monomial 1
P10=dict(P9); P10['G/0']=m(({},1))
case('LM-one',lambda:C.check_certificate([m(({0:1},1))]+E(),'PROPER',P10),'REJECT','proper monic leading term')
# 11 non-monic
P11=dict(P9); P11['G/0']=m(({0:1},2))
case('non-monic',lambda:C.check_certificate([m(({0:1},1))]+E(),'PROPER',P11),'REJECT','proper monic leading term')
# 12 zero basis member
P12=dict(P9); P12['G/0']={}
case('zero-basis-member',lambda:C.check_certificate([m(({0:1},1))]+E(),'PROPER',P12),'REJECT','zero basis member')
# 13 dp comparator: y^2 > x (degree); x*y^2 > x^2*z (last var smaller wins); x^2yz > xy^2z
def dp():
    a=C.leading(m(({0:1},1),({1:2},1))); b=C.leading(m(({0:2,2:1},1),({0:1,1:2},1))); c=C.leading(m(({0:2,1:1,2:1},1),({0:1,1:2,2:1},1)))
    d=C.leading(m(({11:1},1),({0:1},1)))  # omega vs u: same degree, last var: omega has exp 1, u has 0 -> u > omega
    C.require(a==tuple(m(({1:2},1)))[0] and b==tuple(m(({0:1,1:2},1)))[0] and c==tuple(m(({0:2,1:1,2:1},1)))[0] and d==tuple(m(({0:1},1)))[0],'dp comparator')
case('dp-order-4-checks',dp,'PASS')
# 14 cancellation
case('add-cancels-to-empty',lambda:C.require(C.add(m(({0:1},1)),m(({0:1},1)),F(-1))=={},'cancel'),'PASS')
case('multiply-by-empty',lambda:C.require(C.multiply(m(({0:1},1)),{})=={},'mulzero'),'PASS')
# 15 normal full reduction (non-leading term reducible): x^2*y + y reduced by {x^2 - y}: -> y^2 + y ; leading x^2y
case('normal-full',lambda:C.require(C.normal(m(({0:2,1:1},1),({1:1},1)),[m(({0:2},1),({1:1},-1))])==m(({1:2},1),({1:1},1)),'normal'),'PASS')
# 16 big integers: 2^53+1 exact, 2^80+1 vs rounded
case('int-2^53+1-exact',lambda:C.require(C.integer(str(2**53+1))==2**53+1,'prec'),'PASS')
case('int-2^80+1-exact',lambda:C.require(C.integer(str(2**80+1))==2**80+1 and C.integer(str(2**80+1))!=int(float(2**80+1)),'prec'),'PASS')
big=2**80+1; rb=[m(({},big))]+E(); Pb={'ROW/%d'%i:v for i,v in enumerate(rb)}; Pb['U']=m(({},2**80)); Pb['T/0']=m(({},1))
for i in range(1,20): Pb['T/%d'%i]={}
case('rounded-U-rejected',lambda:C.check_certificate(rb,'UNIT',Pb),'REJECT','cofactor identity')
Pb2=dict(Pb); Pb2['U']=m(({},big))
case('exact-big-U-passes',lambda:C.check_certificate(rb,'UNIT',Pb2),'PASS','VERIFIED-UNIT')
# 17 string/parse negatives
for s,lab in [('01','lead-zero'),('-0','neg-zero'),('+3','plus'),('3.0','float-str'),(' 3','space'),('','empty')]:
    case('integer-'+lab,lambda s=s:C.integer(s),'REJECT','STRING')
case('integer-float-type',lambda:C.integer(3.0),'REJECT','STRING syntax')
case('rational-zero-num',lambda:C.rational('0','1'),'REJECT','nonzero rational')
case('rational-neg-den',lambda:C.rational('1','-2'),'REJECT','positive denominator')
case('rational-unreduced',lambda:C.rational('2','4'),'REJECT','reduced rational')
# 18 transcript protocol
hdr='F10-DECISION/1\nARTIFACT|'+C.ARTIFACT+'\nRING|Q|dp|'+','.join(C.NAMES)+'\n'
rowsblk=''.join('POLY|ROW/%d\n'%i+('TERM|1,0,0,0,0,0,0,0,0,0,0,0|-3|7\n' if i==0 else '')+'ENDPOLY\n' for i in range(20))
unit_tail='BRANCH|UNIT\nPOLY|U\nTERM|0,0,0,0,0,0,0,0,0,0,0,0|1|1\nENDPOLY\n'+''.join('POLY|T/%d\nENDPOLY\n'%i for i in range(20))
good=hdr+rowsblk+unit_tail+'DONE\n'
def t_good():
    b,p=C.parse_transcript(good); C.require(b=='UNIT' and p['ROW/0']==m(({0:1},F(-3,7))) and len(p)==41,'parse')
case('transcript-unit-good',t_good,'PASS')
case('transcript-trailing',lambda:C.parse_transcript(good+'// ** warning\n'),'REJECT','trailing engine output')
case('transcript-missing-DONE',lambda:C.parse_transcript(good[:-5]),'REJECT','missing DONE')
case('transcript-ERROR-line',lambda:C.parse_transcript(hdr+rowsblk+'ERROR|lift dimensions\nDONE\n'),'REJECT','unsupported engine output')
case('transcript-branch-early',lambda:C.parse_transcript(hdr+'BRANCH|UNIT\n'+rowsblk+'DONE\n'),'REJECT','branch position')
case('transcript-no-branch',lambda:C.parse_transcript(hdr+rowsblk+'DONE\n'),'REJECT','missing branch')
case('transcript-unfinished-poly',lambda:C.parse_transcript(hdr+'POLY|ROW/0\nTERM|1,0,0,0,0,0,0,0,0,0,0,0|1|1\n'),'REJECT','unfinished polynomial')
case('transcript-dup-monomial',lambda:C.parse_transcript(hdr+'POLY|ROW/0\nTERM|1,0,0,0,0,0,0,0,0,0,0,0|1|1\nTERM|1,0,0,0,0,0,0,0,0,0,0,0|2|1\nENDPOLY\n'),'REJECT','duplicate engine monomial')
case('transcript-width-11',lambda:C.parse_transcript(hdr+'POLY|ROW/0\nTERM|1,0,0,0,0,0,0,0,0,0,0|1|1\nENDPOLY\n'),'REJECT','exponent vector width')
case('transcript-bad-ring',lambda:C.parse_transcript('F10-DECISION/1\nARTIFACT|'+C.ARTIFACT+'\nRING|32003|dp|u\nDONE\n'),'REJECT','framing/ring')
case('transcript-unit-short-tail',lambda:C.parse_transcript(hdr+rowsblk+'BRANCH|UNIT\nPOLY|U\nENDPOLY\nDONE\n'),'REJECT','unit dimensions/tags')
case('transcript-empty',lambda:C.parse_transcript(''),'REJECT','framing/ring')
n_ok=sum(1 for _,_,ok in res if ok)
for lab,out,ok in res: print(('OK  ' if ok else 'BAD ')+lab+' -> '+out)
print('CASES=%d EXPECTED=%d'%(len(res),n_ok))
