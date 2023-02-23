import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st
import pickle

df = pd.read_csv('spam.csv',encoding="ISO-8859-1")

df ['spam'] = df['v1'].apply(lambda x: 1 if x =='spam' else 0)
df = df.drop('Unnamed: 2',axis=1)
df = df.drop('Unnamed: 3',axis=1)
df = df.drop('Unnamed: 4',axis=1)
x_train,x_test,y_train,y_test = train_test_split(df.v2,df.spam,test_size=0.2)


sentiment_model = Pipeline(
    steps=[
        (
            "count_verctorizer",CountVectorizer(stop_words='english', lowercase=True)
        ),
        (
            "naive_bayes", MultinomialNB()
       )
])


sentiment_model.fit(list(x_train),list(y_train))
y_pred = sentiment_model.predict(list(x_test))
pickle.dump(sentiment_model,open('model.pkl','wb'))
