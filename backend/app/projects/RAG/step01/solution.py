from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

print(documents)