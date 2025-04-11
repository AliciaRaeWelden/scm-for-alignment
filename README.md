# Self-Consistent Meaning (SCM) for AI Alignment

## Overview

This project introduces **Self-Consistent Meaning (SCM)** as a lightweight semantic alignment mechanism for large language models. SCM is designed to operate at inference time, continuously tracking and enforcing the semantic coherence of model outputs relative to a user’s intended meaning or task objective.

By maintaining a dynamically updated "meaning vector," SCM enables models to:
- Avoid semantic drift during long reasoning chains
- Filter hallucinated or irrelevant completions
- Align multi-step responses more closely with user intent

This repo provides a conceptual overview, simple Python demo, and example flows for applying SCM to inference-time tasks.

## Why SCM?

Most alignment methods operate at the training or fine-tuning level. SCM offers a complementary, **inference-time alignment layer**, enabling:

- **Real-time output filtering or reranking** based on semantic consistency
- **Modular compatibility** with any LLM or prompting framework
- **Defense against subtle misalignment** from token-level noise, prompt hacks, or context injection

## Core Idea

1. Embed prior outputs, user intent, or instruction into a shared semantic space (e.g. via SBERT or OpenAI embeddings)
2. Track a "semantic centroid" that evolves with model context
3. Score candidate completions or retrieved content for consistency with the centroid
4. Filter or rerank based on cosine similarity or divergence threshold

## Example Use Cases

- Aligning reasoning chains in ReAct/CoT prompts
- Filtering irrelevant tool calls or subgoals
- Re-ranking completions to minimize semantic deviation from task objective
- Verifying memory retrieval in RAG pipelines

## Demo

See [`scm_demo/meaning_vector_demo.py`](scm_demo/meaning_vector_demo.py) for:
- A simple example using sentence embeddings
- Updating a semantic centroid
- Accepting/rejecting outputs based on alignment score

## Future Work

- Extend to structured plans or tool-use chains
- Integrate with LLM APIs for live alignment feedback
- Evaluate SCM as a guardrail in LLM-based agents

## License

MIT License – This idea is released as **public prior art** and open research.
