#!/bin/sh
# grok CLI adapter.
pf="$1"
exec grok -p "$(cat "$pf")"
