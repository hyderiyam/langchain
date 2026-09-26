from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

# Documents
documents = [
    "ali is tall boy",
    "he is the impo guy",
    "who are you"
]

res = embedding.embed_documents(documents)

result = embedding.embed_query(
    "ali is tall boy"
)

print("Query Embedding:")
print(result)

print("\nDocument Embeddings:")
print(res)