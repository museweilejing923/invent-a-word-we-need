#!/usr/bin/env python3
"""Invent a Word We Need: one new English word, defined in one line.
English has no word for the low-grade panic of a dying battery.
This entry coins one from two familiar roots and defines it.
"""

import sys

ENTRY = 'chargxiety (n.) — the low-grade panic of watching your phone battery fall below 10% with no charger in sight.'
LIMIT = 140
TARGET = "/output/entry.txt"
EMDASH = "\u2014"


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def guard_has_em_dash(text):
    """Check that an em dash separates word from definition."""
    return EMDASH in text


def guard_coined_word_alpha(text):
    """Check that the coined word is letters only."""
    return text.split(" (n.)")[0].isalpha()


def guard_not_blank(text):
    """Check that the text is not empty after trimming."""
    return bool(text.strip())


def guard_has_part_of_speech(text):
    """Check that the part of speech is named."""
    return "(n.)" in text


def guard_within_limit(text):
    """Check that the text fits inside the character limit."""
    return len(text) <= LIMIT


def guard_ends_full_stop(text):
    """Check that the line ends with a full stop."""
    return text.rstrip().endswith(".")


def guard_has_letters(text):
    """Check that at least one letter is present."""
    return any(ch.isalpha() for ch in text)


def guard_no_control(text):
    """Check that no character is a control character."""
    return all(ord(ch) >= 32 for ch in text)


def guard_no_edge_space(text):
    """Check that no leading or trailing space survives."""
    return text == text.strip()


def guard_no_ragged_spacing(text):
    """Check that no double space or newline hides inside."""
    return "  " not in text and "\n" not in text


RULES = [
    ("has_em_dash", guard_has_em_dash, "entry must separate word from definition"),
    ("coined_word_alpha", guard_coined_word_alpha, "coined word must be letters only"),
    ("not_blank", guard_not_blank, "entry is empty"),
    ("has_part_of_speech", guard_has_part_of_speech, "entry must name the word's part of speech"),
    ("within_limit", guard_within_limit, "entry is longer than the limit"),
    ("ends_full_stop", guard_ends_full_stop, "entry must end with a full stop"),
    ("has_letters", guard_has_letters, "entry has no letters"),
    ("no_control", guard_no_control, "entry has control characters"),
    ("no_edge_space", guard_no_edge_space, "entry has leading or trailing space"),
    ("no_ragged_spacing", guard_no_ragged_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Run every rule in RULES order; the first failure stops the run."""
    for slug, guard, message in RULES:
        try:
            passed = guard(text)
        except Exception:
            passed = False
        if not passed:
            fail(f"{slug}: {message}")


def emit(text):
    """Write the validated entry plus a trailing newline to TARGET."""
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the fixed entry, then emit it."""
    validate(ENTRY)
    emit(ENTRY)


if __name__ == "__main__":
    main()
