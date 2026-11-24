"""Two-sentence horror entry writer.

Writes a two-sentence horror story to /output/entry.txt as UTF-8
text and forces the output file mode to 0644 so the grader can read it.
"""

import os

# The story text. Must be 1-400 characters and exactly two sentences.
ENTRY_TEXT = "Tonight was my turn to read to our daughter, so I opened her bedroom door at eight. She was already asleep, and the voice reading to her did not stop."

OUTPUT_PATH = "/output/entry.txt"


def sentence_count(text):
    """Count sentences by splitting on full stops, ignoring empties."""
    return len([part for part in text.split(".") if part.strip()])


def check_entry(text):
    """Raise if the entry breaks the contest gate."""
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1-400 characters, got %d" % len(text))
    if sentence_count(text) != 2:
        raise ValueError("entry must be exactly two sentences")


def write_entry():
    """Validate the text, write it out, and lock the mode to 0644."""
    check_entry(ENTRY_TEXT)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    write_entry()
