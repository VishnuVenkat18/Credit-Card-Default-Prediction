import streamlit as st
import pickle
import numpy as np
import pandas

model=pickle.load(open('model.pkl','rb'))

def predictions(RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30_59DaysPastDueNotWorse):
    input=np.array([[RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30_59DaysPastDueNotWorse]]).astype(np.float)
    pred=model.predict(input)
    return pred

def main():
    st.title("Credit Card Default Prediction")
    html_temp=""" 
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Credit Card Default Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    RevolvingUtilizationOfUnsecuredLines=st.text_input('RevolvingUtilizationOfUnsecuredLines','Type Here')
    age=st.text_input('age','Type Here')
    NumberOfTime30_59DaysPastDueNotWorse=st.text_input('NumberOfTime30-59DaysPastDueNotWorse','Type Here')

    safe_html ="""  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;">Loan can be Granted</h2>
        </div>
        """
    warn_html ="""  
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;">Loan cannot be granted</h2>
        </div>
        """
    

    if st.button("Get Score"):
        output=predictions(RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30_59DaysPastDueNotWorse)
    st.success('The Score is {}'.format(output))
    if output == 1:
        st.markdown(safe_html,unsafe_allow_html=True)
    elif output == 2:
        st.markdown(warn_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()