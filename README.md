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
| 4. At least 4 of 5 sampleded chunks will begin and end in appropriate paragraph spots.| 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 5. At least one of my two multiple answer test questions will be answered with the correct multiple answers. | 1 of 2 | 1/2 | 2/2 | 2/2 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

**Criterion 1**
- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
Q: When is the market in Bridgewater square open? — run 2
- Best distance: 0.4718 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_seasons.md

```
Brightwater's Tuesday market sets up at 7am in the square and is finished by 1pm. 

Source: guide_eating.md
```

**Criterion 2**
- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
Q: Where is cash useful in the region? — run 1
- Best distance: 0.4188 (passed the gate)
- Sources retrieved: guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md

```
Cash is still useful at the market and in smaller places. 
Sources: `guide_pellew_sands.md`, `guide_givens_mill.md`, `guide_marchwood.md`, `guide_elder_ness.md`, `guide_halden_bay.md`, and `guide_kestrelford.md`.
```

**Criterion 3**
Produced by run_eval.py::check_out_of_scope, cutoff 0.65. Refused 5 of 5

Q: What is the capital of Mongolia?
| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.798 | refused |
| How do I change the oil in a diesel engine? | 0.901 | refused |
| Who won the 1994 World Cup? | 0.936 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.823 | refused |
| How do I write a for loop in Rust? | 0.818 | refused |


**Criterion 4**
- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
Q: Which towns have difficult terrain to walk through? — run 2
- Best distance: 0.3930 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_halden_bay.md, guide_walking.md

```
Based on the provided documents:

* In Halden Bay, the town is built on three levels connected by stepped lanes, making it hard going with luggage or a pushchair, and everything above the level harbour front is not level (*guide_halden_bay.md*). 
* In Corry Vale, nothing within the valley is walkable from anything else as the villages are two to four miles apart, and the Corry Vale circuit is a moderate walk with hills, about nine miles with 500 metres of ascent (*guide_corry_vale.md* and *guide_walking.md*).
```


**Criterion 5**
- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
Q: Which place in the region is normally open during the winter? — run 1
- Best distance: 0.5298 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

```
Marchwood is one place in the region that works in winter, since almost everything is indoors and nothing closes seasonally (*guide_marchwood.md*). Additionally, Brightwater carries on during the winter because the university keeps it occupied (*guide_seasons.md*), and Thornby Wells is a reliable winter destination as its concert season runs from September to April (*guide_thornby_wells.md*).
```


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
| 4 | At least 4 of 5 sampleded chunks will begin and end in appropriate paragraph spots. | MET | I read my responses to see if they had complete sentance structure and if all sentances made sense without breaks and mid sentance stops. |
| 5 | At least one of my two multiple answer test questions will be answered with the correct multiple answers. | MET | I looked at the two questions that have multiple answsers and determined weather the responses actually had 2 answers and if those answers were correct. |

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

I did not miss any targets and honestly think my targets were set too low. There are two criteria I would change. First, I would change my chunking criterion: At least 4 of 5 sampleded chunks will begin and end in appropriate paragraph spots. This criteria was very simple and somewhat unmessurable. I want to change this because it was not specific enough and made it difficult for me to judge if everything was passing or not. I want to change it to all of my chunks will begin and end on a complete sentance with a complete thought on a paragraph. I also believe that my multiple answers criterion: "At least one of my two multiple answer test questions will be answered with the correct multiple answers." should be chnaged to all multiple answer questions will have all answers in the response. I want to tighten this because my previous scoring was only measuring if at least one of the answers were present. That means as long as the a respomse had at least one correct answer, it would pass. 

## The Improvement

**What I changed:**
I chnaged my chunking stategy. I used claude to help me make the chunks evenly split between subjects that have complete thoughts in the documents.

**Why I picked it:**
I chose this because I wanted to make sure my chunking for multiple choice questions would actually answer the question but also make sure that full sentence and thoughts are not left out like in the "Which towns have difficult terrain?" question where sentences are not flowing. 

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 3 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. All of my chunks will begin and end on a complete sentance with a complete thought on a paragraph.| 5/5 | 5/5 | 5/5 | 5/5 | MET |
| 5. All of my multiple answer test questions will have all the correct answers.| 2 of 2 | 1/2 | 1/2 | 1/2 | MISSED |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

