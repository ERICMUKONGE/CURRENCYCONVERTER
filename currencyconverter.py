import streamlit as st
import requests
import api

st.markdown('<iframe src="https://embed.lottiefiles.com/animation/51720"></iframe>',unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    curr1 = st.selectbox('Currency 1',['EUR','USD','GBP'])
with col2:  
    if curr1 == 'EUR':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/103126"></iframe>',unsafe_allow_html=True)
    elif curr1 == 'USD':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/44076"></iframe>',unsafe_allow_html=True)
    else:
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/103212"></iframe>',unsafe_allow_html=True)
with col3:
    curr2 = st.selectbox('Currency 2',['USD','EUR','GBP'])

url = 'https://free.currconv.com/api/v7/convert?q={curr1}_{curr2},{curr2}_{curr1}&compact=ultra&apiKey={api.api_key}'

re = requests.get(url)
re = re.json()
one_two = re[f"{curr1}_{curr2}"]
two_one = re[f"{curr2}_{curr1}"]

col1, col2 = st.columns(2)
with col1:
    st.write(f"1 {curr1} to {curr2}")
    st.success(one_two)
with col2:
    st.write(f"1 {curr2} to {curr1}")
    st.success(two_one) 

col1,col2 = st.columns(2)
with col1:
    amount = st.number_input(curr1)
with col2:
    converted = amount*one_two
    st.text("convert amount")
    st.success(converted)
st.markdown("<style> body{text-align:center;} #MainMenu, footer{visibility:hidden;} .css-ffhzg2 {background-color: #00000;}</style>",unsafe_allow_html=True)        
