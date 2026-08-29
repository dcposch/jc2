# V1 deployment negative

Both AWS lanes froze the registered package but stopped in the Python
compiler before algebra because `run_aws.sh` pre-created `compiled/` and the
compiler deliberately uses `mkdir(...,exist_ok=False)`.  The common exception
was `FileExistsError`.  V1 has no mathematical output or verdict.  V2 removes
only that premature directory creation.
