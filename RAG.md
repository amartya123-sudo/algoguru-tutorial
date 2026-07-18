# Retrieval-Augmented Generation (RAG) with LlamaIndex, HuggingFace & Ollama

---

## Step 1 — Load Documents

### Goal
Load every file from a `data` folder into memory as document objects.

### Concept
Before you can search or generate anything, you need data. LlamaIndex provides `SimpleDirectoryReader`, which reads every supported file in a directory (`.txt`, `.pdf`, `.md`, and more) and turns each one into a **Document** object.

### Walkthrough
```python
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader(
    input_dir="data",
).load_data()

print(documents)
```
- `SimpleDirectoryReader(input_dir="data")` — points the reader at your data folder.
- `.load_data()` — actually reads the files and returns a list of `Document` objects.

### Try It Yourself
Starter template:
```python
# Load all documents from the "data" directory using
# SimpleDirectoryReader.

# Store the loaded documents in a variable named documents.

# Print the loaded documents.
```
Import `SimpleDirectoryReader`, load the documents, store them in a variable named exactly `documents`, and print them.

### Checkpoint
You should see a printed list of `Document(...)` objects — one per file in your `data` folder.

### Common Mistakes
- Pointing `input_dir` at a folder that doesn't exist or is empty — you'll get zero documents.
- Naming the variable something other than `documents` — later steps (and the validator) expect this exact name.

---

## Step 2 — Count the Loaded Documents

### Goal
Check how many documents were actually loaded.

### Concept
Before building anything on top of your data, it's good practice to sanity-check its scale — just like checking `len(dataset)` in a computer vision project.

### Walkthrough
```python
documents = SimpleDirectoryReader(input_dir="data").load_data()

print(len(documents))
```

### Try It Yourself
Starter template:
```python
# Load all documents from the "data" directory.

# Store them in a variable named documents.

# Print the total number of loaded documents.
```

### Checkpoint
You should see a single integer printed — the number of files loaded from `data`.

### Common Mistakes
- Printing `documents` instead of `len(documents)` — you want the *count*, not the full contents, at this step.

---

## Step 3 — Inspect a Document's Text and Metadata

### Goal
Look inside a single document to see what it actually contains.

### Concept
Every `Document` object has two important parts:
- **`.text`** — the raw text content.
- **`.metadata`** — extra info about the document, like its file name.

### Walkthrough
```python
documents = SimpleDirectoryReader(input_dir="data").load_data()

first_document = documents[0]

print(first_document.text)
print(first_document.metadata)
```

### Math Corner
No formulas here, but an important structural idea: think of each document as a pair **(text, metadata)**. Every later step in this tutorial — chunking, embedding, retrieving — operates on the `.text` part, while the `.metadata` quietly travels along for the ride, ready to be used for citing sources later.

### Try It Yourself
Starter template:
```python
# Load all documents from the "data" directory.

# Store them in a variable named documents.

# Create a variable named first_document
# containing the first loaded document.

# Print the document text.

# Print the document metadata.
```

### Checkpoint
You should see the raw text of your first file printed, followed by a small dictionary of metadata (e.g., file name, file path).

### Common Mistakes
- Using `documents[1]` instead of `documents[0]` — Python indexing starts at 0, so "the first document" is index `0`.

---

## Step 4 — Split Documents into Chunks (Nodes)

### Goal
Break large documents into smaller, searchable pieces called **nodes**.

### Concept
Whole documents are often too long to search or feed to a language model efficiently. Instead, RAG systems split them into smaller overlapping chunks, using a `SentenceSplitter`.

### Walkthrough
```python
from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(
    chunk_size=200,
    chunk_overlap=20,
)

nodes = splitter.get_nodes_from_documents(documents)

print(len(nodes))
```

### Math Corner
Picture the splitter as a sliding window moving across your document's tokens. Two settings control it:
- **`chunk_size = 200`** — how many tokens go into each chunk.
- **`chunk_overlap = 20`** — how many tokens are repeated between consecutive chunks.

