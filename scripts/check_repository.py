import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".yml",
    ".yaml",
    ".txt",
    ".cff",
    ".csv",
    ".ipynb",
}

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".ipynb_checkpoints",
}

SKIP_FILES = {
    "check_repository.py",
    "patch_notebook_paths.py",
}

FORBIDDEN_PATTERNS = [
    "/Users/",
    "C:\\Users",
    "OneDrive",
    "/Desktop/",
    "A mobility-informed SIR model for regional transmission dynamics",
    "Shin J, Ahn S, Kim M",
]

REQUIRED_README_PHRASES = [
    "01_mobility_factor_2016_2017.ipynb",
    "03_rt_estimation_2016_2017.ipynb",
    "gamma",
    "No `theta` parameter is used",
    "sigma = 1.0 / 4.1",
]


def should_skip(path: Path) -> bool:
    if path.name in SKIP_FILES:
        return True
    return any(part in SKIP_DIRS for part in path.parts)


def read_text_file(path: Path) -> str:
    if path.suffix == ".ipynb":
        with path.open("r", encoding="utf-8") as f:
            json.load(f)
        return path.read_text(encoding="utf-8")

    return path.read_text(encoding="utf-8")


def main() -> None:
    problems = []

    citation_file = ROOT / "CITATION.cff"
    if not citation_file.exists():
        problems.append(("CITATION.cff", "missing root citation file"))

    hidden_citation_file = ROOT / ".CITATION.cff"
    if hidden_citation_file.exists():
        problems.append((".CITATION.cff", "rename this file to CITATION.cff"))

    readme_file = ROOT / "README.md"
    if not readme_file.exists():
        problems.append(("README.md", "missing README.md"))
    else:
        readme_text = readme_file.read_text(encoding="utf-8")
        for phrase in REQUIRED_README_PHRASES:
            if phrase not in readme_text:
                problems.append(("README.md", f"missing required phrase: {phrase}"))

    for path in ROOT.rglob("*"):
        if should_skip(path) or not path.is_file():
            continue

        if path.suffix not in TEXT_SUFFIXES:
            continue

        try:
            text = read_text_file(path)
        except UnicodeDecodeError:
            continue
        except json.JSONDecodeError as exc:
            problems.append((str(path.relative_to(ROOT)), f"invalid notebook JSON: {exc}"))
            continue

        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                problems.append((str(path.relative_to(ROOT)), f"forbidden pattern found: {pattern}"))

    if problems:
        print("Repository check failed:")
        for file_path, message in problems:
            print(f"- {file_path}: {message}")
        raise SystemExit(1)

    print("Repository check passed.")


if __name__ == "__main__":
    main()