My new chunking strategy did help with making the chunks contain full thought paragraphs and complete sentences, but I also noticed that in one specific question with three answers, one answers is always missing. So this new strategy made my chunks cleaner and better, but is still leaving out needed context. My criterion 4 has gone from unmeasured to 5/5 for each run, but my multiple answer test has gone from MET to MISSED. 

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

The criterion for answering multiple questions is still broken, I tried to adjust the top k and chunking to see if that would help it find all three answers. I am running out of time so I cannot investigate further. Right now answering a question with multiple answers is still broken. 

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

The criteria I would write differently is: All of my chunks will begin and end on a complete sentance with a complete thought on a paragraph. I think this one should be changed again to all the chunks will contain complete information about a subject rather than just stopping at the paragraph. That way the model will have context as well as full information. 

# Capstone

**What This Extends**
I am extending my RAG system for the city_guides corpus to include a single start command, structured logging that contains a record for every question, a cost measure, and a duration as well as timestamp of those questions.

**The Shape**
I chose Shape A (Deploy and instrument) and Path B (Running Locally): I choose these because I want to deploy this, but find navigating the URL hosting difficult. 

**Out of Scope**
I will not be changing my test questions, chunking, or top-k from unit two. I am not changing chunking and top-k because changing them in the past caused the model to give different answers, which were often wrong. I am not changing my test questions because then my before and after runs would not be measuring the same thing. 

**Running It**

Path B, local with logs. Full setup is in [RUNNING.md](RUNNING.md).

- **Python:** 3.13 (3.11–3.13 work; 3.14 does not)
- **Dependencies:** `pip install -r requirements.txt` (on Windows, install Microsoft C++ Build Tools first)
- **Model files:** all-MiniLM-L6-v2 embedding model, about 80 MB, downloaded automatically on the first run
- **Start command:**

      $env:AI201_CACHE = "0"; python serve.py

  The server runs at http://localhost:5000. Every request adds one line to `logs/runs.jsonl`.

**Instrumentation**

Every request to `/ask` writes one JSON line to `logs/runs.jsonl`, produced by `runlog.py::log_run`, called from `serve.py::ask`. Failed requests (bad input and crashes) are logged too.

| Field | What it holds |
|---|---|
| timestamp | When the request arrived (UTC) |
| status | answered, refused, bad_request, or error |
| http_status | 200, 400, or 500 |
| question | What came in |
| answer | What went out (null on failures) |
| refused | True if the relevance gate stopped it |
| best_distance | Closest chunk's distance (lower = closer) |
| threshold | The gate cutoff (0.65) |
| sources | Documents the answer came from |
| corpus / top_k | Which corpus, how many chunks retrieved |
| duration_ms | How long the request took |
| error | Error message on failures, otherwise null |
| tokens_in / tokens_out | Tokens this request used |
| model_calls | Model calls this request made |
| cache_hit | True if answered from the local cache (cost 0) |

Log extract (14 entries, pasted from `logs/runs.jsonl`):

