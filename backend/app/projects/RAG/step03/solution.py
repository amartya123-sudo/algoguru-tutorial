from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

first_document = documents[0]

print(first_document.text)
print(first_document.metadata)