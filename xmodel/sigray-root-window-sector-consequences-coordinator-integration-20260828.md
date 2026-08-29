# Root-window sector consequences through `td=12` — coordinator integration — 2026-08-28

## Disposition

**GREEN at the entry/tree perimeter stated row by row; no panel-level
promotion.**  Two independent hostile/consequence audits and a coordinator
replay of the entry table agree on the following reusable rule:

> An actual parent of a genuine contact-zero root merge must have
> `0<w<1`.  Therefore a parent whose complete incoming alphabet is
> certified inside `[1,infinity)` excludes that root meet.

The word **complete** is load-bearing.  An entry value `w_0>=1` does not
kill a route after an off-axis or post-jump `M>=2` segment unless its whole
root-arrival alphabet has been proved.  The `root_w_window` JSON histogram
counts generated diagnostic `(r,l)` rows; it does not count realized roots.

## Consequence table

| sector | certified root consequence | remaining firewall |
|---|---|---|
| `td=6,m=2` | **Pole-chain root-meet branch closed.** MP1+MP4+MP5/D5 give both actual parents `W={2}`. | A root contact involving the post-interior suffix and a non-pole/northeast direction, interior residue A, and SF1/landing remain separate. |
| `td=7,m=2` | **Root-meet subcase closed.** The unique entry has `M=(1,2)` and its row-1 parent has exact `W={2}`. | The 62 filed interior budget-fitting cells remain; not a panel closure. |
| `td=8,m=2` | Six generated all-`b=1` root rows die (`W={2}`). | The off-axis `M=(2,2)` entry has no complete post-chain alphabet; root sector open. |
| `td=9,m=2` | **Filed root-meet perimeter closed:** seven generated rows die and there is no off-axis entry. | Interior survivors remain. |
| `td=9,m=3` | **Filed root-meet perimeter closed:** fourteen generated rows die. Any binary hidden hierarchy exposes a singleton row-1 parent with exact `W={2}`. | This is conditional on the filed MP0--MP5 entry/tree perimeter, not a whole-panel result. |
| `td=10,m=2` | **Filed root-meet perimeter closed:** eight all-axis rows die; the sole L6-valid off-axis entry has `M=(2,1)`, so its direct row-1 parent has exact `W(4)={2,4}` and kills the unique two-pole root meet. | Interior survivors remain. |
| `td=10,m=3` | Directly exposed row-1 parents die. | Entry `M=(1,1,2)` can hide the two row-1 leaves behind an inner `M>=2` emission; post-jump arrivals are unfiled. |
| `td=11,m=2` | **Filed root-meet perimeter closed:** the two entries `M=(1,2)` and `(1,3)` each expose their row-1 parent, with exact alphabets `{2}` and `{2,3}`. | Interior/off-axis chain sectors remain. |
| `td=11,m=3` | Root arrangements exposing the `b=1` leaf die. | Entry `M=(1,2,2)` can hide it inside an inner mixed/post-jump block. |
| `td=12,m=2` | Ten all-axis rows and the off-axis `M=(1,3)` root route die. | The three all-`b>=2` entries `(2,2)`, `(3,3)`, `(2,2)` remain root-open. |
| `td=12,m=3` | Twenty all-axis root rows die; a three-leaf hierarchy always exposes a singleton exact row-1 parent there. | The off-axis `(2,2,2)` entry remains root-open. |
| `td=12,m=4` | Thirty generated all-`M=1` rows die. | A `2+2` root partition can hide all four row-1 leaves behind two inner `M>=2` emissions; their post-jump alphabets are unfiled, so the full root sector remains open. |

The especially important anti-overclaim is `td=12,m=4`: zero off-axis
*entries* does not imply root completeness after earlier resonant jumps.

## Evidence checked

- root theorem: `xmodel/sigray-mixed-root-window-coordinator-integration-20260828.md`
  (`aaa4d179...`);
- two-pole closure: `xmodel/sigray-td6-two-pole-root-window-coordinator-integration-20260828.md`
  (`645b9424...`);
- entry and on-axis artifacts:
  `jc72108/systems/book/summary.json` and the named `book_m{m}_td{td}.json`
  files through `td=12`;
- off-axis entries and exact initial values: read-only replay of
  `cases/book_offaxis.py:census` and `cases/book_enum.py:w0_of` (0.1 s);
- topology and propagation: `SHEET6-MULTIPOLE.md` MP1, MP4, MP5/D5.

The two audits independently warned against treating AWS `ROOT` regex
counts, `TERMINAL_ROOT_M1`, or generated `root_w_window` rows as realized
root meets.  No such count is used as a theorem here.  No heavy local
computation or AWS job was used for this integration, and `jc2-lean` was
not entered, listed, searched, read, built, modified, status-checked, or
controlled.
