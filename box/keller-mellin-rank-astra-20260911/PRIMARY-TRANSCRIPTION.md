# Frozen selected mathematical transcription

These are mathematical statements in normalized notation, not verbatim prose or a substitute for the exact pinned primary PDFs. Source version/pins and read limits are in SOURCE-INDEX.md.

S1, Theorem 35 (printed p.20): for a holonomic Weyl module M on affine n-space, set θ_i=x_i∂_i, B_n=k[θ_1,...,θ_n], E_n=k(θ_1,...,θ_n), and let ι denote inclusion of the coordinate torus. Then

    dim_(E_n)(E_n ⊗_(B_n) M) = χ_DR(ι* M) < ∞.

S1, (3.5)–(3.6), p.21:

    χ_DR(M') = Σ_i (−1)^i dim_k H^i DR(M'),
    DR(M') = (Ω^• ⊗ M')[n].

An r-form occupies degree r−n. P.22, Corollary 37/footnote 16 identifies the resulting Euler characteristic of a smooth complement with (−1)^n times its ordinary topological Euler characteristic by algebraic de Rham comparison. Only this convention is imported, not the Feynman-specific identification of modules.

S2, corrected Theorem 2(1), p.1263: for a holonomic D-module on (G_m)^n,

    χ((G_m)^n,M) = dim_(C(s))(M(s)).

Here the original Mellin variables are s_i=−x_i∂_i; simultaneous change of sign of those variables does not change the rational-field rank. The correction retains this Euler/rank equality and replaces its prior proof. Its separate rank-one classification does not state that a higher-rank difference module contains a rank-one submodule.

Manual source-proof caution, not an external theorem: the final optional S1 Appendix B construction treats the ∂-locally-nilpotent part as a torus D-submodule. In C[x,x⁻¹], 1 is locally ∂-nilpotent, but ∂^k(x⁻¹)=(−1)^k k! x^(−k−1) never vanishes. Hence that stability argument cannot be used as written. The report relies on corrected S2 Theorem 2(1), not this optional construction. This does not invalidate the theorem or its standard spectral-sequence Euler step.