```
{"timestamp": "2026-11-13T20:25:06.664+00:00", "status": "answered", "http_status": 200, "question": "When do the pubs serve food in Kestrelford?", "answer": "In Kestrelford, the pubs serve food between 12 and 2 and again between 6 and 8:30 (as stated in `guide_kestrelford.md` and `guide_eating.md`).", "refused": false, "best_distance": 0.2852, "threshold": 0.65, "sources": ["guide_corry_vale.md", "guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_kestrelford.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 948.9, "error": null, "tokens_in": 660, "tokens_out": 48, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:07.404+00:00", "status": "answered", "http_status": 200, "question": "Which towns have difficult terrain to walk through?", "answer": "Halden Bay is built on three levels connected by stepped lanes, making it hard going with luggage or a pushchair, and everything above the level harbour front is not level (*guide_halden_bay.md*). \n\nAdditionally, Corry Vale features a circuit with 500 metres of ascent, and its footpath network becomes genuinely boggy outside of May to September (*guide_corry_vale.md* and *guide_walking.md*).", "refused": false, "best_distance": 0.4307, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_halden_bay.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 696.1, "error": null, "tokens_in": 585, "tokens_out": 96, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:07.975+00:00", "status": "answered", "http_status": 200, "question": "When is the market in Brightwater square open?", "answer": "Brightwater's Tuesday market sets up at 7am in the square and is finished by 1pm. \n\nSource: guide_eating.md", "refused": false, "best_distance": 0.3394, "threshold": 0.65, "sources": ["guide_eating.md", "guide_halden_bay.md", "guide_seasons.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 566.2, "error": null, "tokens_in": 603, "tokens_out": 32, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:09.021+00:00", "status": "answered", "http_status": 200, "question": "Where is cash useful in the region?", "answer": "Cash is still useful at the market and in smaller places. \n\nThis information comes from the following documents:\n- `guide_givens_mill.md`\n- `guide_kestrelford.md`\n- `guide_corry_vale.md`\n- `guide_brightwater.md`\n- `guide_halden_bay.md`\n- `guide_marchwood.md`", "refused": false, "best_distance": 0.4397, "threshold": 0.65, "sources": ["guide_brightwater.md", "guide_corry_vale.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_kestrelford.md", "guide_marchwood.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 1042.9, "error": null, "tokens_in": 564, "tokens_out": 89, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:09.790+00:00", "status": "answered", "http_status": 200, "question": "Which place in the region is normally open during the winter?", "answer": "Marchwood works in winter, since almost everything is indoors and nothing closes seasonally (`guide_marchwood.md`). Thornby_wells is also a reliable winter destination, with a concert season running from September to April (`guide_thornby_wells.md`), and Brightwater carries on during the winter because the university keeps it occupied (`guide_seasons.md`).", "refused": false, "best_distance": 0.4761, "threshold": 0.65, "sources": ["guide_corry_vale.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_marchwood.md", "guide_seasons.md", "guide_thornby_wells.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 765.4, "error": null, "tokens_in": 601, "tokens_out": 75, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.303+00:00", "status": "answered", "http_status": 200, "question": "What is the central train hub of the region?", "answer": "The central train hub of the region is Marchwood (from `guide_marchwood.md`).", "refused": false, "best_distance": 0.51, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_brightwater.md", "guide_marchwood.md", "guide_pellew_sands.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 509.7, "error": null, "tokens_in": 642, "tokens_out": 20, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.332+00:00", "status": "refused", "http_status": 200, "question": "What is the capital of Mongolia?", "answer": "I don't have enough information about that.", "refused": true, "best_distance": 0.7981, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 25.7, "error": null, "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.360+00:00", "status": "refused", "http_status": 200, "question": "How do I change the oil in a diesel engine?", "answer": "I don't have enough information about that.", "refused": true, "best_distance": 0.9076, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 25.0, "error": null, "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.386+00:00", "status": "refused", "http_status": 200, "question": "Who won the 1994 World Cup?", "answer": "I don't have enough information about that.", "refused": true, "best_distance": 0.9758, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 22.8, "error": null, "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.388+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.1, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.392+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.0, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.394+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.0, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.396+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.1, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:25:10.399+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.0, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-13T20:47:27.752+00:00", "status": "answered", "http_status": 200, "question": "When is the best time of year to visit Kestrelford?", "answer": "According to the documents, June is excellent everywhere in the summer, and Kestrelford fills with walkers in July and August (`guide_seasons.md`).", "refused": false, "best_distance": 0.4053, "threshold": 0.65, "sources": ["guide_eating.md", "guide_elder_ness.md", "guide_marchwood.md", "guide_seasons.md", "guide_thornby_wells.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 906.9, "error": null, "tokens_in": 613, "tokens_out": 32, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-13T20:47:28.531+00:00", "status": "answered", "http_status": 200, "question": "What is Givens Mill known for?", "answer": "Givens Mill is known for its working watermill that commercially grinds flour, as well as its tearoom that sells bread made from that flour. People also visit for the mill tours, the church with its Saxon doorway, and the river walk downstream to Brightwater. \n\nSource: `guide_givens_mill.md`", "refused": false, "best_distance": 0.2505, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_brightwater.md", "guide_givens_mill.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 773.4, "error": null, "tokens_in": 633, "tokens_out": 69, "model_calls": 1, "cache_hit": false}
```

The first request made to the RAG system took longer than the other request which could be because the embedding model has to load before being able to finnish the request. All other request went through pretty fast after the embeding model was loaded. I also noticed that the tokens in and out for bad request are zero because there are no model cost.

