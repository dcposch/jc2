"""Immutable reviewed normalized backend function snapshot."""
import sympy as sp

def exprS(e):
    """Unambiguous recursive Singular polynomial serializer (no power/division)."""
    e = sp.sympify(e)
    if e.is_Integer:
        return str(e)
    if e.is_Rational:
        return f'({e.p}/{e.q})'
    if e.is_Symbol:
        return str(e)
    if e.is_Add:
        return '(' + '+'.join((exprS(t) for t in e.args)) + ')'
    if e.is_Mul:
        return '(' + '*'.join((exprS(t) for t in e.args)) + ')'
    if e.is_Pow:
        base, power = e.args
        assert power.is_Integer and power >= 0, (e, power)
        return f'({exprS(base)})^{power}'
    raise TypeError((e, type(e)))

def normalized_script(h_expr, D_expr, C_expr, residual_strings, names, k, target, face_expr, leader_name=None, leader_inverse=None, localizer_rows=('Zc*c-1',)):
    assert k < target < 2 * k
    leader_name = leader_name or f'leader{target}'
    leader_inverse = leader_inverse or f'Z{target}'
    vd, cd, rd, ed, ld = (2 * k - 1, 3 * k - 1, 4 * k - 2, 5 * k - 3, 6 * k - 3)
    face_depth = ed - (target - k)
    low_depth = ld - (target - 1)
    lines = [f'ring R=0,(zz,tt,{','.join(names)}),(lp(1),dp({len(names) + 1}));', 'option(redSB);print("BEGIN_BUILD_NORMALIZED");', f'poly h={h_expr};poly D={D_expr};poly C={C_expr};', f'poly H=h-(1/6)*target_b*tt^{k};', 'poly aa=target_a+(1/4)*target_b^2;poly dd=target_d+(1/2)*target_b*target_c;', 'poly pp=dd-(1/3)*aa^2;poly qq=target_e+(1/4)*target_c^2-(1/3)*aa*dd+(2/27)*aa^3;', f'poly vv=D+((1/3)*target_a+(1/18)*target_b^2)*tt^{vd};', f'poly VV=C-(1/4)*target_b*tt^{k}*D+((1/12)*target_a*target_b+(1/54)*target_b^3-(1/2)*target_c)*tt^{cd};', 'print("BEGIN_DIVIDE_vv2");list L0=division(vv^2,ideal(H));matrix M0=L0[1];ideal N0=L0[2];poly UU=M0[1,1];poly RR=N0[1];', 'if(vv^2-UU*H-RR!=0){ERROR("division0 identity failed");}print("END_DIVIDE_vv2");print(size(UU));print(size(RR));', 'print("BEGIN_DIVIDE_vvU");list L1=division(vv*UU,ideal(H));matrix M1=L1[1];ideal N1=L1[2];poly PP=M1[1,1];poly RR1=N1[1];', 'if(vv*UU-PP*H-RR1!=0){ERROR("division1 identity failed");}print("END_DIVIDE_vvU");print(size(PP));print(size(RR1));', 'print("BEGIN_DIVIDE_vvR");list L2=division(vv*RR,ideal(H));matrix M2=L2[1];ideal N2=L2[2];poly Qpart=M2[1,1];poly RR2=N2[1];', 'if(vv*RR-Qpart*H-RR2!=0){ERROR("division2 identity failed");}print("END_DIVIDE_vvR");print(size(Qpart));print(size(RR2));', 'print("BEGIN_DIVIDE_U2");list L3=division(UU^2,ideal(H));matrix M3=L3[1];ideal N3=L3[2];poly WW=M3[1,1];poly RR3=N3[1];', 'if(UU^2-WW*H-RR3!=0){ERROR("division3 identity failed");}print("END_DIVIDE_U2");print(size(WW));print(size(RR3));', 'poly derivedV=VV-(3/8)*tt*UU;', f'poly upper=(3/4)*RR+pp*tt^{rd}-(1/8)*tt*PP;', 'poly digit=Qpart-(1/8)*RR1-(9/64)*tt*WW;', f'poly low=RR2-(9/64)*tt*RR3+pp*tt^{rd}*vv+qq*tt^{ld};', f'poly digitDifference=digit-{leader_name}*tt^{face_depth}*({face_expr});', 'print("BEGIN_EXTRACT_CHARACTERISTIC");matrix cv=coef(derivedV,tt*zz);matrix cu=coef(upper,tt*zz);matrix ce=coef(digitDifference,tt*zz);matrix cl=coef(low,tt*zz);', 'print("END_EXTRACT_CHARACTERISTIC");', f'intvec wt=0,1,{','.join(('0' for _ in names))};', 'ideal I=' + (','.join(residual_strings) if residual_strings else '0') + ';', 'int j;int charRows=0;', 'for(j=1;j<=ncols(cv);j++){I[size(I)+1]=cv[2,j];charRows++;}for(j=1;j<=ncols(cu);j++){I[size(I)+1]=cu[2,j];charRows++;}', f'for(j=1;j<=ncols(ce);j++){{if(deg(ce[1,j],wt)<={face_depth}){{I[size(I)+1]=ce[2,j];charRows++;}}}}', f'for(j=1;j<=ncols(cl);j++){{if(deg(cl[1,j],wt)<{low_depth}){{I[size(I)+1]=cl[2,j];charRows++;}}}}', f'I[size(I)+1]={leader_inverse}*{leader_name}-1;' + ''.join((f'I[size(I)+1]={row};' for row in localizer_rows)), 'print("BEGIN_ROW_COUNTS");print(charRows+1);print(size(I));print("END_ROW_COUNTS");', 'print("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");', f'ideal neg={leader_name},{leader_inverse}*{leader_name}-1;ideal pos={leader_name}-1,{leader_inverse}*{leader_name}-1;', 'print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;']
    return '\n'.join(lines) + '\n'
