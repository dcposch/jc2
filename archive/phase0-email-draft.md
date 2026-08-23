# GGV email — FINAL as sent (2026-08-11)

To: cvalqui@pucp.edu.pe, vander@dm.uba.ar, jjgucci@dm.uba.ar
Subject: Settling the (8,28) strip subcase of Proposition 4.3 (arXiv:2204.14178)
Attachment: paper1/main.pdf

## Body

Dear Professors Valqui and Guccione,

Over the past month I have been working on the degree pair left open by
arXiv:2204.14178v1. The attached note settles the strip subcase of
Proposition 4.3 (A0 = (8,28), [P,Q] = x^2): a vertex-gap obstruction
empties the generic chart by proof, and the remaining strata return the
unit ideal in exact computation over Q and at several large primes
(archived with the note). Conditional on Proposition 4.3, subcase (2) is
fully discarded. Subcase (1) is not claimed; Helali and Suzuki have
independent exclusions of it, so together the pair below 125 appears
closed.

The note was written in collaboration with an AI system, credited as
coauthor; all claims are machine-verified in exact arithmetic, and the
two central identities are checked in Lean.

Two requests, if you have time:

1. Does the polygon and vertex data used for subcase (2) match
   Proposition 4.3 as you intended?
2. Any corrections, and your preference for how the dependence on
   Proposition 4.3 is cited.

Artifact (code, certificates, logs): doi.org/10.5281/zenodo.21894922

Best,
Dan Clemens Posch

## Notes (not in the email)

- Salutation covers both Guccinones jointly; body approved by DC 2026-08-11.
- Endorsement ask deliberately deferred to a follow-up after a positive
  reaction (arXiv new-user flow).
- Bound corollary stated as "appears closed" — visible, not claimed.
- No mention of sheet-6/DC2/farm per the phase-0 rule; the artifact link
  and request 2 leave the door open.
- Horruitiner not on To: per DC's send list; can be added on any reply.

---

# Follow-up — FINAL as approved (2026-08-14, DC: "short, colloquial")

To: cvalqui@pucp.edu.pe, vander@dm.uba.ar, jjgucci@dm.uba.ar (reply in thread)
Subject: Re: Settling the (8,28) strip subcase of Proposition 4.3 (arXiv:2204.14178)
Attachment: paper1/main.pdf (v2)

## Body (pbcopy'd 2026-08-14)

Dear Professors Valqui and Guccione,

Quick update on Monday's note: the rigidity statement that was conjectural
there is now a theorem (Thm 6.5 in the attached v2), so nothing on our
side is conditional anymore -- the only remaining dependence is your
Proposition 4.3. Still glad to hear whether the polygon data matches your
intention, whenever convenient.

Best,
Dan Clemens Posch

## Notes
- Superseded the longer 08-13 draft per DC (<=3 sentences, colloquial).
- Endorsement ask still deferred. Attach the v2 PDF (paper1/main.pdf).

---

# Horruitiner CC line (pbcopy'd 2026-08-16; DC pastes when adding him to the GGV thread)
# Address: rmh322@cornell.edu (from the arXiv:2204.14178 PDF author list, Cornell affiliation)

CC Rodrigo Horruitiner, who I should have included from the start as a
coauthor of arXiv:2204.14178. Rodrigo: the note below settles the (8,28)
strip subcase of Proposition 4.3 (machine-verified, conditional on the
Proposition; v2 attached upthread), and I would value your read on
whether the polygon data matches what you intended.

# Helali / Suzuki draft (2026-08-16; DC review before send; emails from
# their artifact repos)

To: hello@lumelia.io (Helali — via his site lumelia.io; no direct
address published; fallback = GitHub issue on
bilLkarkariy/jc2-72-108-exact-certificates)
+ Suzuki: NO public email (ORCID 0009-0002-0556-4967 private, no
employment listed; artifact PDFs address-free) — reach via a polite
Zenodo-record comment/request or an issue if he has a repo; or ask
Helali if they are in contact (their artifacts appeared days apart)
Subject: Coordinated note on closing the degree pair below 125?

Dear Billel Helali,  [honorifics dropped: both profile as independent researchers, no doctorates in evidence; single-recipient form with forward-to-Suzuki line — final as pbcopy'd 2026-08-16]

I have been working on the (72,108) degree pair for the plane Jacobian
Conjecture. My note (attached) settles subcase (2) of Proposition 4.3
of arXiv:2204.14178, the (8,28) strip family, with all claims machine-
verified in exact arithmetic. In the process I replayed both of your
subcase (1) artifacts in full: both reproduce exactly, and the three
computations agree everywhere they overlap.

Since your exclusions and mine together appear to close the last pair
below degree 125, I wonder if you would be interested in a short
coordinated note recording the combined result, with the three
verifications credited to their authors. Happy to share my replay
logs and cross-check writeup in any case.

Best,
Dan Clemens Posch

# SEND LOG
- 2026-08-11: GGV original (Valqui, JA+JJ Guccione) + paper v2
- 2026-08-14: GGV follow-up (thread; theorem-upgrade note)
- 2026-08-16: Horruitiner CC'd into thread (rmh322@cornell.edu) + v3 attached
- 2026-08-16: Helali (hello@lumelia.io) + v3; Suzuki forward requested

---

## v4 proactive send into the GGV thread (drafted 2026-08-18, DC approved "do #1 and #2 today")

Reply-all into the existing thread (GGV + Horruitiner CC). Attach paper1/main.pdf (v4).
Recommended: send AFTER today's Zenodo bundle upload so the DOI line is concrete.

Dear all,

Attaching v4 of the short paper, superseding the version sent August 16. Three changes: a prior-art remark at Theorem 6.1 (the theorem also follows from Zoladek 2008, Appendix A.7; our characteristic-p proof is retained as an independent argument), citations to the four public replication artifacts of the (72,108) computation, and a revised author line with an explicit AI-collaboration disclosure.

We are also archiving the full theory bundle (all proofs, solver inputs, and verification scripts) on Zenodo today: [BUNDLE-DOI].

No response needed; sharing for the record. As before, if any of this is useful to your program, please use it freely.

Best regards,
Dan Clemens Posch

## Helali send: DROPPED per DC 2026-08-18 ("not a mathematician at all, only loosely interested").
## Citation of his artifact stands (merit policy); no further dedicated outreach.

## SEND LOG addition: v4 + bundle DOI sent into GGV thread 2026-08-18 (DC confirmed ~16:45 PDT)

## SEND LOG: MO ANSWER POSTED 2026-08-19 (~01:00 PDT)
https://mathoverflow.net/a/514446 (q513413). Final short form: 125 bound w/
Prop-4.3 conditionality, GGV-Horruitiner credited, Helali/Suzuki/Ishihara
DOIs + exact-replay claim, both our DOIs (21894922 + 22002825), book-relative
qualifier, AI disclosure + responsibility clause, msolve-tools share offer.
