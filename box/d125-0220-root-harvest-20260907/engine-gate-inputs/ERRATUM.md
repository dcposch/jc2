# Prose-only byte-count correction

The sealed report SHA481ba6521e86e7a5786e71b9f8e1ac266c483d56bfe9eba164bd59f468812fbf
calls the fixed alarm program107 bytes. Its actual ASCII length is **102 bytes**,
as checked directly by AST literal evaluation of engine.py's alarm_script return.
The code, <256-byte test, all resource caps and all other artifact pins are
unchanged. Neither version was executed in Singular. Do not edit the sealed body.
