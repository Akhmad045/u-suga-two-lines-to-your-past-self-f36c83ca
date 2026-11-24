#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes a two-line warning to my past self
to /output/entry.txt.

Line one warns my past self about one specific moment in a single sentence:
the phone call to my father on Tuesday, 12 March, and the exact sentence I
said out loud. Line two says in one sentence why that moment mattered and
what changed because of it: he died on Thursday, so that sentence is the
last thing he ever heard from me. A quoted sentence, a date, and an
irreversible consequence — no wasted words.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

ENTRY = ("Don't say 'I'll come next weekend' to your father on the phone "
         "on Tuesday, 12 March.\n"
         "He died on Thursday, and that sentence is the last thing he ever "
         "heard from you.")

MAX_CHARS = 280


def validate(text):
    """Enforce the competition gate: 1-280 chars, not only whitespace,
    exactly two lines, each a single sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) == 0:
        raise ValueError("entry is empty (gate needs 1-280 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the 280-character gate"
        )
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(
            f"entry must be exactly two lines, got {len(lines)}"
        )
    for i, line in enumerate(lines, 1):
        if line.strip() == "":
            raise ValueError(f"line {i} is empty")
        if line != line.strip():
            raise ValueError(f"line {i} has leading or trailing whitespace")
        if line[-1] not in ".!?":
            raise ValueError(
                f"line {i} must end with sentence punctuation"
            )
        if ". " in line or "! " in line or "? " in line:
            raise ValueError(
                f"line {i} must be a single sentence"
            )
    return text


def self_test():
    """Exercise validate() against the gate's rejection cases."""
    cases = [
        ("", "empty"),
        (" ", "whitespace-only"),
        ("x" * 281, "281 chars"),
        ("one line only", "single line"),
        ("a.\nb.\nc.", "three lines"),
        ("trailing \nb.", "trailing whitespace"),
        ("a.\n b.", "leading whitespace on line 2"),
        ("no punctuation\nyes.", "line 1 without sentence punctuation"),
        ("Two sentences here. Really.\nSecond line.",
         "two sentences in line 1"),
        ("\n", "only a newline"),
    ]
    for text, label in cases:
        try:
            validate(text)
        except ValueError as exc:
            print(f"self-test ok: rejected {label}: {exc}")
        else:
            raise SystemExit(f"self-test FAIL: {label} was accepted")
    # boundary: exactly 280 chars across two lines must pass
    boundary = "a" * 139 + ".\n" + "b" * 138 + "."
    assert len(boundary) == 280, len(boundary)
    validate(boundary)
    print("self-test ok: 280-char boundary accepted")
    # the entry itself must pass
    validate(ENTRY)
    print("self-test ok: entry accepted")
    print("self-test: all cases passed")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(ENTRY)
    data = text.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the entry
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print(f"wrote {out_path}: {len(text)} chars, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
