from sentence_transformers import SentenceTransformer, util

# Load a pretrained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

user_instruction = "Summarize the risks of inference-time compute"

initial_context = [
    "Inference-time compute can lead to unpredictable model behavior.",
    "There are concerns about malicious prompt injections at inference time.",
    "Dynamic model behavior during inference poses a risk for alignment."
]

candidate_outputs = [
    "Inference-time alignment risks include context drift.",
    "Compute budgets are important for training efficiency.",
    "Models can be hacked with clever prompts during inference.",
    "Training datasets should be balanced for fairness.",
    "Inference-time compute can trigger latent unsafe behaviors."
]

instruction_embedding = model.encode(user_instruction, convert_to_tensor=True)
context_embeddings = model.encode(initial_context, convert_to_tensor=True)

semantic_centroid = (instruction_embedding + context_embeddings.mean(dim=0)) / 2

candidate_embeddings = model.encode(candidate_outputs, convert_to_tensor=True)
cosine_scores = util.cos_sim(candidate_embeddings, semantic_centroid)

threshold = 0.4
print(f"\nCandidate outputs aligned with meaning vector (threshold={threshold}):\n")
for i, score in enumerate(cosine_scores):
    if score >= threshold:
        print(f"✓ {candidate_outputs[i]}  [Score: {score.item():.3f}]")
    else:
        print(f"✗ {candidate_outputs[i]}  [Score: {score.item():.3f}]")
