from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

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

print(len(nodes))