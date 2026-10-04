# Opus 5.5 run for the open system review: launch args for the parent (CloudAgent)

The executor subagent that built this pack has no CloudAgent tool, and the box has no Anthropic key (the local `agent` CLI is Grok). This follows the same route as `/workspace/training-ep01/plan-2026-10-03/OPUS55-LAUNCH-ARGS.md`. The paid routes (the ElevenLabs Flows LLM node, Descript Underlord) were NOT used and should not be.

action: launch
model: claude-opus-5-5
model_params: {effort: high}
files:
  - url: file:///workspace/biblical-manhood/studio/podcast-show/research/opus55/opus55-pack.tar.gz
prompt: |
  Unpack opus55-pack.tar.gz. Read BRIEF.md first, then every file under evidence/ (including evidence/hosts/)
  and scripts/. Follow the writing rules in BRIEF.md and evidence/UNSLOP.md for everything you write.
  Do sections 1-7 from the brief in order. Section 2 (the E001 open) matters most, because an audio
  re-record waits on it. Section 7 is a real self-critique followed by revised versions.
  Do not generate any media, call any paid API, or sign up for anything.
  Write the complete answer as one Markdown file named opus55-review.md and return it as the artifact.
  Work at expert level and take the time you need.

## After it lands
1. Save the raw answer, unedited, to `research/opus55/opus55-review.md`. Put a header line on top giving the model, the effort and the time it landed (CT). Never substitute or paraphrase it, and never write a stand-in if the run fails. Report the failure instead.
2. Diff its E001 open against `_build/intros_data.py` entry 1 and bring any change to Aaron before the E001 re-record.
3. Apply accepted line edits in `_build/intros_data.py` only, then run `python3 _build/intro_lint.py`, `python3 _build/intro.py scripts/E0*.md`, `_build/lint.sh` and the timing check (E020 at 16:00 or under).
4. The E081-E104 opens can go into `_build/intros_data.py` as entries at any time. intro.py only touches the scripts it is given, and intro_lint.py checks every entry.
