import json
from pathlib import Path

# Where the log lives: a "logs" folder next to this file.
LOG_DIR = Path(__file__).parent / "logs"
LOG_FILE = LOG_DIR / "runs.jsonl"


def log_run(record):
    """Add one record (a dictionary) to the log as a single line of JSON."""
    # Make the logs folder the first time; do nothing if it already exists.
    LOG_DIR.mkdir(exist_ok=True)

    # "a" = append: add to the end of the file instead of erasing it ("w" would erase).
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
