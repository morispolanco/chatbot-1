import streamlit as st
import requests

st.title("Chatbot")

st.sidebar.title("NLP Bot")
st.sidebar.markdown('This is a nlp chatbot that uses blenderbot at its backend made by me for all the lonely folk out there.')


API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text 

user_input = get_text()

generated = []
past = []

if user_input:
    output = query({
        "inputs": {
            "past_user_inputs": past,
            "generated_responses": generated,
            "text": user_input,
        },"parameters": {"repetition_penalty": 1.33},
    })

    past.append(user_input)
    generated.append(output["generated_text"])


    st.text_area("Bot:", value=output['generated_text'], height=200, max_chars=None, key=None)

