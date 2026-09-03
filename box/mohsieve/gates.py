"""Load-bearing checks that survive python3 -O. No ast.Assert here."""
FAILURES = []


def require(name, cond, detail=""):
    if cond:
        print("  [ok]   %s" % name)
        return True
    print("  [FAIL] %s   %s" % (name, detail))
    FAILURES.append(name)
    return False


def fail_closed():
    if FAILURES:
        print("GATES FAILED (%d): %s" % (len(FAILURES), FAILURES))
        raise SystemExit(1)


def reset():
    FAILURES.clear()
