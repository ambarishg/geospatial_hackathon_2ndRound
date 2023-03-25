import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import re
import string
import os
import openai
import spacy
from geopy.geocoders import Nominatim


key = ''
location = ''
endpoint = ''

openai.api_type = "azure"
openai.api_key = key
openai.api_base = endpoint
openai.api_version = "2022-12-01"
deployment_id=''

filename = "data/ne_embeddings.pkl"

def create_prompt(context,query):
    header = "Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry Not Sufficient context to answer query' \n"
    return header + context + "\n\n" + query + "\n"

def generate_answer(prompt):
    response = openai.Completion.create(
    engine=deployment_id,
    prompt=prompt,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop = [' END']
    )
    return (response.choices[0].text).strip()

st.header("Geographical Text Analysis Question and Answering System")

user_input = st.text_area("Your Question",
"What are the geographical features in North East?")

result = st.button("Make recommendations")

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

@st.cache(allow_output_mutation=True)
def get_embeddings():
    with open(filename, 'rb') as f:
        df_embeddings = pickle.load(f)
    return df_embeddings

if result:
    df_embeddings = get_embeddings()
    pole_data = df_embeddings["embeddings"].tolist()
    q_new = user_input
    q_new = [model.encode(q_new)]
    result = cosine_similarity(q_new,pole_data)
    result_df = pd.DataFrame(result[0], columns = ['sim'])
    df = pd.DataFrame(df_embeddings["text"].tolist(),columns = ["text"])
    q = pd.concat([df,result_df],axis = 1)
    q = q.sort_values(by="sim",ascending = False)

    q_n = q[:50]
    q_n = q_n[["text"]]
    context= "\n\n".join(q_n["text"])
    
    prompt = create_prompt(context,user_input)
    reply = generate_answer(prompt)
    st.write(reply)

    geo_list = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(reply)
    for ent in doc.ents:
        if ent.label_ in ["GPE","LOC"]:
            geo_list.append(ent.text)
    
    st.subheader("Geographical Features:")
    geolocator = Nominatim(user_agent="A")
    for loc in geo_list: 
        location = geolocator.geocode(loc)
        if location is not None:
            st.write(location.address,
                     location.latitude,
                     location.longitude)