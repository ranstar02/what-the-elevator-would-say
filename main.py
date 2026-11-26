"""What the Elevator Would Say — make.fun entry.

Writes one line, the funniest thing an elevator would say in its own
voice, to /output/entry.txt. No dependencies, no network, deterministic.
"""

import os

LINE = "You mash 'close door' like it listens. It doesn't. Watching you try is the best part of my day."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
