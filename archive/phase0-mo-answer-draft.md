# Phase 0: MathOverflow answer draft (v3)

Target: https://mathoverflow.net/questions/513413 ("The simplest case of Jacobian conjecture").
Post under DC's own account. Complements, does not duplicate, https://mathoverflow.net/a/513493 (ratto3423).

v2 2026-08-18: full rewrite applying ALL 12 defects from round-1 hostile review
(xmodel/grok-mo-review.md, FAIL). v3 same day: applies round-2 residuals N1-N3,
N5 + optional items (xmodel/grok-mo-review2.md, FAIL-converging). Round-3: PASS
(xmodel/grok-round3.md). DOI filled + verified 2026-08-18. CLEARED TO POST.

---

## Answer text (MO Markdown + MathJax)

Nothing below is a proof-side reason to believe $\mathrm{JC}_2$; it is a report on the exclusion frontier this thread is tracking, with artifacts, and with evidence tiers stated.

The baseline is the Newton-polygon program of Guccione, Guccione and Valqui, raised with Horruitiner in [arXiv:2204.14178](https://arxiv.org/abs/2204.14178) to $\max(\deg P,\deg Q)\ge 108$: below degree $125$ a single family survives, $(72,108)$ up to order, reduced by their Prop. 4.3 to two explicit supports with $[P,Q]=x^2$. Everything at $(72,108)$ is conditional on that reduction, whose supporting chain is partly arXiv-only. The elimination of both supports, hence the bound $125$ stated in ratto3423's answer, now has a public, replicated record: Helali ([10.5281/zenodo.21479814](https://doi.org/10.5281/zenodo.21479814), first, July 21), Suzuki ([21483636](https://doi.org/10.5281/zenodo.21483636)), Ishihara ([21757679](https://doi.org/10.5281/zenodo.21757679)); these three are the public replicated record for that elimination, and I have replayed the Helali and Suzuki artifacts exactly. Strinz ([21633408](https://doi.org/10.5281/zenodo.21633408)) runs a parallel audited program whose own abstract marks its case closure open, and Leox reports a further independent elimination in the comments here, which I have not checked.

What I can add, with tiers stated explicitly:

1. A note on the minimal cell, archived with re-runnable exact-arithmetic verification at [10.5281/zenodo.21894922](https://doi.org/10.5281/zenodo.21894922). For the strip-shaped support, the Gröbner verdict on the generic chart is replaced by a proof: a vertex-gap obstruction, and a logarithmic-residue functional $R_{k,d_2}$ describing the depth-two block variety of every strip cell $k,d_2\ge 2$ in characteristic zero. The rigidity input is an elementary polynomial ODE lemma (if $AC'-\nu A'C$ is a nonzero constant, with $A,C$ polynomials and $\nu\ge 1$ an integer, then $\deg A\le 1$; it appears in Żołądek 2008, Appendix A.7, and for $\nu=1$ in Hermoso and Alcázar, arXiv:2410.18867); the new content is the vertex-gap and $R_{k,d_2}$ package.

2. A machine-checked ladder over the sheet number (topological degree) $d$ of a hypothetical counterexample, in Sigray's frame, archived in the theory bundle below. The enumerated $d\le 5$ book has zero survivors, consistent with the published low-sheet exclusions (Orevkov; Domrina and Orevkov; Żołądek, Thm 6.12); we do not rely on Sigray's Thm 9.1. At $d=7$, all $17$ cells of the enumerated off-axis book die under a uniform tower theorem, relative to the filed route perimeter. At $d=11$ there is a conditional emptiness certificate over an audited $411$-row quotient of the route space, conditional on named fail-closed classes; a $14$-cell type-$(3,5)$ book at $d=12$ is empty on its enumerated list at the same conditional tier. Each promoted statement ships with an executable gate suite.

To be precise about what is not proved: the ladder results are book-relative. They kill every configuration in the completed books named above, at the tiers stated, and the reduction that would land an arbitrary counterexample in those books is not yet a theorem; the gaps are named in the write-ups (no transport theorem from the GGV normal form into the sheet frame, no upper bound on $d$, among others). The smallest unfinished on-axis two-pole cell is at $d=6$, a residue condition on a depth ladder, with a computation aimed at deciding the current subcase either way in progress; the same residue survives in several larger composite panels, and the composite single-pole and general off-axis sectors are not closed. None of this proves $\mathrm{JC}_2$; these are exclusion and structure results.

On the question actually asked I have nothing structural to add to the other answers (the tame generation of $\mathrm{Aut}(\mathbb{A}^2)$, the McKay-Wang inversion formula).

The full theory bundle, verification scripts and adversarial review logs included, is archived at [10.5281/zenodo.22002825](https://doi.org/10.5281/zenodo.22002825). Scrutiny is welcome, adversarial review especially, and I am glad to coordinate with anyone named above. Since the role of AI has been asked about on this page: this work was produced in close collaboration with Claude, with GPT and Grok as adversarial reviewers, and I take responsibility for every claim.

---

## Pre-post checklist (DC)

1. DOI FILLED 2026-08-18 (10.5281/zenodo.22002825, verified resolving + description hedge-consistent via API). Confirm 10.5281/zenodo.21894922 also still resolves on posting day.
2. Reload the thread immediately before posting: new answers/comments (especially ratto3423's or Leox's write-ups) may require rewording the credit paragraph.
3. Re-verify tier language against AUDIT.md / REDUCTION.md on posting day; if a td=6 residue-A verdict has landed, rewrite the $d=6$ sentence.
4. Style pass: under ~650 words, zero em dashes, MathJax renders in MO preview.
5. Sequence: bundle DOI live, then the GGV-thread v4 note, then this post. (Helali coordination email struck per 2026-08-18 decision.)
6. Grok round-3 verdict on THIS v3 must be PASS before posting (round 1: grok-mo-review.md FAIL/12 applied; round 2: grok-mo-review2.md FAIL-converging, N1-N3+N5 applied).
