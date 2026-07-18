from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)

from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

Settings.llm = Ollama(
    model="llama3.2",
)

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

index = VectorStoreIndex.from_documents(
    documents,
)

query_engine = index.as_query_engine()

response = query_engine.query(
    "What is Python?"
)

print(response)