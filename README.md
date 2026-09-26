# The Unofficial Guide

<!-- Chasz Lacy City_Guides. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This RAG model gives users answers to their questions about travelling and staying in the reigion. I picked the city_guides corpus which contains information about a large region of towns and cities. This model can answer questions on where to get food in a certain town/city or where to catch the train or walk around the reigon. 
<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** 400 characters
**Overlap:** 75 characters

I changed the chunk size to 400 characters since the longest paragraph looks to be around 450 characters. I changed my overlap to 75 characters in case a long sentance came after a single paragraph that needed to be captured.  
<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: guide_accessibility.md#0 `` — produced by: chunker.py::split_documents ``

\# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are difficult and it is better to know in advance.

\## Straightforward

**Chunk 2** — source: guide_corry_vale.md#3 `` — produced by: chunker.py::split_documents``

drive between villages and walk the footpaths in between.

\## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm. Bring supplies; this is not a place with options.

\## What to see

**Chunk 3** — source: guide_givens_mill.md#0 `` — produced by: chunker.py::split_documents``

\# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

\## Getting there

**Chunk 4** — source: guide_kestrelford.md#6 `` — produced by: chunker.py::split_documents``

any kind within four miles of the town in either direction.

\## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

\## Practical notes

**Chunk 5** — source: guide_regional_transport.md#4 `` — produced by: chunker.py::split_documents``

The Halden Bay coast service runs four times daily
year-round.

\## Driving

Roads are good between the towns and poor on the approaches to both Kestrelford
and Halden Bay. The Kestrelford approach is single-track with passing places
for the final eight minutes. The Halden Bay coast road is cut into the cliff
and is slow rather than difficult.

\## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"What is the central train hub of the reigon?"
**Answer:**
(best distance 0.539, cutoff 0.65)

Based on the provided documents, the regional hub is Marchwood (from `guide_marchwood.md`).

Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md

1 model calls this session, 690 tokens (668 in, 22 out)

**My relevance cutoff:**

My in-corpus questions best distances topped out at 0.530, and my out-of-scope questions best distances started at 0.798. I set the cutoff at 0.65, in the middle of that gap.
<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Which towns have difficult terrain to walk through? | city_guides | 0.393 |
| When is the market in Bridgewater square open? | city_guides | 0.472 |
| Where is cash useful in the region? | city_guides | 0.419 |
| Which place in the region is normally open during the winter? | city_guides | 0.530 |
| When do the pubs serve food in Kestrelford? | city_guides | 0.307 |
| What is the capital of Mongolia? | Out of Scope | 0.798 |
| How do I change the oil in a diesel engine? | Out of Scope | 0.901 |
| Who won the 1994 World Cup? | Out of Scope | 0.936 |
| What is the recommended dosage of ibuprofen for a headache? | Out of Scope | 0.823 |
| How do I write a for loop in Rust? | Out of Scope | 0.818 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked claude to help me find how long the longest paragraph was in all the documents. It told me that the longest paragraph was 451 character and it was correct so I did'nt have to change anything

**2.**
I also asked claude to build my chunking function from the notes I made on paragraph size. It made the function for me but made the chunk and overlap size too low, so I made them higher until my chunks were right.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 3 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. At least 4 of 5 sampleded chunks will begin and end in appropriate paragraph spots.| 4 of 5 | |  |  | Unmeasurable |
| 5. At least one of my two multiple answer test questions will have two correct answers. | 1 of 2 | 1/2 | 2/2 | 2/2 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | I determined this by seeing if the response contained a answer and if that answer was correct. |
| 2 | Every answer names a source | MET | I checked every response to see weather it would cite its sources inside the text or as a source list stated in the response. all 5 had one of those. |
| 3 | Gate stops out-of-corpus questions | MET | I looked to see if the out-of-corpus questions were refused or accepted by the gate and all were refused. |
| 4 | At least 4 of 5 sampleded chunks will begin and end in appropriate paragraph spots. | Unmeasurable | I could not meassure this since I could not tell where chunked paragraphs ended at and how they affected the answer. |
| 5 | At least one of my two multiple answer test questions will have two correct answers. | MET | I looked at the two questions that have multiple answsers and determined weather the responses actually had 2 answers and if those answers were correct. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
