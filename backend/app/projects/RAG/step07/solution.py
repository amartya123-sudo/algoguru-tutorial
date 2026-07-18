from sklearn.metrics.pairwise import cosine_similarity
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
)

query = "What is Python?"

query_embedding = model.get_text_embedding(
    query,
)

document_embedding = model.get_text_embedding(
    "Python is a programming language.",
)

score = cosine_similarity([query_embedding], [document_embedding])[0][0]

print(score)