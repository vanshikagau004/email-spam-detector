import streamlit as st
import pickle

st.title("Email Spam Detector")

st.write("Enter a message to check if it is Spam or Not Spam.")

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

message = st.text_area("Enter your message")

if st.button("Predict"):

    if message != "":
        vector = vectorizer.transform([message])
        result = model.predict(vector)

        if result[0] == 1:
            st.error("This message is SPAM")
        else:
            st.success("This message is NOT SPAM")

    else:

        st.warning("Please enter a message")
