

    ✅ "Inference-time alignment risks include context drift."
        ❌ "Training datasets should be balanced for fairness."

Each candidate is embedded and scored for cosine similarity with the centroid. This measures how semantically "close" they are to the evolving task meaning.

Step 3: Filter Based on Alignment
---------------------------------

We set a threshold (e.g., 0.4) and only keep outputs above that value. This ensures that reasoning chains, completions, or memory retrievals don't drift off-topic.

Example result:

    ✓ Inference-time alignment risks include context drift.        [Score: 0.65]
        ✓ Models can be hacked with clever prompts during inference.  [Score: 0.62]
	    ✗ Training datasets should be balanced for fairness.           [Score: 0.23]
	        ✗ Compute budgets are important for training efficiency.       [Score: 0.29]
		    ✓ Inference-time compute can trigger latent unsafe behaviors.  [Score: 0.58]

Why This Matters for Alignment
------------------------------

- SCM provides a lightweight, inference-time alignment filter
- It doesn’t require fine-tuning or RLHF — just embeddings + cosine similarity
- It offers semantic guardrails against hallucination, drift, or topic injection
- It's architecture-agnostic and can be used alongside agents, RAG, CoT, or tool-using systems

Try It Yourself
---------------

To run the demo:

    python scm_demo/meaning_vector_demo.py

You’ll need:

- Python 3.8+
- The sentence-transformers library:

    pip install sentence-transformers

Contributing
------------

Want to improve SCM or try it in other workflows?
Create a new demo folder (e.g. `scm_demo/scm_for_rag/`) or open a GitHub Issue with suggestions, bugs, or results from your own experiments.

License
-------

MIT License. Released as public prior art and open research.
~