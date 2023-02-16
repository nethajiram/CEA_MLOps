import pickle
import streamlit as st 


pickle_in = open("rfc.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,CreditCard,SecuritiesAccount,CDAccount,Online):
    prediction=classifier.predict([[Age,Experience,Income,Family,CCAvg,Education,Mortgage,CreditCard,SecuritiesAccount,CDAccount,Online]])
    print(prediction)
    return prediction

def main():
    st.title("Credit Card Prediction")
    Age = st.text_input("Age")
    Experience = st.text_input("Experience")
    Income = st.text_input("Income")
    Family = st.text_input("Family")
    CCAvg = st.text_input("CCAvg")
    Education = st.text_input("Education")
    Mortgage = st.text_input("Mortgage")
    CreditCard = st.text_input("CreditCard")
    SecuritiesAccount = st.text_input("Securities Account")
    CDAccount = st.text_input("CD Account")
    Online = st.text_input("Online")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,CreditCard,SecuritiesAccount,CDAccount,Online)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    