The window moves forward by a **stride** each time:
```
stride = chunk_size − chunk_overlap = 200 − 20 = 180
```
So chunk 2 starts 180 tokens after chunk 1 started, but shares its first 20 tokens with chunk 1's last 20 — this overlap prevents a sentence or idea from being awkwardly cut in half at a chunk boundary. For a document of length **N** tokens, you'll get roughly:
```
number of chunks ≈ ⌈(N − chunk_overlap) / stride⌉
```
This is exactly why `len(nodes)` will usually be much bigger than `len(documents)` — one document becomes many chunks.

### Try It Yourself
Starter template:
```python
# Load all documents from the "data" directory.

# Create a SentenceSplitter with:
# - chunk_size = 200
# - chunk_overlap = 20

# Split the documents into nodes.

# Store the result in a variable named nodes.

# Print the total number of nodes.
```

### Checkpoint
You should see a number larger than your document count from Step 2 — confirming your documents were successfully broken into smaller chunks.

### Common Mistakes
- Setting `chunk_overlap` larger than `chunk_size` — this is invalid and will raise an error, since the stride would become zero or negative.
- Forgetting to reload `documents` before splitting, if working in a fresh script.

---

## Step 5 — Inspect a Node's Text and Metadata

### Goal
Look inside a single chunk (node) the same way you inspected a whole document in Step 3.

### Concept
A **node** is structurally the same kind of object as a document — it has `.text` and `.metadata` — just smaller, since it represents one chunk rather than a whole file.

### Walkthrough
```python
nodes = splitter.get_nodes_from_documents(documents)

first_node = nodes[0]

print(first_node.text)
print(first_node.metadata)
```

### Try It Yourself
Starter template:
```python
# Load the documents.

# Split the documents into nodes.

# Create a variable named first_node
# containing the first node.

# Print the node text.

# Print the node metadata.
```

### Checkpoint
You should see a chunk of text noticeably shorter than the full document from Step 3, along with metadata (which usually includes information inherited from its parent document).

### Common Mistakes
- Confusing "node" (a chunk) with "document" (a whole file) — they look similar in code but represent very different scopes of text.

---

## Step 6 — Generate an Embedding for a Node

### Goal
Convert a chunk of text into a numeric vector that captures its *meaning*.

### Concept
An **embedding model** turns text into a list of numbers (a vector) such that texts with similar meaning end up as vectors that are close together — even if they don't share any of the same words.

### Walkthrough
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
)

embedding = model.get_text_embedding(nodes[0].text)

print(embedding)
```

### Math Corner
An embedding is a function mapping text into a fixed-size numeric space:
```
embed: text → ℝ^d
```
For `BAAI/bge-small-en-v1.5`, **d = 384** — no matter how long or short your chunk of text is, you get back exactly 384 numbers. This is the core trick that makes "search by meaning" possible: two chunks discussing the same idea in completely different words will still end up as *nearby* vectors in this 384-dimensional space.

### Try It Yourself
Starter template:
```python
# Load the documents.

# Split the documents into nodes.

# Create a HuggingFaceEmbedding model using:
# "BAAI/bge-small-en-v1.5"

# Generate an embedding for the first node.

# Store it in a variable named embedding.

# Print the embedding.
```

### Checkpoint
You should see a printed list of 384 floating-point numbers.

### Common Mistakes
- The first run downloads the embedding model — expect a short delay and make sure you have an internet connection the first time.
- Passing a `Document` or `Node` object directly to `get_text_embedding()` instead of its `.text` attribute — the method expects a plain string.

---

## Step 7 — Measure Similarity Between Two Embeddings

### Goal
Quantify how similar two pieces of text are, using their embeddings.

### Concept
Once text is turned into vectors, you need a way to measure "closeness." The standard tool is **cosine similarity** — it measures the angle between two vectors, ignoring their length.

### Walkthrough
```python
from sklearn.metrics.pairwise import cosine_similarity

