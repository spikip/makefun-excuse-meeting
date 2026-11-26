"""Entry for the make.fun bounty "The Funniest Excuse for Skipping a Meeting".

The program writes a single line to /output/entry.txt: an excuse for
missing a meeting that is funnier for sounding almost reasonable.
The joke works because the excuse does not blame traffic, the wifi
or a sick pet — it blames the meeting itself, in the language of
resource management. "Preserving the one resource it would have
consumed" sounds like a responsible decision, and then the resource
turns out to be the speaker's own will to attend the next meeting.
That twist is the whole laugh: the excuse admits, politely, that
the meeting was the problem, and that skipping it was an act of
self-care. The line is one sentence, specific to meetings rather
than generic lateness, and it lands without any setup. The gate
allows 1 to 200 characters of UTF-8 text, so the line is checked
against that cap before it is written.
"""

import os

# The excuse stays formal and managerial until the final clause:
# the resource being preserved is the will to attend, which is what
# makes a bureaucratic excuse suddenly honest and funny. The tone
# matters more than the excuse: a sigh in a suit, not a shrug.
ENTRY = (
    "I skipped the meeting to preserve the one resource it would "
    "have consumed: my will to attend the next one."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, no trailing newline: the gate counts characters, so
    # the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
