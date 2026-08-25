# V3 fail-closed source-control endpoint

AWS host: r6d `ip-172-30-0-197`  
Tag: `q8_w0_rankdrop_b1_c_infinity_v3_controls_std_dp_r6d_v1`

V3 stopped in `generate_v3.py` before emitting a Singular input.  It treated
the first object returned by `compile_quotient("approx")` as a tuple of names;
the pinned compiler returns a `Ring` object there.  The resulting Python
`TypeError` is a software failure only.  No CAS ran and no algebraic
empty/nonempty conclusion exists.

Remote endpoint SHA256:

```text
a768392d2a280c1db4624c0590658b22ae8178d1b0638f6a15e4930b83993b8c  generator.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  input.sing
87f2ea3de6c24e7dc401083edb69d346f461e0c52718ca2e865be36bb72ab1a8  launcher.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  launcher.stderr
```

V2 is unaffected.  V4 pins/imports the V3 helper bytes and removes only this
invalid names assertion before rerunning all intended controls.
