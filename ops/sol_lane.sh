#!/bin/sh
# Compatibility shim; use ops/lane.sh codex <tag> <promptfile> instead.
exec sh ops/lane.sh codex "$1" "$2"
