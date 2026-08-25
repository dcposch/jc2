# Self-contained selected-Q8 contact count

This exact lightweight replay consumes only fibres for which a positive-order
moving source lift was explicitly frozen:

```text
80 distinct order-8 fibres, plus w=25 at order 64.
```

It proves normalized contact sum `80*8+64=704>658`.  It intentionally does not
count any of the remaining fixed fibres at order one.

The component conclusion still depends on the separately frozen sparse
contact-to-component lemma and retains its mod-127/degree-one/no-merger scope.
