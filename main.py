"""Write the dog's excuse for eating the homework to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = (
    "In my defense, it was a ruff draft, and you said yourself "
    "it needed to be torn apart."
)


def main() -> None:
    # The gate reads exactly this one line from /output/entry.txt.
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
