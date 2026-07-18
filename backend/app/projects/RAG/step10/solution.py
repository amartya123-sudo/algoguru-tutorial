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

print(index)