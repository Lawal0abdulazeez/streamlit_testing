import numpy as np 
import pickle
import pandas as pd 
import streamlit as st 

from PIL import Image


pickle_in = open('regmodel.pkl', 'rb')
regressor = pickle.load(pickle_in)


def predict_score1(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,
                  RAD,TAX,PTRATIO,B,LSTAT):
    prediction = regressor.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,
                                     AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
    print(prediction)
    return prediction



def predict_score(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
    try:
        # Convert input features to numeric
        input_data = [[float(CRIM), float(ZN), float(INDUS), float(CHAS), float(NOX),
                       float(RM), float(AGE), float(DIS), float(RAD), float(TAX),
                       float(PTRATIO), float(B), float(LSTAT)]]

        # Make prediction
        prediction = regressor.predict(input_data)

        return prediction[0]
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    st.title('Classifier')
    html_temp = """
    <div style="background-color: tomato;padding: 10px;">
    <h2 style="color: white; text-align: center;"> Classifier</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    CRIM= st.text_input('CRIM', 'Type Here')
    ZN= st.text_input('ZN', 'Type Here')
    INDUS= st.text_input('INDUS', 'Type Here')
    CHAS= st.text_input('CHAS', 'Type Here')
    NOX= st.text_input('NOX', 'Type Here')    
    RM= st.text_input('RM', 'Type Here')
    AGE= st.text_input('AGE', 'Type Here')
    DIS= st.text_input('DIS', 'Type Here')
    RAD= st.text_input('RAD', 'Type Here')
    TAX= st.text_input('TAX', 'Type Here')
    PTRATIO= st.text_input('PTRATIO', 'Type Here')
    B= st.text_input('B', 'Type Here')
    LSTAT= st.text_input('LSTAT', 'Type Here')
    result = ""
    if st.button("Prediction"):
        result = predict_score(CRIM,ZN,INDUS,CHAS,NOX,RM,
                               AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    st.success('The output is {}'.format(result))
    if st.button('About'):
        st.text('Lets Learn')
        st.text('Build with Streamlit')
        
if __name__ == '__main__':
    main()