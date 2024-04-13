import joblib
import pandas as pd


loaded_model = joblib.load('model.joblib')

row = [
    0,         # Total_Stops
    0,         # Airline_Air India
    0,         # Airline_GoAir
    0,         # Airline_IndiGo
    0,         # Airline_Jet Airways
    0,         # Airline_Jet Airways Business
    0,         # Airline_Multiple carriers
    0,         # Airline_SpiceJet
    0,         # Airline_Trujet
    1,         # Airline_Vistara
    0,         # Source_Chennai
    1,         # Source_Delhi
    0,         # Source_Kolkata
    0,         # Source_Mumbai
    0,         # Destination_Cochin
    0,         # Destination_Delhi
    1,         # Destination_Hyderabad
    0,         # Destination_Kolkata
    0,         # Destination_New Delhi
    23,        # Day
    4,         # Month
    1.16,      # TotalTime
    0,         # day_of_week_Monday
    0,         # day_of_week_Saturday
    0,         # day_of_week_Sunday
    0,         # day_of_week_Thursday
    1,         # day_of_week_Tuesday
    0,         # day_of_week_Wednesday
    1,         # dep_timezone_Morning
    0,         # dep_timezone_Afternoon
    0,         # dep_timezone_Evening
    1,         # arrival_timezone_Morning
    0,         # arrival_timezone_Afternoon
    0,         # arrival_timezone_Evening
    0,         # Additional_Info_1 short layover
    0,         # Additional_Info_2 long layover
    0,         # Additional_Info_business class
    0,         # Additional_Info_change airports
    1,         # Additional_Info_in-flight meal not included
    1,         # Additional_Info_no check-in baggage included
    0          # Additional_Info_red-eye flight
]

series = pd.Series(row)

# Reshape it into a DataFrame with one row
data = series.to_frame().T

predictions = loaded_model.predict(data)
print(f"{predictions[0]:.3f}")