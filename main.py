"""Make the AI judge laugh — ai-joke-02.

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no input.
Runs twice -> identical bytes.
"""

from pathlib import Path

JOKE = (
    "My AI coding agent wrote 500 lines in 10 seconds. "
    "490 were wrong, but it apologized so politely "
    "I promoted it to senior."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
