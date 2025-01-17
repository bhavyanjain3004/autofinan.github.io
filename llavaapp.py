from openai import OpenAI

# Streamlit the app framework
import streamlit as st

# Create a client
client = OpenAI(api_key="jhjhjh1234", base_url="http://localhost:8000/v1")

# The title of the app
st.title("🚀 Fake OpenAI Server App (...llama cpp)")
image_url = st.text_input("Put image URL")
prompt = st.chat_input("Pass your prompt here")

# If the user types a prompt and hits enter
if prompt:
    st.chat_message("user").markdown(prompt)

    # Function calling LLM call
    response = client.chat.completions.create(
        # which model we want to use
        model="mistral-function-calling",
        # pass through our prompt
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
        # Add stream
         stream=True,
        
    )
    with st.chat_message("ai"):
        completed_message = ""
        message = st.empty()
       # Streaming the response out
        for chunk in response:
         # If the value is not none print it out
             if chunk.choices[0].delta.content is not None:
                 completed_message += chunk.choices[0].delta.content
                 message.markdown(completed_message)
             # print(chunk.choices[0].delta.content, flush=True, end="")

# Print it out
# print(response.choices[0].message.content)