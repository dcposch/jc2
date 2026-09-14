# Exact D1 quadratic quotient audit

`print-audit-quotient-d1.py/.json` independently derives and checks the
optimization for both branches. The source rows are the actual saved D1
Jacobian residuals, not a newly prescribed face. Let
`d=Zface_H2_2`, `e=Zface_H2_5`, and `b_i=Zface_B2_i`.
Three rational-leader equations from the actual Gröbner basis give

    b7 = 40*d*e/49-e^3/35721,
    b4 = d^2/6+5*d*e^2/61236-e^4/357128352,
    b1 = 1489*d^2*e/32148900
         -37*d*e^3/46873096200-e^5/39051985291200.

The leaders are nonzero rational scalars. Substituting these graph maps
into the actual basis produces the monic equation

    q = d^2-(283/3500658)*d*e^2+(37/20415837456)*e^4.

No coefficient of an unproved face is being set to zero: q is an exact
consequence of the already required nonzero D1 differential equations.
The same three graphs and q result on both branches and match the
production `deep_quotient_seed_control_delta*.json` artifacts exactly.

For each branch the independent audit constructs a Q polynomial ring with
all five face variables, ZJ and the separation/inverse variables. It checks
both ideal inclusions between the original D1 generators and the saved
Gröbner basis. It then checks both ideal inclusions between the original
ideal and the model consisting of the three graph equations, q, the actual
J-inverse equation after graph substitution and monic reduction, and the
separation inverse equation. All four normal-form checks return zero.
The dimension is2 before and after; this includes the one-dimensional
separation factor. The reduced J-inverse remains a single equation
`ZJ*(A*d*e^11+B*e^13)-1`, with the exact rational A,B recorded in JSON.
Positive/negative Rabinowitsch controls return the expected nonunit/unit
answers. No parameter is inverted during graph or monic division.

The production transition is even more conservative: it verifies these
four consequences against the **current** residual ideal, adjoins them,
and retains all original generators. It checks both inclusions for the
ideal before and after adjoining the consequences. It then solves the
three rational graph equations and retains q explicitly. Thus any extra
Jacobian rows already accumulated are preserved as well.

Write a=283/3500658 and b=37/20415837456. The normal form recurrence is

    A0=0, B0=1; A1=1, B1=0,
    A_(n+1)=a*A_n+B_n, B_(n+1)=-b*A_n,
    d^n = A_n*d*e^(2n-2)+B_n*e^(2n) modulo q  (n>=1).

The audit compares powers0 through40 with direct monic polynomial
remainders. It also evaluates selected identities at both exact conjugate
roots over the quadratic coefficient extension; both pass. The discriminant
is nonzero, and neither root is selected. Every reduction changes the
original scalar row by a multiple of the retained q. Since q is independent
of the physical t,w coordinates, reduction also commutes with the
normalized derivatives used by the Jacobian computation.

A normal form `A+B*d` is retained as **one scalar equation**. It must never
be interpreted as the two equations A=0 and B=0. The requested negative
control is q=d^2-e with the scalar row d-1. The combined ideal is nonunit
and has d=e=1; the other conjugate d=-1,e=1 satisfies q but fails d-1.
Splitting the row into coefficients -1 and1 produces a false unit. The
independent audit verifies each of these claims exactly.

The continuation protects d and e from graph elimination, keeps q as an
explicit ideal generator, and caches polynomial coefficient rows. Later
proved graph substitutions affect only other coordinates and therefore
preserve the ideal(q). Substituting such a graph into a cached normal form
is still congruent to regenerating the original row and reducing modulo q.
A subsequent image may acquire a higher power of d; that does not authorize
splitting coefficients or choosing a root. The image remains a combined
polynomial row with q retained. Every phase's exact row replay must use
this same monic quotient and the same protected-coordinate map.
