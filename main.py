"""One Star, Written in Sap - Round 2 entry program.

Writes a single one-line 1-star review, in the voice of a houseplant,
to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "One star. He eats salad in front of me, crunching my cousins "
    "while I sit here in dry soil. I am not decor, I am a witness "
    "to a massacre."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
