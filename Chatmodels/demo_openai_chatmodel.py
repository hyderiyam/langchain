from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='claude-opus-5-5',temperature=0.3,max_completion_tokens=15)

result = model.invoke('who is jinnah')
print(result.content)