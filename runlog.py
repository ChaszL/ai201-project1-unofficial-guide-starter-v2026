import json
from pathlib import Path

# Where the log lives: a "logs" folder next to this file.
LOG_DIR = Path(__file__).parent / "logs"
LOG_FILE = LOG_DIR / "runs.jsonl"


def usage_snapshot():
    """Read generate.py's running totals for this session.

    generate.py only keeps totals for the whole time the server has been up.
    Take one snapshot when a request starts and compare it to the totals when
    the request ends: the difference is what that one request used.
    """
    import generate as gen

    tokens = gen.token_counts()
    return {
        "tokens_in": tokens["prompt"],
        "tokens_out": tokens["output"],
        "model_calls": gen.call_count(),
        "cache_hits": gen._cache_hits,
    }


def log_run(record, usage_before=None):
    """Add one record (a dictionary) to the log as a single line of JSON.

    If usage_before (a snapshot taken when the request started) is given,
    the tokens, model calls and cache hit for this request are added too.
    """
    if usage_before is not None:
        after = usage_snapshot()
        record["tokens_in"] = after["tokens_in"] - usage_before["tokens_in"]
        record["tokens_out"] = after["tokens_out"] - usage_before["tokens_out"]
        record["model_calls"] = after["model_calls"] - usage_before["model_calls"]
        # True if the answer came from the local cache instead of the API (cost 0).
        record["cache_hit"] = after["cache_hits"] > usage_before["cache_hits"]

    # Logging must never take the server down. If the file can't be written
    # (for example it's locked by another program), print a warning and move on.
    try:
        # Make the logs folder the first time; do nothing if it already exists.
        LOG_DIR.mkdir(exist_ok=True)

        # "a" = append: add to the end of the file instead of erasing it ("w" would erase).
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(f"[runlog] could not write log: {exc}")
