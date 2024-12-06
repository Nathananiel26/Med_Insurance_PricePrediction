import streamlit as st
import joblib


st.title('🏥Medical Insurance Prediction')

with st.form(key='insurnace'):
    age = st.number_input('Enter your age',min_value=1,max_value=200000)
    sex = st.selectbox(label='Select your gender',options=['Male','Female'])
    sex_val = 1 if sex == 'Male' else 0

    bmi = st.number_input(label='Enter your BMI weight')
    chldren = st.number_input('Enter the number of your chilredn',min_value=0,max_value=200000)
    
    smoker = st.selectbox(label='Do you smoke ?',options=['Yes','No'])
    smoker_val = 1 if smoker == 'Yes' else 0

    region = st.selectbox(label='Select your region',options=['South West','South East','North West','North East'])
    region_val = 0
    if region == 'South West':
        region_val = 1
    elif region == 'South East':
        region_val = 2
    elif region == 'North West':
        region_val = 3
    else :
        region_val = 4

    display_button = st.form_submit_button(label='Predict')

if display_button:
    model = joblib.load('Medical_Insurance_Model')
    result = model.predict([[age,sex_val,bmi,chldren,smoker_val,region_val]])
    st.success(f'Your Medical Insurance Price is :{result}')
    st.balloons()