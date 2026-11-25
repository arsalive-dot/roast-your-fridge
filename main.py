"""One-line fridge roast for make.fun's One Line, One Laugh: Roast Your Fridge.

Writes the entry to /output/entry.txt deterministically.

The roast is built for the judge's brief: it names a specific, recognisable
detail (an ice maker that has produced three cubes since 2019), and the
twist pays off in the last few words — the lazy appliance acting as if it
is doing its owner a favour.
"""

import os

ENTRY = "My fridge's ice maker has made three cubes since 2019 and still acts like it's doing me a favour."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
