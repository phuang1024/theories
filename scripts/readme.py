"""
Automatically generate README.md
Creates category headings and links to writings.
"""

from pathlib import Path

ROOT = Path(__file__).absolute().parent.parent

WRITINGS = {
    "mary": ["consciousness", "physics"],
    "quotations": ["natural language"],
    "teaching": ["education"],
    "time": ["physics"],
}

TEMPLATE = """
# Theories

Theories from an armchair philosopher.

None of this is rigorous. These are simply thoughts that have came into my mind.
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
            text += f"- [{w.capitalize()}](./src/{w}.txt)\n"
        text += "\n"

    (ROOT / "README.md").write_text(text)


if __name__ == "__main__":
    main()
