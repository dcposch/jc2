# Rejected V12 producer: compiler sentinel false positive

V12 was stopped before Singular ran.  The compiler correctly removed its
unique `option(redSB);` directive, but the replacement explanatory comment
still contained the substring `option(redSB)`.  A deliberately overbroad
post-rewrite sentinel rejected that comment.

This is an implementation failure with **no algebra endpoint and no
membership conclusion**.  V13 freezes the same one-line algebra repair while
testing only for the exact executable directive `option(redSB);`.

Rejected evidence is under `aws_q_r6d_failed_compiler_sentinel/`.

