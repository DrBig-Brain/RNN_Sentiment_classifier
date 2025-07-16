import streamlit as st
import pickle 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.models import load_model
try:
    model = load_model('model.keras')
    with open('tokenizer.pkl','rb') as file:
        tokenizer=pickle.load(file)

    st.title("RNN Sentiment Predictor")
    sentimets=['Negative','Positive']

    text = st.text_area("enter the movie review to classify",height=300)
    if text !=None:
        text_stripped=text.strip()
        tokenized_text=tokenizer.texts_to_sequences([text_stripped])
        padded_sequence = pad_sequences(tokenized_text,maxlen=236,padding='post')
        if st.button('Predict'):
            pred = model.predict(padded_sequence)
            if pred>=0.5:
                index=1
            else:
                index=0
            st.success(f'Sentiment: {sentimets[index]}')
except:
    st.text('model failed to load, try rerunning the application')
