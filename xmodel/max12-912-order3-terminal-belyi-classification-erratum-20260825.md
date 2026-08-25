# Erratum — selected-Q8 terminal Belyi nondegeneracy

Date: 2026-08-25  
Status: **review-mandated correction recorded; classification confirmed at
the corrected scope; frozen producer bytes unchanged**

The hostile review
`xmodel/max12-912-order3-terminal-belyi-classification-review-claude-20260824.md`
(SHA-256
`713e41def64d0fc313d254cae5d660e412f5ba9b69bd4d7c0e6c212a4688c52b`)
confirmed every algebraic step of the registered actual-trajectory theorem
but found one missing hypothesis in three unrestricted prose sentences of
the frozen producer report.

The classification of rational solutions of

```text
nu^10 h^3 (Z')^9 = j^9 Z^8
```

requires `Z` not identically zero.  Without it, `Z=0` satisfies the displayed
identity for arbitrary allowed noncube `h`, but cannot be written as
`Z=T^3` with nonconstant `T` and does not admit
`h=C*T^2/(T')^3`.  Accordingly, every unrestricted occurrence of “every
rational solution” in the frozen report is to be read with the added
hypothesis

```text
Z != 0 (equivalently, in the registered scope, Z is nonconstant).
```

No actual selected-Q8 trajectory is lost: the original frozen row
`9*r8'=j/u`, with `j!=0`, forces `r8` and hence
`Z=r8^9/nu^10` to be nonconstant.  Thus the corrected promotable theorem is
the producer theorem at strict selected-Q8 `k=mu=0,nu!=0,Z!=0` scope.  The
zero-`Z` family is excluded from the classification rather than silently
discarded.

This erratum changes no frozen producer, manifest, replay, or review byte and
licenses no coefficient-fibre realization, Taylor integrality, trajectory
existence or exclusion, maximum-twelve result, counterexample, or JC2
conclusion.
