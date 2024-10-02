"""
Automatically generate README.md
Creates category headings and links to writings.
"""

from pathlib import Path

ROOT = Path(__file__).absolute().parent

WRITINGS = {
    "fourier_me.txt": ["humans"],
    "free_will.txt": ["humans"],
    "mary.txt": ["consciousness", "physics"],
    "quotations.txt": ["humans", "natural language"],
    "rci.txt": ["lectures", "physics"],
    "relative_functionalism.txt": ["consciousness"],
    "teaching.txt": ["education"],
    "time.txt": ["physics"],
}

TEMPLATE = """
# Theories

Theories from an armchair philosopher.

None of this is rigorous or necessarily original.
These are simply thoughts that have came into my mind.

Credit is given where it is due.
""".strip() + "\n\n"


def main():
    categories = set()
    for c in WRITINGS.values():
        categories.update(c)
    categories = sorted(categories)

    text = TEMPLATE
    for c in categories:
        writings = []
        for w in WRITINGS.keys():
            if c in WRITINGS[w]:
                writings.append(w)
        writings = sorted(writings)

        text += f"### {c.capitalize()}\n\n"
        for w in writings:
            title = w.rsplit(".", 1)[0].replace("_", " ").capitalize()
            text += f"- [{title}](./src/{w})\n"
        text += "\n"

    (ROOT / "README.md").write_text(text)


if __name__ == "__main__":
    main()
