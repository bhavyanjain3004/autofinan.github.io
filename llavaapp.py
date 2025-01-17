from openai import OpenAI
import streamlit as st


client = OpenAI(api_key="jhjhjh1234", base_url="http://localhost:8000/v1")


st.title("OpenAI Server App (...llama cpp)")
image_url = st.text_input("Put image URL")
prompt = st.chat_input("Pass your prompt here")


if prompt:
    st.chat_message("user").markdown(prompt)

    
    response = client.chat.completions.create(
        model="mistral-function-calling",
        messages=[{"role": "user", "content": 
                   [{
                       'type': 'image_url',
                       'image_url': image_url
                   },
                   {
                       'type': 'type',
                       'text':prompt
                   }
                   ]
                }],
         stream=True,
        
    )
    with st.chat_message("ai"):
        completed_message = ""
        message = st.empty()
      
        for chunk in response:
        
             if chunk.choices[0].delta.content is not None:
                 completed_message += chunk.choices[0].delta.content
                 message.markdown(completed_message)