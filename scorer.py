import re

from rapidfuzz import fuzz

# rapidfuzz so that llm can have some flexibility in its answers.
# partial_ratio slides `expects` along `answer` and scores the best-matching
# window, so a short phrase inside a long answer still scores ~100 when present
# and stays high for small differences ("7 am to 1 pm" vs "7am to 1pm").
THRESHOLD = 85


def _normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)   # drop punctuation
    return re.sub(r"\s+", " ", text).strip()


def judge(question, expects, answer, results) -> bool:
    expects, answer = _normalize(expects), _normalize(answer)
    if not expects:
        return False
    if expects in answer:
        return True
    return fuzz.partial_ratio(expects, answer) >= THRESHOLD

def retrieval_hits(expects, results) -> bool:
    """Did retrieval return a document that contains the expected answer?"""
    expects = _normalize(expects)
    for doc in results:
        if expects in _normalize(doc.get("text", "")):
            return True
    return False
