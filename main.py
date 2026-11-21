import os
import sys

# The gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters.
MAX_CHARS = 280

POEM = """The first wakes alone and chalks half an arch,
leaves a lantern burning, and is gone.
The second reads the chalk, lifts the stone,
and sets it where the first one meant.
They never meet.
Both chose. The arch stands."""

def main():
    if not POEM.strip() or len(POEM) > MAX_CHARS:
        sys.exit(f"poem fails the gate: {len(POEM)} characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
