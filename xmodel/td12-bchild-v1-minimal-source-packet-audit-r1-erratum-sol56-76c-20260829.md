# TD12-BCHILD/v1 minimal source-packet audit: R1 erratum

Date: 2026-08-29  
Basis: `76c746f698103d20019bfeb72654a361ccc5371d`  
Charged report:
`xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md`

## Correction

The sentence

> For all three first-child vectors one packet may share `PairRef`, fibre,
> and source ladder ...

is **withdrawn**.

The `nu=25` B cell and the `nu=17` sibling cell are alternative reduced
route states.  Nothing in the frozen basis identifies them as vertices of
one exact pair, one fibre, or one completion.  Packet construction must
therefore be route-separated:

```text
TD12LocalPairJet_B
  = PairRef_B + F_B/completion_B + centre c_B + f/g/source jets at nu=25;

TD12LocalPairJet_S
  = PairRef_S + F_S/completion_S + centres c_+,c_-
    + one common f/g/source jet family at nu=17.
```

Only the universal recurrence schema is shared between these two packets.
Within `TD12LocalPairJet_S`, the `+` and `-` vectors are evaluations of the
same `P_k` family and therefore genuinely share one parent packet.

No other statement, hash, absent-versus-uncited classification, or minimal
field list in the charged report changes.

## Custody

Charged report full SHA-256 before and after this erratum:

```text
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
```

*End of sealed report body.*

## Seal

- Body length: `1432` bytes (all bytes before this heading).
- Body SHA-256:
  `dc988adc5627129274a31ec0fd6860f217d63d21035a1d3274921ebc7be4f8a0`.
- Frozen Git basis:
  `76c746f698103d20019bfeb72654a361ccc5371d`.