query = "What is Python?"

query_embedding = model.get_text_embedding(query)
document_embedding = model.get_text_embedding("Python is a programming language.")

score = cosine_similarity([query_embedding], [document_embedding])[0][0]

print(score)
```

### Math Corner
```
cos_sim(A, B) = (A · B) / (‖A‖ · ‖B‖)
```
where `A · B` is the dot product (multiply matching elements, then sum them) and `‖A‖`, `‖B‖` are each vector's length. The result always falls between:
- **1** → the two texts mean almost the same thing
- **0** → the two texts are unrelated
- **−1** → the two texts are "opposite" in meaning (rare in practice for normal text)

This one formula is the engine behind nearly everything that follows in this tutorial — semantic search (Steps 8–9), retrieval (Step 11), and beyond.

### Try It Yourself
Starter template:
```python
# Create a HuggingFaceEmbedding model using
# "BAAI/bge-small-en-v1.5".

# Create a variable named query.

# Generate an embedding for the query.

# Generate an embedding for the sentence:
# "Python is a programming language."

# Compute the cosine similarity between
# the two embeddings.

# Store the result in a variable named score.

# Print the similarity score.
```

### Checkpoint
You should see a decimal number close to 1 (since the query and sentence are closely related in meaning).

### Common Mistakes
- Forgetting the double brackets: `cosine_similarity([query_embedding], [document_embedding])` — scikit-learn expects a *list of vectors* on each side, not a single vector.

---

## Step 8 — Build a Simple Vector Store

### Goal
Combine chunking and embedding into a small, hand-built database of searchable records.

### Concept
A **vector store** is just a collection of records, where each record holds a chunk's text, its embedding, and its metadata — everything needed to search it later.

### Walkthrough
```python
vector_store = []

for node in nodes:
    vector_store.append({
        "text": node.text,
        "embedding": model.get_text_embedding(node.text),
        "metadata": node.metadata,
    })

print(len(vector_store))
```

### Math Corner
There's no new formula here, but an important conceptual one: this loop applies the embedding function from Step 6 (`embed: text → ℝ^384`) to *every single node*, not just one. The result is effectively a table:

| text | embedding (384 numbers) | metadata |
|---|---|---|
| chunk 1 | [0.12, −0.03, ...] | {...} |
| chunk 2 | [0.05, 0.41, ...] | {...} |
| ... | ... | ... |

This is exactly what real vector databases (FAISS, Pinecone, Chroma, etc.) store under the hood — they just add speed and scale on top of this same basic idea.

### Try It Yourself
Starter template:
```python
# Load the documents.

# Split the documents into nodes.

# Create a HuggingFaceEmbedding model.

# Create an empty list named vector_store.

# For each node:
# - Generate an embedding.
# - Store the node text.
# - Store the embedding.
# - Store the node metadata.

# Print the total number of records
# in the vector store.
```

### Checkpoint
`len(vector_store)` should equal `len(nodes)` from Step 4 — one record per chunk.

### Common Mistakes
- Embedding `documents` instead of `nodes` — you want one record *per chunk*, not per whole file.
- This loop calls the embedding model once per node — for a large dataset, expect it to take a noticeable amount of time. That's normal.

---

## Step 9 — Perform Semantic Search

### Goal
Given a question, find the most relevant chunk in your vector store — by meaning, not keyword matching.

### Concept
This is the payoff of Steps 4–8: a real (if small-scale) **semantic search engine**, built entirely by hand.

### Walkthrough
```python
query = "What is Python?"
query_embedding = model.get_text_embedding(query)

best_match = max(
    vector_store,
    key=lambda record: cosine_similarity([query_embedding], [record["embedding"]])[0][0],
)

