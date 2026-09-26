"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


def _split_into_sentences(paragraph: str) -> list[str]:
    """Split a paragraph into sentences, without dropping any text."""
    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(paragraph) if s.strip()]
    return sentences or [paragraph.strip()]


def _sentence_overlap(text: str, max_chars: int) -> str:
    """
    The longest suffix of `text` made of whole sentences that still fits in
    `max_chars`. Used as the overlap carried into the next chunk, so a chunk
    never *opens* mid-sentence either. Only looks at the last paragraph, so
    overlap never reaches back across a paragraph break.
    """
    if not text:
        return ""
    last_para = text.split("\n\n")[-1]
    tail = ""
    for sentence in reversed(_split_into_sentences(last_para)):
        candidate = f"{sentence} {tail}".strip()
        if len(candidate) > max_chars:
            break
        tail = candidate
    return tail


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks.

    Paragraphs are the unit of splitting: a whole paragraph goes into a chunk
    together whenever it fits. When a single paragraph is too long to fit in
    one chunk on its own, it's broken on sentence boundaries instead of a raw
    character count, so a chunk never opens or closes mid-sentence. The
    overlap carried between consecutive chunks is trimmed to whole sentences
    for the same reason.
    """
    chunk_size = 400
    overlap_chars = 75

    chunks: list[Chunk] = []
    for doc in documents:
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", doc.text) if p.strip()]

        # Flatten into (text, is_new_paragraph) units: a whole paragraph when
        # it fits on its own, otherwise its individual sentences.
        units: list[tuple[str, bool]] = []
        for para in paragraphs:
            if len(para) <= chunk_size:
                units.append((para, True))
            else:
                for i, sentence in enumerate(_split_into_sentences(para)):
                    units.append((sentence, i == 0))

        index = 0
        current = ""
        for text, is_new_paragraph in units:
            sep = "\n\n" if is_new_paragraph else " "
            candidate = f"{current}{sep}{text}" if current else text

            # Accept the candidate if it fits, or if `current` is empty —
            # the latter means this single unit is already too long on its
            # own, and we keep it whole rather than cut it mid-sentence.
            if len(candidate) <= chunk_size or not current:
                current = candidate
                continue

            chunks.append(
                Chunk(
                    text=current,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )
            index += 1

            tail = _sentence_overlap(current, overlap_chars)
            current = f"{tail}\n\n{text}" if tail else text

        if current:
            chunks.append(
                Chunk(
                    text=current,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
