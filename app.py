import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
st.markdown("""
<style>
.css-1rs6os.edgvbvh3{
visibility : hidden;

}
</style>
""",unsafe_allow_html=True)

st.markdown("""
<style>
.css-cio0dv.egzxvld1{
visibility : hidden;

}
</style>
""",unsafe_allow_html=True)



def predict(text):
    c = model.predict(text)
    int(c)

    return c

def main():
    st.title("Spam Text Classification")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Text Classification Wed App </h2>
    <p style="color:white;text-align:center;">Powerd By:Sanket Suryavanshi</p>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('spam.jpeg')

    text = st.text_input("Text "," ")
    if (text):
        pass
    else:
        st.text('Please Enter text')


    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your Text is not Spam</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your Text is Spam</h2>
       </div>
    """

    if st.button("Predict"):
        l = []
        l.append(text)
        output=predict(l)
        

        if output == 1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()