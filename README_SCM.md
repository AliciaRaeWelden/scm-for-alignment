# 🧠 Self-Consistent Semantic Meaning (SCM)

**A New Geometric Framework for Language Understanding**

---

## 📍 Overview

This repository contains a prototype implementation and interactive demo of **Self-Consistent Semantic Meaning (SCM)** — a novel approach to sentence understanding that replaces black-box attention with a transparent, iterative process.

SCM models meaning not as a fixed output from a deep transformer, but as a **convergent geometric process**, inspired by **self-consistent field (SCF) methods** in quantum chemistry.

It offers:
- 🔁 Iterative refinement of meaning representations
- 🌀 A shared **semantic centroid** that evolves dynamically
- 🔬 Visual insight into how token-level meaning stabilizes — or fails to
- ⚠️ A potential diagnostic for inference-time instability in LLMs

---

## 💡 Why SCM?

> *How do we know what a language model “means” — and when that meaning might drift?*

Transformers use deeply stacked attention and MLPs, making it difficult to interpret internal state. Small changes to inputs can lead to **non-local, unpredictable outputs** — a problem for real-time alignment and safe deployment.

SCM proposes a simple, transparent alternative:
- Every token is **pulled toward a shared representation**, iteratively.
- The system converges when all tokens agree with a **semantic centroid**.
- This makes it possible to **observe the trajectory** of meaning formation.

---

## 🧪 What's in this Demo?

- ✅ A working prototype of SCM inference on simple English sentences
- 📈 Visualizations of token paths through semantic space
- 🧭 Comparisons with BERT embeddings on:
  - Literal statements
  - Ambiguous language
  - Metaphors and emotional content

---

## 👩‍🏫 For Researchers New to AI

You don't need to know how transformers work to understand SCM.

Here's the basic idea:

1. **Start with token embeddings**: Each word is represented as a vector in high-dimensional space.
2. **Define a prototype concept space**: For example, a vector that represents "sports" or "emotion".
3. **Iteratively update each token** so that it aligns better with the group meaning.
4. **Watch the whole sentence converge** to a shared understanding — or not.

You can think of this like **group consensus** forming over time. Each token “votes” and adjusts its position in meaning-space until everyone agrees.

---

## 🎯 Why It Matters

🔍 **Interpretability**  
SCM produces step-by-step trajectories of semantic convergence. This could help us detect when a model is:
- Misinterpreting metaphors
- Exhibiting alignment drift
- Failing to resolve ambiguity

🛡️ **Inference-Time Safety**  
Because SCM is iterative, we can pause, intervene, or inspect at any step — something that’s extremely hard with a transformer.

🧪 **Complement to Existing LLMs**  
SCM is not a replacement, but a complementary lens. Comparing its stable centroid to a transformer output may reveal *where meaning diverges.*

---

## 🛠️ Running the Demo

If you're using this via Hugging Face Spaces, just scroll down and interact with the input boxes.

To run locally:

```bash
git clone https://github.com/AliciaRaeWelden/scm-for-alignment
cd scm-for-alignment
pip install -r requirements.txt
streamlit run app.py
```

---

## 📚 Learn More

- [SCF Methods in Quantum Chemistry](https://en.wikipedia.org/wiki/Self-consistent_field)
- [Transformer Interpretability Challenges](https://arxiv.org/abs/2010.10596)
- [Why Inference-Time Safety Matters](https://www.alignmentforum.org/posts/...)

---