print(best_match["text"])
```

### Math Corner
This is a **brute-force nearest-neighbor search**. For your query embedding `q` and every stored chunk embedding `eᵢ`, it computes cosine similarity for *every single record*, then keeps the best one:
```
best_match = argmax_i ( cos_sim(q, eᵢ) )
```
This is the same "pick the highest score" idea (**argmax**) you'd use to decide a predicted class in an image classifier — here it picks the most relevant chunk of text instead. Note the cost: comparing against *every* record means this approach gets slower as your vector store grows (it's **O(n)**, where n is the number of chunks) — a limitation that real vector databases are specifically built to solve at scale.

### Try It Yourself
Starter template:
```python
# Load the documents.

# Split the documents into nodes.

# Create embeddings for every node and
# store them in a variable named vector_store.

# Create a variable named query.

# Generate an embedding for the query.

# Find the most similar document using
# cosine similarity.

# Store the best matching record in a
# variable named best_match.

# Print the matched text.
```

### Checkpoint
You should see the text of whichever chunk best answers "What is Python?" — even if the word "Python" doesn't appear verbatim in a chunk that's still conceptually related, semantic search can still surface it.

### Common Mistakes
- Using `min` instead of `max` — cosine similarity is a *similarity* score (higher = better), not a distance (where lower would be better).

---

## Step 10 — Build a Vector Store Index (the Easy Way)

### Goal
Replace your hand-built vector store (Steps 8–9) with LlamaIndex's built-in `VectorStoreIndex`.

### Concept
You've now built chunking, embedding, and search entirely by hand. This step reveals that a single line of LlamaIndex code does all of that automatically.

### Walkthrough
```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

documents = SimpleDirectoryReader(input_dir="data").load_data()

index = VectorStoreIndex.from_documents(documents)

print(index)
```

### Math Corner
No new formulas — but a valuable realization: `VectorStoreIndex.from_documents()` performs, internally, exactly the pipeline you built manually in Steps 4, 6, and 8 — split into nodes, embed each node, store the results. You now understand *why* this one line works, rather than treating it as a black box.

### Try It Yourself
Starter template:
```python
# Load all documents from the "data" directory.

# Create a VectorStoreIndex using the loaded documents.

# Store the index in a variable named index.

# Print the index.
```

### Checkpoint
`print(index)` should run without errors and show some representation of a `VectorStoreIndex` object.

### Common Mistakes
- Expecting `print(index)` to show readable search results — the index object itself is just the searchable structure; actual searching happens in Step 11.

---

## Step 11 — Retrieve the Top-K Most Relevant Chunks

### Goal
Use the index to fetch the most relevant chunks for a given question.

### Concept
A **retriever** wraps your index and, given a query, returns the top-scoring chunks — generalizing Step 9's "find the single best match" into "find the best *k* matches."

### Walkthrough
```python
retriever = index.as_retriever(similarity_top_k=2)

results = retriever.retrieve("What is Python?")

print(results)
```

### Math Corner
This generalizes Step 9's argmax into **top-k retrieval**:
```
top_k(q) = the k chunks eᵢ with the k largest values of cos_sim(q, eᵢ)
```
With `similarity_top_k=2`, you get back the 2 best-matching chunks instead of just 1. Choosing *k* is a real trade-off:
- Too small → you might miss relevant information spread across multiple chunks.
- Too large → you flood the eventual LLM prompt (Step 12+) with irrelevant text, wasting its limited context window and potentially confusing the answer.

### Try It Yourself
Starter template:
```python
# Load the documents.

# Create a VectorStoreIndex.

# Create a retriever that returns
# the top 2 most similar nodes.

# Retrieve the nodes for the query:
# "What is Python?"

# Store the retrieved nodes in
# a variable named results.

# Print the retrieved nodes.
```

### Checkpoint
You should see a list of exactly 2 retrieved nodes, each with a similarity score attached.

### Common Mistakes
- Setting `similarity_top_k` higher than the total number of available nodes — it will just return however many exist, without error.

---

## Step 12 — Build a Full Query Engine with a Local LLM

### Goal
Connect retrieval to an actual language model, completing your first full RAG pipeline.

### Concept
So far, you've only *found* relevant text. Now you'll let a language model *read* that text and generate a natural-language answer — the "G" (Generation) in RAG. This step uses **Ollama**, which runs language models locally on your machine.

### Walkthrough
```python
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

