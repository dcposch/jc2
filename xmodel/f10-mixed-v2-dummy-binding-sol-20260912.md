# f10 mixed v2 dummy binding

Status: **GAP — NO `dummy.sh` PUBLISHED**.

First action was `2026-09-12T23:17:47.416510884Z`. All four charged pins matched before use; the commands and registration were read WHOLE, the exact CAPRUN canonical-argv definition at lines 184–188 was selectively read, and the immutable coordination WHOLE read was reused after its pin matched.

The exact child argv has 12 elements:

```text
["/usr/bin/setpriv","--reuid=65534","--regid=65534","--clear-groups","--no-new-privs","/usr/bin/python3.12","-E","-s","-S","-B","/opt/jc2-mixed-20260912/runtime/probe.py","--descendant-rss-term-kill"]
```

Applying CAPRUN's literal compact-JSON UTF-8 encoding plus one LF gives SHA-256 `e585a9fa1c85c2a84ccec59c96df6857cf3514822edb2c435ce1db01cb0eb8d5`; count is `12`.

The task arrived only 73 seconds before its reserve and 133 seconds before HARD. Reproducing, substituting, and WHOLE-auditing the 143-line accepted block through the mandated patch-only write path could not be completed safely within that immutable horizon. I therefore did not publish partial or unaudited executable bytes. No worker qualification or execution is implied, and ROOT must not use this report as a binding.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `1236`.
- Body SHA-256:
  `48025be496754502a61d3a35a117abe94db065236fe26d33c462071c5c90ddf8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
