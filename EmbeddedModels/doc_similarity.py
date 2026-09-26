from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embedding= GoogleGenerativeAIEmbeddings(
     model = 'gemini-embedding-2' 
)

documents = [
    "Lionel Messi is known for his dribbling and playmaking.",
    "Cristiano Ronaldo is known for his goalscoring and athleticism.",
    "Kylian Mbappe is known for his speed and finishing.",
    "Neymar is known for his skills and creativity."
]
doc_embedding = embedding.embed_documents(documents)
query = embedding.embed_query(' tell me about Lionel Messi')

score = cosine_similarity([query], doc_embedding)

index , score = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]
print(documents[index])