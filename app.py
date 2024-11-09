import streamlit as st
from PIL import Image

img =Image.open("con1.jpg")
st.sidebar.image(img.resize((200,300)))
curr=["Naira","Pounds","Dollar","Euro","Yen","Cedi"]
conv=[1,2000,1750,1800,120,75]

def convert(num,initial,final):
    ini_id =curr.index(initial)
    fin_id =curr.index(final)

    valve1 =conv[ini_id]
    valve2 =conv[fin_id]

    result = num *  valve1 / valve2
    return round(result,2)

num = st.number_input("How much are you converting")
initial = st.selectbox("what is your initial currency?",curr)
final =st.selectbox("what currency are you converting to?",curr)

amount = convert(num,initial,final)

if st.button("convert"):
    st.write(amount)


                       
                       
            


