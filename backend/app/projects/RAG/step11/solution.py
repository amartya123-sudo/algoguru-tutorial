from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

index = VectorStoreIndex.from_documents(
    documents,
)

retriever = index.as_retriever(
    similarity_top_k=2,
)

results = retriever.retrieve(
    "What is Python?"
)

print(results)