import streamlit as st
import pandas as pd
import joblib

loaded_model = joblib.load('model.joblib')

# Define column names
columns = ['Total_Stops', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo', 'Airline_Jet Airways', 'Airline_Jet Airways Business', 'Airline_Multiple carriers', 'Airline_SpiceJet', 'Airline_Trujet', 'Airline_Vistara', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai', 'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata', 'Destination_New Delhi', 'Day', 'Month', 'TotalTime', 'day_of_week_Monday', 'day_of_week_Saturday', 'day_of_week_Sunday', 'day_of_week_Thursday', 'day_of_week_Tuesday', 'day_of_week_Wednesday', 'dep_timezone_Morning', 'dep_timezone_Afternoon', 'dep_timezone_Evening', 'arrival_timezone_Morning', 'arrival_timezone_Afternoon', 'arrival_timezone_Evening', 'Additional_Info_1 short layover', 'Additional_Info_2 long layover', 'Additional_Info_business class', 'Additional_Info_change airports', 'Additional_Info_in-flight meal not included', 'Additional_Info_no check-in baggage included', 'Additional_Info_red-eye flight']

# Create a dictionary to store input values
input_data = {}

st.title("Flight Fare Prediction App")
st.write("### Enter Flight Information")
c1, c2, c3 = st.columns(3)
with c1: input_data['Total_Stops'] = st.number_input("Total Stops", min_value=0)
with c2: input_data['Day'] = st.number_input("Day", min_value=1, max_value=31)
with c3: input_data['Month'] = st.number_input("Month", min_value=1, max_value=12)


c4, c5 = st.columns(2)
with c4: input_data['TotalTime'] = st.number_input("Total Time (in hours)", min_value=0.0)
with c5: airline = st.selectbox("Airline", ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 'Multiple carriers', 'SpiceJet', 'Trujet', 'Vistara'])

input_data['Airline_' + airline] = 1

# Source and Destination selection
c6, c7 = st.columns(2)
with c6: 
    source = st.selectbox("Source", ['Chennai', 'Delhi', 'Kolkata', 'Mumbai'])
    input_data['Source_' + source] = 1
with c7:
    destination = st.selectbox("Destination", ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'])
    input_data['Destination_' + destination] = 1

c8, c9, c10 = st.columns(3)
with c8:
    day_of_week = st.selectbox("Day of the Week", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    input_data['day_of_week_' + day_of_week] = 1
with c9:
    dep_timezone = st.selectbox("Departure Timezone", ['Morning', 'Afternoon', 'Evening'])
    input_data['dep_timezone_' + dep_timezone] = 1

with c10:
    arrival_timezone = st.selectbox("Arrival Timezone", ['Morning', 'Afternoon', 'Evening'])
    input_data['arrival_timezone_' + arrival_timezone] = 1

# Additional Information checkboxes
additional_info_options = ['1 short layover', '2 long layover', 'business class', 'change airports', 'in-flight meal not included', 'no check-in baggage included', 'red-eye flight']
additional_info = st.multiselect("Additional Information", additional_info_options)
for info in additional_info:
    input_data['Additional_Info_' + info] = 1

if st.button("Submit"):
    # Create a dataframe from the input data
    df = pd.DataFrame([input_data], columns=columns)
    df.fillna(0, inplace=True)
    predictions = loaded_model.predict(df)
    st.write(f"# Your flight fare will be ₹{predictions[0]:.3f}")