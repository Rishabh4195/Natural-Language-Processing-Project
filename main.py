import json
import pickle
import time
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie, st_lottie_spinner  # pip install streamlit-lottie

global Lrdetect_Model

# Loading Image using PIL
im = Image.open("E:/Extra/hutti photos/Camera/IMG_20220203_173551.jpg")
# Adding Image to web app
st.set_page_config(page_title="Hotel Review", page_icon=im)


def load_lottiefile(filepath: "C:/Users/Rishb/PycharmProjects/Hotel Review/hotelicon.json"):
    with open(filepath, "r") as f:
        return json.load(f)


lottie_coding = load_lottiefile("C:/Users/Rishb/PycharmProjects/Hotel Review/hotelicon.json")
# for main widgets

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",  # medium ; high
    height=100,
    width=650,
    key=None)

LrdetectFile = open('model.pkl', 'rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Hotel Review Prediction")
# st.subheader('')
# input_test = st.text_input("", "")
input_test = st.text_input("Welcome in review detection app, Write Your Reviews in a Box And click on Results", "")

button_clicked = st.button("Results")
if button_clicked:
    prediction = st.text(Lrdetect_Model.predict([input_test]))
    lottie_thanks = load_lottiefile("C:/Users/Rishb/PycharmProjects/Hotel Review/thank-you-animaiton.json")
    with st_lottie_spinner(lottie_thanks, height=150, width=150):
        time.sleep(3)
    st.balloons()

# def load_lottiefile(filepath: "C:/Users/Rishb/PycharmProjects/Hotel Review/success.json"):
# with open(filepath, "r") as f:
# return json.load(f)


# lottie_coding1 = load_lottiefile("C:/Users/Rishb/PycharmProjects/Hotel Review/success.json")
# for second widget

# st_lottie(lottie_coding1, speed=1, reverse=False, loop=True, quality="low", height=100, width=100, key=None)
# quality="low",  # medium ; high(quality will be change as per our requirement)

# lottie_thanks = load_lottiefile("C:/Users/Rishb/PycharmProjects/Hotel Review/thank-you-animaiton.json")
# for third widget

# if st.button("Press It"):
# with st_lottie_spinner(lottie_thanks, height=500, width=650):
# time.sleep(3)
# st.balloons()
