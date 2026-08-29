# TD6 V89H5V2 initial parser-sentinel erratum

Date: 2026-08-26

The first dual deployment used source archive
`6383ab91b1dacac1a62a4e71f170831968dc7901459eb2f442e74cd7082221ea`
and terminated identically with rc 1 before parsing the first frozen
coefficient.  The tiny AST parser attempted to call `m.tri`, which is a
module, rather than its polynomial context `m.tri.CTX`.

This was a deployment/parser sentinel only.  No mathematical membership
test, division by `F`, denominator audit, or verdict ran.  The failed client,
manifest, archive, and both AWS run directories are retained under names
containing `sentinel`.

V2R1 changes exactly that constructor call to `m.tri.CTX(node.value)` and
must receive a new source manifest/archive and fresh dual AWS run roots.
