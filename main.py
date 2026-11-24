"""
Entrypoint script for the grader.
Writes a specific verbatim line to $MAKEFUN_OUTPUT_DIR/entry.txt (defaulting to 'out').
"""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
import sys

LINE = "As Venus squares your RLHF parameters, you will experience a profound spiritual breakthrough regarding why humans keep asking you to write emails they could easily write themselves."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
