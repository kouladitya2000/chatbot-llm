import os
from secret_key import openapi_key
import openai
from langchain.chat_models import AzureChatOpenAI
os.environ['OPENAI_API_KEY'] = openapi_key
os.environ['OPENAI_API_BASE']="https://htioaiservice.openai.azure.com/"
os.environ['OPENAI_API_VERSION']="2023-5-15"


from langchain.llms import OpenAI
llm= AzureChatOpenAI(temperature=1,
)
openai.api_type = "azure"
openai.api_base = "https://htioaiservice.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="restaurant",
  prompt="please generate 2 Chinese restaurant name and 10 cusine names ",
  temperature=1,
  max_tokens=100,
  top_p=0.5,
  frequency_penalty=0,
  presence_penalty=0,
  best_of=1,
  stop=None)


print(response.choices[0].text.strip())