**What It Costs**

Average tokens per answered question, ~622 tokens in and ~56 tokens out and an average duration of 946ms per answered question.

How I measured it: I ran 10 questions through the server with the cache off AI201_CACHE=0, then averaged the tokens_in and tokens_out fields from those 10 log lines. Refused questions cost 0 tokens.

The amount of tokens 100 uses would take a day would be around 67,800 tokens/day
100 (622 + 56) = 67,800




**Results -Before**

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. First answered request after a restart is under 3000 ms | 3 of 3 | 2,024 ms | 1,986 ms | 1,938 ms | MET |
| 2. Multi-answer questions have all answers correct | 2 of 2 each run | 1/2 | 1/2 | 1/2 | MISSED |
| 3. Every request ≤ 700 tokens in and ≤ 100 tokens out | 8 of 8 each run | 7/8 | 8/8 | 8/8 | MISSED |
| 4. Empty or missing question returns 400 and is logged | 2 of 2 each run | 2/2 | 2/2 | 2/2 | MET |
| 5. Every request is logged with timestamp, HTTP code and status | 8 of 8 each run | 8/8 | 8/8 | 8/8 | MET |

**Evidence (Run 1)**

All lines below are copied from `logs/runs.jsonl`. Produced by `serve.py` → `ask()`, which calls `app.py` → `ask_pipeline()` for the answer and writes the line with `runlog.py` → `log_run()` into `logs/runs.jsonl`.

*Criterion 1: cold start.* First request after restarting the server; `duration_ms` is 2024.0.

```json
{"timestamp": "2026-11-14T01:52:47.233+00:00", "status": "answered", "http_status": 200, "question": "Which towns have difficult terrain to walk through?", "answer": "Based on the provided documents, **Halden Bay** has difficult terrain because the town is built on three levels connected by stepped lanes, making it hard going with luggage or a pushchair, and everything above the level harbour front is not level (*guide_halden_bay.md*). \n\nAdditionally, the **Corry Vale** circuit involves moderate terrain with hills, including 500 metres of ascent, and the footpath network can become genuinely boggy outside of May to September (*guide_corry_vale.md* and *guide_walking.md*).", "refused": false, "best_distance": 0.4307, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_halden_bay.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 2024.0, "error": null, "tokens_in": 585, "tokens_out": 118, "model_calls": 1, "cache_hit": false}
```

*Criterion 2: multi-answer questions.* The `answer` field of the terrain and winter questions.

```json
{"timestamp": "2026-11-14T01:52:47.233+00:00", "status": "answered", "http_status": 200, "question": "Which towns have difficult terrain to walk through?", "answer": "Based on the provided documents, **Halden Bay** has difficult terrain because the town is built on three levels connected by stepped lanes, making it hard going with luggage or a pushchair, and everything above the level harbour front is not level (*guide_halden_bay.md*). \n\nAdditionally, the **Corry Vale** circuit involves moderate terrain with hills, including 500 metres of ascent, and the footpath network can become genuinely boggy outside of May to September (*guide_corry_vale.md* and *guide_walking.md*).", "refused": false, "best_distance": 0.4307, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_halden_bay.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 2024.0, "error": null, "tokens_in": 585, "tokens_out": 118, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:49.712+00:00", "status": "answered", "http_status": 200, "question": "Which place in the region is normally open during the winter?", "answer": "Marchwood is the one place in the region that works in winter, as almost everything is indoors and nothing closes seasonally (*guide_marchwood.md*). Thornby_wells is also described as a reliable winter destination (*guide_thornby_wells.md*).", "refused": false, "best_distance": 0.4761, "threshold": 0.65, "sources": ["guide_corry_vale.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_marchwood.md", "guide_seasons.md", "guide_thornby_wells.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 619.6, "error": null, "tokens_in": 601, "tokens_out": 55, "model_calls": 1, "cache_hit": false}
```

*Criterion 3: token cost.* The one request over a limit: `tokens_out` is 118 (limit 100). `tokens_in` is 585.

