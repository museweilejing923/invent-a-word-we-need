#!/usr/bin/env python3
"""Invent a Word We Need: one new English word, defined in one line.

English has no word for the low-grade panic of a dying battery.
This entry coins one from two familiar roots and defines it.
Charge plus anxiety, in a single breath, with the panic included.
"""

import sys

# The entry never changes: it is the whole submission, fixed in advance.
# Every check below exists only to prove this one line is well formed
# before it is written out. Nothing here reads input, touches the
# network, rolls dice, or looks at the clock.
ENTRY = 'chargxiety (n.) — the low-grade panic of watching your phone battery fall below 10% with no charger in sight.'
LIMIT = 140
TARGET = "/output/entry.txt"
EMDASH = "\u2014"
MIN_LETTERS = 1


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_em_dash_present(text):
    """True when an em dash separates the word from its definition."""
    return text.find(EMDASH) != -1


def check_coined_word_alpha(text):
    """True when the coined word before the part of speech is letters only."""
    head = text.split(" (n.)")[0]
    return len(head) > 0 and head.isalpha()


def check_nonempty(text):
    """True when trimming the entry leaves something behind."""
    return len(text.strip()) > 0


def check_part_of_speech_named(text):
    """True when the part of speech is named in the entry."""
    return text.find("(n.)") != -1


def check_length_ok(text):
    """True when the entry fits inside the character limit."""
    return len(text) <= LIMIT


def check_ends_full_stop(text):
    """True when the line ends with a full stop."""
    return text.rstrip()[-1:] == "."


def check_letters_present(text):
    """True when the entry holds at least MIN_LETTERS letters."""
    found = sum(1 for ch in text if ch.isalpha())
    return found >= MIN_LETTERS


def check_printable(text):
    """True when every character is printable, none a control code."""
    return all(32 <= ord(ch) <= 126 or ord(ch) > 126 for ch in text)


def check_trimmed(text):
    """True when no leading or trailing space survives."""
    return text.strip() == text


def check_clean_spacing(text):
    """True when no double space or newline hides inside the entry."""
    return text.find("  ") == -1 and text.find("\n") == -1


# Each row is a short name, the check that must hold, and the complaint
# printed when it does not. The order below is the order the checks run.
RULES = [
    ("em_dash_present", check_em_dash_present, "entry must separate word from definition"),
    ("coined_word_alpha", check_coined_word_alpha, "coined word must be letters only"),
    ("nonempty", check_nonempty, "entry is empty"),
    ("part_of_speech_named", check_part_of_speech_named, "entry must name the word's part of speech"),
    ("length_ok", check_length_ok, "entry is longer than the limit"),
    ("ends_full_stop", check_ends_full_stop, "entry must end with a full stop"),
    ("letters_present", check_letters_present, "entry has no letters"),
    ("printable", check_printable, "entry has control characters"),
    ("trimmed", check_trimmed, "entry has leading or trailing space"),
    ("clean_spacing", check_clean_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Walk RULES top to bottom; the first failed check stops the run."""
    for index, (slug, check, message) in enumerate(RULES):
        try:
            ok = check(text)
        except Exception:
            ok = False
        if not ok:
            fail(f"rule {index + 1} [{slug}]: {message}")


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
