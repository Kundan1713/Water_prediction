import pickle
import streamlit as st
import numpy as np
import warnings

loaded_model=pickle.load(open('Water_probabilty.sav','rb'))
def prediction_water(input_data):
    input_data_in_array = np.asarray(input_data)

    reshaped_input_data = input_data_in_array.reshape(1,-1)
    prediction=loaded_model.predict(reshaped_input_data)
    return prediction

    
def main():
    warnings.filterwarnings("ignore")
    st.title("Water Protability prediction")
    ph=st.number_input("PH value")
    Hardness=st.number_input("Hardness")
    Solids=st.number_input("Solids")
    Chloramines=st.number_input("Chloramines")
    Sulfate=st.number_input("Sulfate")
    Conductivity=st.number_input("Conductivity")
    Organic_carbon=st.number_input("Organic_carbon")
    Trihalomethanes=st.number_input("Trihalomethanes")
    Turbidity=st.number_input("Turbidity")
    if st.button("Predict"):
        input_data = ([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        prediction = prediction_water(input_data)
        if prediction==1:
            result="Water is drinkable"
        else:
            result="water is not drinkable"
        st.success(result)
if __name__ == "__main__":
    main()
        
     