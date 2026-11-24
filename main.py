# One Line of Earned Pride — u-mang-one-line-of-earned-pride-a0138557
# makefun anchor 5e0463eb33adb72a01021f772cd768fae8c69e5d round 34230529
# Writes a single line of quiet, earned pride to /output/entry.txt.
# Stdlib only, deterministic, no trailing newline.
import os

LINE = "Maya stuttered through every school assembly; today she read the morning announcements without a single stumble, and the whole cafeteria kept eating — like it was ordinary."

# Gate: entry must be 1-240 chars of UTF-8 text, not whitespace-only.
MAX_CHARS = 240
assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line outside 1-240 chars"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
