from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

splitter = SentenceSplitter(
    chunk_size=200,
    chunk_overlap=20,
)

nodes = splitter.get_nodes_from_documents(
    documents,
)

model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
)

vector_store = []

for node in nodes:

    vector_store.append(
        {
            "text": node.text,
            "embedding": model.get_text_embedding(
                node.text,
            ),
            "metadata": node.metadata,
        }
    )

print(len(vector_store))