from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from dotenv import load_dotenv
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm= HuggingFacePipeline.from_model_id(
model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
task='text-generation',

)

model=ChatHuggingFace(
    llm=llm
)

results =model.invoke('who is mola ali')
print(results.content)


