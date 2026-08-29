# Preregistration: D3 raw-to-global `8_28` / `M`-cokernel interface

Date: 2026-08-27

## Frozen question

Build the first fail-closed interface from the literal raw `2S/3S` source
through weight 22 to the seven-dimensional cokernel of

```text
H = X^8 - 1,
M(Y) = 4 H Y' + 6 H' Y.
```

The first run consumes only the frozen artificial R0 control.  It must:

1. enumerate every raw `2S` and `3S` coefficient slot through weight 22,
   with the exact raw monomial and its image under
   `F=t^8 f(t^3X,t^-1)` or `G=t^12 g(t^3X,t^-1)`;
2. retain the literal R0 artificial face assignment separately from R0's
   formal/rootwise cusp fixture;
3. accept local `V8`, `U11`, `U14`, and higher-`u` sidecars only when each
   has a serialized derivation DAG from named raw slots, with every formal
   cleanup operation and factor/deck/orientation tag;
4. glue those descendants to one literal `E22 in Q[X]` only when the
   derivation is typed globally; and
5. only then emit the unique remainder of `E22` in `Q[X]_{<=6}` modulo
   `im(M)`.

The schema checks `raw_to_morse.cleanup_DAG` before any carrier value.  If
that field is absent, the result is the first missing provenance field, not
an inferred global polynomial and not a face exclusion.  The compiler will
also record the smallest concrete R1 witness: the raw `F14` slice contains
only `X^2`, whereas the artificial local fixture uses `U14=X`.

## Ambient objects and maps

- Raw coefficient source: the polynomial ring over `Q` on the named slots
  `f_i_j` with `(i,j) in 2S` and `g_i_j` with `(i,j) in 3S`, restricted to
  normalized weights `0 <= n <= 22`.
- Raw chart: `Q[t,X]`, with

  ```text
  x^i y^j in f |-> t^(8+3i-j) X^i,
  x^i y^j in g |-> t^(12+3i-j) X^i.
  ```

- Root-local charts: `kappa_p[[t,u]]` for each irreducible factor `p` of
  `H`, oriented by `u = H mod t`; the determinant tag is
  `u_X(c,0)=H'(c)`.  No aliases define these maps.
- Global endpoint: `Q[X]`, containing a literal polynomial `E22`.
- Linear quotient target (not a quotient ring):
  `Q[X] / im(M)`, represented by the complement `Q[X]_{<=6}`.

Factor tags are exactly `X-1`, `X+1`, `X^2+1`, and `X^4+1`.  Deck,
orientation, chart, and determinant tags are mandatory and remain distinct.
The two R2 carrier branches may vary factorwise.  No choice among the 16
zero/nonzero branch patterns determines the global `H`-multiple.

## Frozen inputs

The compiler pins the exact R0, reviewed R1, reviewed R2, reviewed artificial
R3 scope firewall, and the independent `M`-cokernel audit.  R0 supplies two
separate artificial fixtures:

- a literal raw face assignment with `2S/3S` support; and
- a hand-specified local carrier `V8=1/48`, `U14=X`, together with the
  quarantined global polynomial identity
  `1+(13/12)H=M(X/48)`.

The second is not presumed to descend from the first.  R0 itself says its
nonconstant root-sign packets fail polynomial-source provenance, R1 says
`U14=X` is not a direct raw `F14` row, and R2 leaves the raw cleanup and
global sidecar image open.

## Exact reducer and controls

For a leading term `p_m X^m`, `m>=7`, subtract

```text
p_m / (4*(m+5)) * M(X^(m-7)).
```

The compiler replays the decomposition `P=M(Y)+r(P)` exactly over `Q`.
Registered controls are:

- `M(X/48)=1+(13/12)H` has seven-vector zero;
- `1` has seven-vector `(1,0,0,0,0,0,0)`;
- `H X^i` has vector `-12/(i+13)` in coordinate `i`, for `0<=i<=6`;
- deleting the `raw_to_morse.cleanup_DAG` field must stop compilation;
- pretending raw `F14` contains `X` must be rejected by the literal slice;
- dropping an orientation or factor tag must be rejected;
- changing `13/12` to `1` in the quarantined fixture must give a nonzero
  remainder.

Thus `r o (H*)` is explicitly checked as a diagonal isomorphism.  The
unknown `H`-multiple remains fully live.

## Verdict firewall

- `PASS-TYPED-GLOBAL-E22`: allowed only with a complete raw-to-Morse DAG,
  all factor/deck/orientation tags, a literal global polynomial identity,
  and exact reducer replay.
- `STOP-FIRST-MISSING-PROVENANCE`: the expected fail-closed interface
  outcome when a required field is absent.  It is a useful compiler result,
  but no `E22` is emitted as a raw descendant.
- Any quarantined polynomial reducer control is labelled as such and is not
  promoted to raw provenance.

No outcome licenses an `8_28` face/family exclusion, `G2-PSC`, `G2-BD`, a
Keller pair, a counterexample, or JC2.  In particular this first run does
not consume R3 as a source pair; R3 is pinned only to prevent overreading its
reviewed artificial squarefree replacement-edge theorem.