Settings.llm = Ollama(model="llama3.2")

documents = SimpleDirectoryReader(input_dir="data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("What is Python?")

print(response)
```

### Math Corner
No single formula here, but an important conceptual pipeline — `query_engine.query()` performs, automatically:
1. Embed the query (Step 6's math).
2. Retrieve the top-k relevant chunks (Step 11's math).
3. Insert those chunks as **context** into a prompt.
4. Let the LLM generate an answer *grounded* in that retrieved context, rather than purely from what it memorized during training.

This is the whole idea of RAG in one line: it lets a general-purpose model answer questions accurately about *your* documents — data it's never seen before — by handing it the relevant evidence at question time.

### Try It Yourself
Starter template:
```python
# Create an Ollama LLM using the "llama3.2" model.

# Assign it to Settings.llm.

# Load the documents.

# Create a VectorStoreIndex.

# Create a QueryEngine.

# Ask the question:
# "What is Python?"

# Store the response in a variable
# named response.

# Print the response.
```

### Checkpoint
You should see a coherent, natural-language answer to "What is Python?", grounded in your loaded documents. (Requires Ollama running locally with the `llama3.2` model pulled.)

### Common Mistakes
- Forgetting to have Ollama running locally (`ollama serve`) and the `llama3.2` model pulled (`ollama pull llama3.2`) before running this step — you'll get a connection error otherwise.
- Setting `Settings.llm` *after* creating the index — set it first, so the query engine knows which model to use.

---

## Step 13 — Build a Prompt Template

### Goal
Manually construct the kind of prompt that Step 12 was building automatically behind the scenes.

### Concept
A **prompt template** is text with placeholders that get filled in dynamically — here, a `{context}` placeholder for retrieved information and a `{question}` placeholder for the user's question.

### Walkthrough
```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("""
You are a helpful assistant.

Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
""")

formatted_prompt = prompt.format(
    context="Python is a programming language.",
    question="What is Python?",
)

print(formatted_prompt)
```

### Math Corner
No formulas, but an important concept: **grounding**. The instruction *"Answer the question using only the context below"* explicitly constrains the model to rely on the retrieved evidence rather than its own possibly outdated or wrong internal knowledge. This single sentence is one of the most effective tools for reducing **hallucination** — a model confidently making up an incorrect answer.

### Try It Yourself
Starter template:
```python
# Create a PromptTemplate.

# The template should include:
# - Retrieved context
# - User question
# - An instruction to answer only
#   using the provided context.

# Store it in a variable named prompt.

# Format the prompt using:
# context="Python is a programming language."
# question="What is Python?"

# Store the formatted prompt in
# a variable named formatted_prompt.

# Print the formatted prompt.
```

### Checkpoint
You should see a fully-formed block of text with the context and question inserted exactly where `{context}` and `{question}` were.

### Common Mistakes
- Misspelling a placeholder name (e.g., `{Context}` vs `{context}`) — `.format()` requires an exact match between the template's placeholders and the keyword arguments you pass in.

---

## Step 14 — Assemble the Full RAG Pipeline Manually

### Goal
Wire together retrieval (Steps 10–11) and generation (Step 13) yourself — without Step 12's automatic `query_engine` shortcut.

### Concept
This step makes visible everything that was hidden inside Step 12's one-liner: retrieve, combine, format, generate.

### Walkthrough
```python
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

index = VectorStoreIndex.from_documents(documents)
retriever = index.as_retriever(similarity_top_k=2)

question = "What is Python?"
results = retriever.retrieve(question)

context = "\n\n".join(node.text for node in results)

prompt = PromptTemplate.from_template("""
Answer the question using only
the provided context.

Context:
{context}

Question:
{question}

Answer:
""")

formatted_prompt = prompt.format(context=context, question=question)

llm = ChatOllama(model="llama3.2")
response = llm.invoke(formatted_prompt)

print(response.content)
```

### Math Corner
This step is a direct composition of everything so far:
1. **Retrieve** — top-k chunks via cosine similarity (Step 11's math).
2. **Concatenate** — join the retrieved chunks' text into one `context` string, separated by blank lines.
3. **Format** — inject `context` and `question` into the template (Step 13).
4. **Generate** — send the finished prompt to the LLM and get back `response.content`.

There's no new formula here — but there is an important realization: a "RAG pipeline" isn't a magical, monolithic thing. It's just retrieval and generation, glued together with a few lines of ordinary Python.

### Try It Yourself
Starter template:
```python
# Load the documents.

# Create a VectorStoreIndex.

# Create a retriever that returns
# the top 2 matching nodes.

# Retrieve nodes for the question:
# "What is Python?"

# Combine the retrieved node text
# into a variable named context.

# Create a PromptTemplate.

# Format the prompt using the
# retrieved context and question.

# Create a ChatOllama model.

# Invoke the model.

# Store the response in a variable
# named response.

# Print the response.
```

### Checkpoint
You should see a natural-language answer printed, produced entirely from code you assembled step by step.

### Common Mistakes
- Forgetting `.content` when printing the response — `llm.invoke()` returns a message *object*, and the actual text lives in its `.content` attribute.
- Joining retrieved chunks without any separator — using `"\n\n".join(...)` keeps chunks visually distinct for the LLM; concatenating them with no space can blur chunk boundaries.

---

## Step 15 — Add Conversational Memory

### Goal
Upgrade your RAG pipeline into something closer to a real chatbot, by remembering previous turns of the conversation.

### Concept
Every step so far handled one isolated question. Real conversations need the model to remember earlier exchanges — for example, understanding "what about its main library?" as a follow-up. This is done by tracking a running **chat history** and feeding it into the prompt.

### Walkthrough
```python
chat_history = []

question = "What is Python?"

results = retriever.retrieve(question)
context = "\n\n".join(node.text for node in results)

prompt = PromptTemplate.from_template("""
Conversation:
{history}

Context:
{context}

Question:
{question}

Answer:
""")

formatted_prompt = prompt.format(
    history="\n".join(chat_history),
    context=context,
    question=question,
)

response = llm.invoke(formatted_prompt)

chat_history.append(f"User: {question}")
chat_history.append(f"Assistant: {response.content}")

print(response.content)
```

### Math Corner
No new formulas — this step simply extends Step 13's template idea with one more placeholder, `{history}`. Conceptually, though, it completes the picture of a real RAG chatbot: it now combines
- **long-term memory** — the document corpus, searched fresh every time via retrieval, and
- **short-term memory** — the growing `chat_history` list, capturing the conversation so far,

all funneled through a single prompt sent to the LLM. Note the sequencing: `chat_history` is appended to *after* the response is generated — so the current turn's question and answer become part of the memory available for the *next* turn, not the current one.

### Try It Yourself
Starter template:
```python
# Load the documents.

# Create a VectorStoreIndex.

# Create a retriever.

# Create a ChatOllama model.

# Create an empty list named chat_history.

# Ask the question:
# "What is Python?"

# Retrieve relevant nodes.

# Combine the retrieved text into a variable
# named context.

# Create a PromptTemplate that includes:
# - Chat history
# - Retrieved context
# - Current question

# Invoke the language model.

# Append both the user's question and the
# assistant's response to chat_history.

# Print the assistant's response.
```

### Checkpoint
Run the script twice with two different (related) questions, feeding the same growing `chat_history` between calls — the second answer should reflect awareness of the first question.

### Common Mistakes
- Appending to `chat_history` *before* generating the response — this would make the model see its own not-yet-generated answer as if it had already said it.
- Letting `chat_history` grow indefinitely in a long-running app — real systems typically cap or summarize history to avoid exceeding the LLM's context window.