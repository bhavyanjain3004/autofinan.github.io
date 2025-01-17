from openai import OpenAI
import streamlit as st
import instructor
from pydantic import BaseModel
from stock_data import get_stock_prices


client = OpenAI(api_key="jhjhjh1234", base_url="http://localhost:8000/v1")
client = instructor.patch(client=client)

class ResponseModel(BaseModel):
    ticker: str
    days: int

st.title(" OpenAI Server App (...llama cpp)")
prompt = st.chat_input("Pass your prompt here")

if prompt:
    st.chat_message("user").markdown(prompt)

    response = client.chat.completions.create(
        model="mistral-function-calling",
        messages=[{"role": "user", "content": prompt}],
        
        response_model=ResponseModel,
    )

    st.chat_message("ai").markdown(response)

    try:
        prices = get_stock_prices(response.ticker, response.days)
        st.chat_message("ai").markdown(prices)
        fullresponse = client.chat.completions.create(
            model="mixtral",
            messages=[{"role": "user", "content": prompt + "\n" + str(prices)}],
            stream=True,
        )

        with st.chat_message("ai"):
            completed_message = ""
            message = st.empty()
            for chunk in fullresponse:
                if chunk.choices[0].delta.content is not None:
                    completed_message += chunk.choices[0].delta.content
                    message.markdown(completed_message)
    except Exception as e:
        st.chat_message("ai").markdown("Something went wrong 😭")

