import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20220220/pngtree-3d-render-heart-valve-bicuspid-human-atrium-photo-image_15742204.jpg");
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""

st.title("Heart Disease Prediction Model")
tab1,tab3=st.tabs(['Predict','Bulk Predict'])

with tab1:
    age=st.number_input("Age in years",min_value=0,max_value=120)
    sex=st.selectbox('Sex',['Male','Female'])
    chest_pain=st.selectbox('Chest Pain Type',['Typical Angina','Atypical Angina','Non-Anginal Pain','Typical Angina'])
    resting_bp=st.number_input("Resting Bp in (mm Hg)",min_value=0,max_value=300)
    chlore=st.number_input("Serum Cholesterol (mm/dl)")
    fastingbs=st.selectbox("Fasting blood Sugar",['<=120 mg/dl','> 120 mg/dl'])
    resting_ecg=st.selectbox("Resting ECG",['Normal','ST-T Wave Abnormalities','Left Ventricular Hypertrophy'])
    max_hr=st.number_input("Max Heart Rate")
    exercise_angina=st.selectbox("Exercise induced Angina",['Yes','No'])
    oldpeak=st.number_input("Oldpeak",min_value=0.0,max_value=10.0)
    st_slope=st.selectbox("Slope of Peak Exercise",['Upsloping','Flat','DownSloping'])

    sex= 0 if sex=='Female' else 1
    chest_pain=['Typical Angina','Atypical Angina','Non-Anginal Pain','Typical Angina'].index(chest_pain)
    fastingbs=1 if fastingbs=='> 120 mg/dl' else 0
    resting_ecg=['Left Ventricular Hypertrophy','Normal','ST-T Wave Abnormalities'].index(resting_ecg)
    exercise_angina=1 if exercise_angina =='Yes' else 0
    st_slope=['DownSloping','Flat','Upsloping'].index(st_slope)

    ip_data=pd.DataFrame({
        'Age':[age],
        'Sex':[sex],
        'ChestPainType':[chest_pain],
        'RestingBP':[resting_bp],
        'Cholesterol':[chlore],
        'FastingBS':[fastingbs],
        'RestingECG':[resting_ecg],
        'MaxHR':[max_hr],
        'ExerciseAngina':[exercise_angina],
        'Oldpeak':[oldpeak],
        'ST_Slope':[st_slope]
    })
    algonames=['Decision Tree','Logistic Regression','Decision Tree']
    model_names=['DecisonTree1.pkl','LogisticRegresion.pkl','SVm.pkl']
    predictions=[]
    def prediction_function(data):
        
        for modelname in model_names:
            model=pickle.load(open(modelname,'rb'))
            prediction=model.predict(data)
            predictions.append(prediction)
        return predictions
    if st.button('Submit'):
        st.subheader('Results.....')

        results=prediction_function(ip_data)

        for i in range(len(predictions)):
            st.subheader(algonames[i])
            if results[i][0]==0:
                st.write("No Heart Disease")
            else:
                st.write("Has Heart Disease")
            st.markdown("--------------------------------")
with tab3:
    st.title("Upload Your Csv File")
    st.subheader("Follow the instruction before uploading")
    st.info(""" 1] Please See to that the Dataset has only 11 columns
                2] Make Sure all the columns headers Spelling is correct.
                3] Data must be:
                    'Age' in Years
                    'Sex' Male or Female
                    'ChestPainTpe'
                    'RestingBP'
                    'Cholesterol' 
                    'FastingBS'
                    'RestingECG'
                    'MaxHR'
                    'ExerciseAngina' 
                    'Oldpeak'
                    'ST_Slope'
    """)
    uploaded_file=st.file_uploader("Upload a csv file",type=['csv'])

    if uploaded_file is not None:
        input_data=pd.read_csv(uploaded_file)
        model=pickle.load(open('SVm.pkl','rb'))
        input_data['predict']=''
        for i in range(1,len(input_data)):
            arr=input_data.iloc[i,:-1].values
            input_data['predict'][i]=model.predict([arr])[0]
        input_data.to_csv('PredictionsData.csv',index=False)
        st.write(input_data)
st.markdown(page_bg,unsafe_allow_html=True)