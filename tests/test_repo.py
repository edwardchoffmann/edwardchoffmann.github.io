from pathlib import Path


def test_readme_exists() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "README.md").is_file()
