#!/usr/bin/env python3
"""Find possible collisions between newly raised OPENs and banked reports.

The tool is deliberately lexical: a hit is a review candidate, never a claim
that an OPEN is closed.  It reads one report, extracts OPEN entries under an
explicit ``OPEN(S) RAISED`` or ``OPEN(S) OPENED`` heading, and scans the banked
corpus for relation-bearing lines whose local context shares the OPEN's key
nouns and bounded-quantity vocabulary.

The rendered Markdown always contains a ``COLLISIONS`` section.  Read or
contract errors produce an ERROR block and a non-zero exit instead of a
partial or silently empty result.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


OPEN_RE = re.compile(r"OPEN\[([^]\r\n]+)\]")
RAISED_RE = re.compile(
    r"^\s*(?:#{1,6}\s+|\*\*)?OPENS?\s+"
    r"(?:RAISED(?:\s+OR\s+SHARPENED)?|OPENED)\b",
    re.IGNORECASE,
)
OTHER_OPEN_STATUS_RE = re.compile(
    r"^\s*(?:#{1,6}\s+|\*\*)?OPENS?\s+"
    r"(?:CLOSED|RESOLVED|ANSWERED|UNTOUCHED|RE-RANKED|RETIRED)\b",
    re.IGNORECASE,
)
ENTRY_RE = re.compile(
    r"^\s*(?:(?:#{1,6}|[-*+]|\d+[.)])\s+)?"
    r"(?:\*\*)?`?(OPEN\[[^]\r\n]+\])"
)
INLINE_RAISE_RE = re.compile(
    r"^\s*(?:(?:[-*+]|\d+[.)])\s+)?(?:THIS\s+REPORT\s+)?"
    r"RAISES?\s*:?\s*(OPEN\[[^]\r\n]+\])",
    re.IGNORECASE,
)
BOUND_CUE_RE = re.compile(
    r"\b(?:bound(?:s|ed|ing)?|cap(?:s|ped|ping)?|ceiling|floor|"
    r"at\s+most|at\s+least)\b",
    re.IGNORECASE,
)
RELATION_RE = re.compile(
    r"(?:<=|>=|==|(?<![<>=])=(?!=)|[<>≤≥]|\\(?:leq?|geq?)\b)"
    r"|\b(?:bound(?:s|ed|ing)?|cap(?:s|ped|ping)?|ceiling|floor|"
    r"at\s+most|at\s+least)\b",
    re.IGNORECASE,
)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_]*")

# These are connective/status words, not useful collision keys.  One-letter
# symbols are also omitted: in this corpus they make searches far too broad.
STOP_TERMS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "bound",
    "bounded",
    "bounding",
    "bounds",
    "by",
    "candidate",
    "cap",
    "capped",
    "caps",
    "does",
    "every",
    "for",
    "from",
    "has",
    "have",
    "hold",
    "holds",
    "in",
    "into",
    "is",
    "it",
    "its",
    "none",
    "of",
    "on",
    "one",
    "open",
    "opened",
    "only",
    "or",
    "quantity",
    "raised",
    "raises",
    "than",
    "that",
    "the",
    "this",
    "terms",
    "to",
    "versus",
    "vs",
    "what",
    "which",
    "with",
}
REQUIRED_TOP_LEVEL = ("AUDIT.md", "notes.md", "APPROACHES.md")
DEFAULT_CONTEXT_LINES = 8
DEFAULT_MAX_CANDIDATES = 100


class CollisionError(RuntimeError):
    """The scan could not satisfy its fail-closed input contract."""


@dataclass(frozen=True)
class OpenQuestion:
    identifier: str
    report_line: int
    description: str
    key_terms: frozenset[str]
    quantity_terms: frozenset[str]

    @property
    def token(self) -> str:
        return f"OPEN[{self.identifier}]"


@dataclass(frozen=True)
class Collision:
    identifier: str
    path: str
    line: int
    text: str


def _canonical_term(word: str) -> str:
    term = word.replace("_", "").casefold()
    if term in {"degree", "degrees"}:
        return "deg"
    return term


def _terms(text: str) -> frozenset[str]:
    values = {_canonical_term(word) for word in WORD_RE.findall(text)}
    return frozenset(
        term for term in values if len(term) >= 2 and term not in STOP_TERMS
    )


def _identifier_terms(identifier: str) -> frozenset[str]:
    return _terms(" ".join(re.split(r"[^A-Za-z0-9_]+", identifier)))


def _quantity_terms(description: str) -> frozenset[str]:
    for fragment in re.split(r"(?<=[.!?;])\s+|\n+", description):
        without_token = OPEN_RE.sub(" ", fragment)
        if not RELATION_RE.search(without_token):
            continue
        cue = BOUND_CUE_RE.search(without_token)
        if cue is None:
            values = _terms(without_token)
            if values:
                return values
            continue
        # In the campaign's usual imperative form ("bound X in terms of Y"),
        # the bounded quantity is the text after the cue.  For passive forms,
        # retain both sides so "X is bounded by Y" does not discard X.
        after = without_token[cue.end() :]
        if re.match(r"\s+by\b", after, re.IGNORECASE):
            relevant = without_token
        else:
            relevant = after
        values = _terms(relevant)
        if values:
            return values
    return frozenset()


def _section_boundary(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if re.match(r"^#{1,6}\s", stripped):
        return True
    if re.match(r"^\*\*[^*].*\*\*(?:\s|$)", stripped):
        return True
    return bool(re.match(r"^[A-Z][A-Z0-9 _/()'-]{2,}\s{2,}\S", line))


def extract_raised_opens(report: str) -> tuple[OpenQuestion, ...]:
    """Extract entries explicitly presented as raised/opened by ``report``."""

    entries: list[tuple[str, int, str]] = []
    active = False
    current_identifier: str | None = None
    current_line = 0
    current_text: list[str] = []

    def finish_entry() -> None:
        nonlocal current_identifier, current_line, current_text
        if current_identifier is not None:
            entries.append(
                (
                    current_identifier,
                    current_line,
                    " ".join(part.strip() for part in current_text if part.strip()),
                )
            )
        current_identifier = None
        current_line = 0
        current_text = []

    def start_entry(token_text: str, lineno: int, description: str) -> None:
        nonlocal current_identifier, current_line, current_text
        finish_entry()
        match = OPEN_RE.search(token_text)
        if match is None:  # guarded by callers; retain a fail-closed invariant
            raise CollisionError(f"line {lineno}: malformed OPEN token")
        identifier = match.group(1).strip()
        if not identifier or len(identifier) > 160 or any(
            ord(char) < 32 for char in identifier
        ):
            raise CollisionError(f"line {lineno}: invalid OPEN identifier")
        current_identifier = identifier
        current_line = lineno
        current_text = [description]

    def start_entries(text: str, lineno: int) -> bool:
        """Start every same-line OPEN entry and reject broken bracket syntax."""

        tokens = list(OPEN_RE.finditer(text))
        remainder = OPEN_RE.sub("", text)
        if "OPEN[" in remainder:
            raise CollisionError(f"line {lineno}: malformed OPEN token")
        for index, token in enumerate(tokens):
            end = tokens[index + 1].start() if index + 1 < len(tokens) else len(text)
            start_entry(token.group(0), lineno, text[token.start() : end])
        return bool(tokens)

    for lineno, line in enumerate(report.splitlines(), start=1):
        raised = RAISED_RE.search(line)
        if raised is not None:
            finish_entry()
            active = True
            tail = line[raised.end() :]
            start_entries(tail, lineno)
            continue

        if active:
            if "OPEN[" in OPEN_RE.sub("", line):
                raise CollisionError(f"line {lineno}: malformed OPEN token")
            entry = ENTRY_RE.match(line)
            if entry is not None:
                start_entries(line[entry.start(1) :], lineno)
            elif OTHER_OPEN_STATUS_RE.search(line) or _section_boundary(line):
                finish_entry()
                active = False
            elif current_identifier is not None:
                current_text.append(line)
            continue

        inline = INLINE_RAISE_RE.search(line)
        if inline is not None:
            start_entries(line[inline.start(1) :], lineno)
            finish_entry()

    finish_entry()

    # Keep first-seen report order but merge repeated raised entries so one OPEN
    # cannot produce duplicate candidate lists.
    merged: dict[str, tuple[int, list[str]]] = {}
    for identifier, lineno, description in entries:
        if identifier not in merged:
            merged[identifier] = (lineno, [description])
        else:
            merged[identifier][1].append(description)

    questions: list[OpenQuestion] = []
    for identifier, (lineno, descriptions) in merged.items():
        description = " ".join(descriptions)
        key_terms = _identifier_terms(identifier)
        quantity_terms = _quantity_terms(description)
        if not quantity_terms:
            raise CollisionError(
                f"OPEN[{identifier}] at report line {lineno} lacks an explicit "
                "bounded-quantity description"
            )
        if not key_terms:
            raise CollisionError(
                f"{identifier!r} at report line {lineno} has no safe search terms"
            )
        questions.append(
            OpenQuestion(
                identifier,
                lineno,
                description,
                key_terms,
                quantity_terms,
            )
        )
    return tuple(questions)


def _read_utf8(path: Path, label: str) -> str:
    try:
        if path.is_symlink() or not path.is_file():
            raise OSError("not a regular non-symlink file")
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise CollisionError(f"cannot read {label} {path}: {exc}") from exc


def banked_corpus(root: Path, report: Path) -> tuple[Path, ...]:
    """Resolve the exact banked corpus, excluding the report being sealed."""

    try:
        root = root.resolve(strict=True)
        report_real = report.resolve(strict=True)
    except OSError as exc:
        raise CollisionError(f"cannot resolve root/report: {exc}") from exc

    xmodel = root / "xmodel"
    if xmodel.is_symlink() or not xmodel.is_dir():
        raise CollisionError(f"banked corpus directory is unavailable: {xmodel}")

    paths = list(xmodel.glob("*.md"))
    if not paths:
        raise CollisionError(f"banked corpus has no xmodel/*.md files: {xmodel}")
    # Corpus guard (round 20260904T0000Z systems upgrade): during a blind
    # ideation round the other same-round submissions must not be scanned,
    # and unsealed lane reports (receipt without final_status) are not banked.
    import re as _re
    m = _re.match(r"ideation-(\d{8}T\d{4}Z)-", report.name)
    round_tag = m.group(1) if m else None
    guarded: list[Path] = []
    for path in paths:
        if round_tag and path.name.startswith(f"ideation-{round_tag}-") \
                and not path.name.endswith("-packet.md"):
            continue
        receipt = path.with_suffix(".run.v2")
        if receipt.is_file():
            try:
                if "final_status=" not in receipt.read_text(errors="replace"):
                    continue
            except OSError:
                continue
        guarded.append(path)
    paths = guarded
    paths.extend(root / name for name in REQUIRED_TOP_LEVEL)

    result: list[Path] = []
    for path in sorted(paths, key=lambda item: item.as_posix()):
        try:
            resolved = path.resolve(strict=True)
        except OSError as exc:
            raise CollisionError(f"cannot resolve corpus path {path}: {exc}") from exc
        if resolved == report_real:
            continue
        if path.is_symlink() or not path.is_file():
            raise CollisionError(f"corpus entry is not a regular non-symlink file: {path}")
        result.append(path)
    return tuple(result)


def find_collisions(
    questions: Sequence[OpenQuestion],
    corpus: Iterable[Path],
    root: Path,
    *,
    context_lines: int = DEFAULT_CONTEXT_LINES,
    max_candidates: int = DEFAULT_MAX_CANDIDATES,
) -> tuple[Collision, ...]:
    """Return deterministic lexical candidates; no result implies closure."""

    if context_lines < 0 or context_lines > 50:
        raise CollisionError("context_lines must be between 0 and 50")
    if max_candidates < 1 or max_candidates > 1000:
        raise CollisionError("max_candidates must be between 1 and 1000")
    try:
        root_real = root.resolve(strict=True)
    except OSError as exc:
        raise CollisionError(f"cannot resolve corpus root {root}: {exc}") from exc

    matches: list[Collision] = []
    for path in corpus:
        text = _read_utf8(path, "corpus file")
        lines = text.splitlines()
        line_terms = [_terms(line) for line in lines]
        try:
            display_path = path.resolve(strict=True).relative_to(root_real).as_posix()
        except (OSError, ValueError) as exc:
            raise CollisionError(f"corpus path escapes root: {path}") from exc

        for index, line in enumerate(lines):
            if not RELATION_RE.search(line):
                continue
            # A banked inequality may still carry the OPEN label under which
            # it was recorded.  That label is provenance, not a reason to
            # suppress an otherwise matching candidate.  Only generated
            # collision-output lines are excluded here; the report itself is
            # already excluded from the corpus by ``banked_corpus``.
            if "COLLISIONS" in line:
                continue
            low = max(0, index - context_lines)
            high = min(len(lines), index + context_lines + 1)
            context = frozenset().union(*line_terms[low:high])
            on_line = line_terms[index]

            for question in questions:
                # The adopted card says key nouns *plus* the bounded quantity,
                # so do not weaken an identifier to an arbitrary two-token OR.
                key_need = len(question.key_terms)
                if key_need and len(question.key_terms & context) < key_need:
                    continue
                if question.key_terms and not question.key_terms & on_line:
                    continue
                quantity = question.quantity_terms
                context_need = min(2, len(quantity))
                if context_need and len(quantity & context) < context_need:
                    continue
                line_need = 2 if len(quantity) >= 3 else 1
                if len(quantity & on_line) < line_need:
                    continue
                snippet = " ".join(line.strip().split())
                if len(snippet) > 240:
                    snippet = snippet[:237] + "..."
                matches.append(
                    Collision(question.identifier, display_path, index + 1, snippet)
                )
                if sum(
                    match.identifier == question.identifier for match in matches
                ) > max_candidates:
                    raise CollisionError(
                        f"{question.token} produced more than {max_candidates} "
                        "candidates; refine its bounded-quantity description"
                    )

    return tuple(
        sorted(matches, key=lambda item: (item.identifier, item.path, item.line))
    )


def render_collisions(
    questions: Sequence[OpenQuestion], collisions: Sequence[Collision]
) -> str:
    """Render the mandatory Markdown block, including explicit empty states."""

    grouped: dict[str, list[Collision]] = {question.identifier: [] for question in questions}
    for collision in collisions:
        grouped.setdefault(collision.identifier, []).append(collision)

    output = ["## COLLISIONS", ""]
    if not questions:
        output.extend(
            [
                "status: EMPTY",
                "",
                "- NONE — the report contains no explicitly raised `OPEN[...]` entries.",
            ]
        )
    else:
        output.append("status: CANDIDATES" if collisions else "status: EMPTY")
        output.append("")
        for question in questions:
            candidates = grouped.get(question.identifier, [])
            if not candidates:
                output.append(
                    f"- `{question.token}` (report:{question.report_line}): NONE"
                )
                output.append("")
                continue
            output.append(f"### {question.token}")
            output.append("")
            for candidate in candidates:
                output.append(
                    f"- `{candidate.path}:{candidate.line}` — {candidate.text}"
                )
            output.append("")
        while output[-1] == "":
            output.pop()
    return "\n".join(output) + "\n"


def _error_block(reason: str) -> str:
    safe_reason = " ".join(reason.splitlines())
    return f"## COLLISIONS\n\nstatus: ERROR\n\n- scan failed closed: {safe_reason}\n"


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description=__doc__)
    value.add_argument("report", type=Path, help="unsealed Markdown report")
    value.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root containing xmodel/ and the banked top-level files",
    )
    value.add_argument(
        "--context-lines",
        type=int,
        default=DEFAULT_CONTEXT_LINES,
        help="lines on either side used to match key nouns (default: 8)",
    )
    value.add_argument(
        "--max-candidates",
        type=int,
        default=DEFAULT_MAX_CANDIDATES,
        help="fail closed above this many candidates per OPEN (default: 100)",
    )
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        report_text = _read_utf8(args.report, "report")
        questions = extract_raised_opens(report_text)
        corpus = banked_corpus(args.root, args.report)
        collisions = find_collisions(
            questions,
            corpus,
            args.root,
            context_lines=args.context_lines,
            max_candidates=args.max_candidates,
        )
    except CollisionError as exc:
        print(_error_block(str(exc)), end="")
        print(f"open_collision: {exc}", file=sys.stderr)
        return 2
    print(render_collisions(questions, collisions), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