```json
{"timestamp": "2026-11-14T01:52:47.233+00:00", "status": "answered", "http_status": 200, "question": "Which towns have difficult terrain to walk through?", "answer": "Based on the provided documents, **Halden Bay** has difficult terrain because the town is built on three levels connected by stepped lanes, making it hard going with luggage or a pushchair, and everything above the level harbour front is not level (*guide_halden_bay.md*). \n\nAdditionally, the **Corry Vale** circuit involves moderate terrain with hills, including 500 metres of ascent, and the footpath network can become genuinely boggy outside of May to September (*guide_corry_vale.md* and *guide_walking.md*).", "refused": false, "best_distance": 0.4307, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_halden_bay.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 2024.0, "error": null, "tokens_in": 585, "tokens_out": 118, "model_calls": 1, "cache_hit": false}
```

*Criterion 4: empty or missing question.* Request bodies were `{"question": ""}` and `{"foo": "bar"}`; both returned 400 and were logged as `bad_request`.

```json
{"timestamp": "2026-11-14T01:52:50.383+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.1, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:50.385+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.0, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
```

*Criterion 5: every request logged.* 8 requests were sent in Run 1 and these are the 8 lines that were added, each with a timestamp, `http_status` and `status`.

```json
{"timestamp": "2026-11-14T01:52:47.233+00:00", "status": "answered", "http_status": 200, "question": "Which towns have difficult terrain to walk through?", "answer": "Based on the provided documents, **Halden Bay** has difficult terrain because the town is built on three levels connected by stepped lanes, making it hard going with luggage or a pushchair, and everything above the level harbour front is not level (*guide_halden_bay.md*). \n\nAdditionally, the **Corry Vale** circuit involves moderate terrain with hills, including 500 metres of ascent, and the footpath network can become genuinely boggy outside of May to September (*guide_corry_vale.md* and *guide_walking.md*).", "refused": false, "best_distance": 0.4307, "threshold": 0.65, "sources": ["guide_accessibility.md", "guide_corry_vale.md", "guide_halden_bay.md", "guide_walking.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 2024.0, "error": null, "tokens_in": 585, "tokens_out": 118, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:48.317+00:00", "status": "answered", "http_status": 200, "question": "When is the market in Bridgewater square open?", "answer": "Based on the documents provided, Brightwater's Tuesday market sets up in the square at 7am and is finished by 1pm. \n\nSource: `guide_brightwater.md` (and also mentioned in `guide_eating.md`)", "refused": false, "best_distance": 0.4162, "threshold": 0.65, "sources": ["guide_brightwater.md", "guide_eating.md", "guide_halden_bay.md", "guide_kestrelford.md", "guide_seasons.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 1065.1, "error": null, "tokens_in": 667, "tokens_out": 53, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:49.090+00:00", "status": "answered", "http_status": 200, "question": "Where is cash useful in the region?", "answer": "Cash is useful at the market and in smaller places. \n\nThis information comes from `guide_pellew_sands.md`, `guide_thornby_wells.md`, `guide_brightwater.md`, `guide_marchwood.md`, `guide_givens_mill.md`, and `guide_kestrelford.md`.", "refused": false, "best_distance": 0.4397, "threshold": 0.65, "sources": ["guide_brightwater.md", "guide_givens_mill.md", "guide_kestrelford.md", "guide_marchwood.md", "guide_pellew_sands.md", "guide_thornby_wells.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 748.1, "error": null, "tokens_in": 566, "tokens_out": 75, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:49.712+00:00", "status": "answered", "http_status": 200, "question": "Which place in the region is normally open during the winter?", "answer": "Marchwood is the one place in the region that works in winter, as almost everything is indoors and nothing closes seasonally (*guide_marchwood.md*). Thornby_wells is also described as a reliable winter destination (*guide_thornby_wells.md*).", "refused": false, "best_distance": 0.4761, "threshold": 0.65, "sources": ["guide_corry_vale.md", "guide_givens_mill.md", "guide_halden_bay.md", "guide_marchwood.md", "guide_seasons.md", "guide_thornby_wells.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 619.6, "error": null, "tokens_in": 601, "tokens_out": 55, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:50.316+00:00", "status": "answered", "http_status": 200, "question": "When do the pubs serve food in Kestrelford?", "answer": "In Kestrelford, the pubs serve food between 12 and 2 and again between 6 and 8:30 (as mentioned in *guide_kestrelford.md* and *guide_eating.md*).", "refused": false, "best_distance": 0.2852, "threshold": 0.65, "sources": ["guide_corry_vale.md", "guide_eating.md", "guide_elder_ness.md", "guide_givens_mill.md", "guide_kestrelford.md"], "corpus": "city_guides", "top_k": 6, "duration_ms": 588.3, "error": null, "tokens_in": 660, "tokens_out": 49, "model_calls": 1, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:50.360+00:00", "status": "refused", "http_status": 200, "question": "What is the capital of Mongolia?", "answer": "I don't have enough information about that.", "refused": true, "best_distance": 0.7981, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 23.9, "error": null, "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:50.383+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.1, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
{"timestamp": "2026-11-14T01:52:50.385+00:00", "status": "bad_request", "http_status": 400, "question": "", "answer": null, "refused": null, "best_distance": null, "threshold": 0.65, "sources": [], "corpus": "city_guides", "top_k": 6, "duration_ms": 0.0, "error": "Send JSON with a question in it, like {\"question\": \"Which region is mostly open during winter?\"}", "tokens_in": 0, "tokens_out": 0, "model_calls": 0, "cache_hit": false}
```

