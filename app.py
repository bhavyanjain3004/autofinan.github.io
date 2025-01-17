from openai import OpenAI
import streamlit as st
import instructor
from pydantic import BaseModel




client = OpenAI(api_key="dhddjcnd", base_url="http://localhost:8000/v1")
client = instructor.patch(client=client)

class ResponseModel(BaseModel):
   ticker:str
   days:int

st.title("🚀 Fake OpenAI Server App (...llama cpp)")
prompt = st.chat_input("Pass your prompt here")

if prompt:
   st.chat_message("user").markdown(prompt)

response = client.chat.completions.create(
    model="models/mistral-7b-instruct-v0.1.Q4_0.gguf",
    messages=[{"role": "user","content": prompt
    }],
    #stream=True,
    response_model=ResponseModel, 
)

st.chat_message('ai').markdown(response)

#with st.chat_message('ai'):
   #completed_message = ""
   #message = st.empty()
#for chunk in response:
   #if chunk.choices[0].delta.content is not None:
      #completed_message += chunk.choices[0].delta.content
      #message.markdown(completed_message)
   #print(chunk.choices[0].delta.content, flush=True, end="")


#print(response.choices[0].message.content)