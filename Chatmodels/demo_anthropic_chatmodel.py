from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='gpt-4',temperature=0.3,max_completion_tokens=15)

result = model.invoke('who is jinnah')
print(result.content)