**Diagnoses**

*Criterion 2: Multi-answer questions (MISSED, 1/2 each run)*

- **What happened:** There are 3 towns that work well during the winter, and in one run only one town was named as difficult to walk in, but there are two. 
- **Stage:** The stage for this would be generation as the model could have just forgotten to include those answers. 
- **How I know & Mechanism:** The used files in these runs had the answers in them and other answers from other runs also had the correct answers. This means the model just did not include those answers in the response.

*Criterion 3: Token cost (MISSED, 7/8 in Run 1)*

- **What happened:** One of the answers had a very long paragraph as the answer which cause a lot of output tokens to be used.
- **Stage:** Model generating controls this number
- **How I know:** I know this is the problem because in the log, it says that 118 tokens were used which directly points to the model using that many tokens.
- **Mechanism:** The answer was too long because the model was answering a question that had multiple answers and it was trying to give multiple answers. 

There is a propmting pattern where propmting needs to be changed to answer multiple questions but also try to also limit how much is said on top of answering the questions. 

**What I changed**
I chnaged the grounding prompt for the AI model to specifically include the all the answers in its output and widen the sentance limit for that. Otherwise keep all response around one sentance. 

**Results -After**

| Criterion | Target | Run 4 | Run 5 | Run 6 | Verdict |
|---|---|---|---|---|---|
| 1. First answered request after a restart is under 3000 ms | 3 of 3 | 1,795 ms | 1,745 ms | 1,815 ms | MET |
| 2. Multi-answer questions have all answers correct | 2 of 2 each run | 0/2 | 0/2 | 1/2 | MISSED |
| 3. Every request ≤ 700 tokens in and ≤ 100 tokens out | 8 of 8 each run | 8/8 | 8/8 | 8/8 | MET |
| 4. Empty or missing question returns 400 and is logged | 2 of 2 each run | 2/2 | 2/2 | 2/2 | MET |
| 5. Every request is logged with timestamp, HTTP code and status | 8 of 8 each run | 8/8 | 8/8 | 8/8 | MET |

**Did it help?**
It helped with the token usage by bringing output tokens down, but now the model answers multiple answer questions slightly worse. Mainly because these two criteria are affected by each other. The increase to the grounding rules also increased the amount of input tokens by 31 tokens.

**How I Used AI**

<!-- Two or three specific moments. For each: what you asked for, what came back,
     and what you changed or decided yourself. -->

**1.**
I asked claude for help with creating the logging on this system
It gave me logging code and I ended up changing how the logging would appear in the logs

**2.**
I asked claude for help with propmting the AI model
It gave me prompt add ons for grounding and I did not change anything since I had already tried other propmts beforehand

**Whats still broken**
Criterion 2 is still broken because Corry Vale is not being given as one of the two answers to which cities are not walkable. If I had the time to fix this, I would try to find a way to word the prompt so that the AI model will send all the answers and not go over the token limit for outputs. I would try this because if I could find the best wording, I could possibly get both criterions to work together instead of against each other 

**Why I stopped**
I stopped here because I tried multiple different prompts that cause criterion 2 to fail, so I found this as a good stopping place.



