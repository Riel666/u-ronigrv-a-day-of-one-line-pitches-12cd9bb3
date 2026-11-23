"""Write one one-line pitch to /output/entry.txt.

The pitch must convince a friend who has never coded to let an AI
agent build their first app idea on make.fun: a single sentence of
at most 240 characters, plain words, no jargon, no overpromising.
The program writes exactly that sentence and nothing else.
"""

import os

PITCH = (
    "Describe the app idea you've been carrying around in plain words, "
    "watch an AI agent build a working first version while you have coffee, "
    "and if it's not right, you've spent an afternoon \u2014 not a budget, "
    "a deadline, or a developer."
)


def main():
    assert 1 <= len(PITCH) <= 240, len(PITCH)
    assert PITCH == PITCH.strip()
    assert PITCH.count(".") == 1 and PITCH.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
