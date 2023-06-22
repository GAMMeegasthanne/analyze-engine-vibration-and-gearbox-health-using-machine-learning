import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from joblib import load

# Load the trained model
model_file = 'trained_model.joblib'
clf = load(model_file)

# Define a function to predict the label
def predict_label(time, magnitude):
    new_data = {'Time(s)': [time], 'Magnitude': [magnitude]}
    df_new = pd.DataFrame(new_data)
    prediction = clf.predict(df_new)
    return prediction[0]

# Example usage
new_time = 11
new_magnitude = 900.0
prediction = predict_label(new_time, new_magnitude)
print(f"The label for {new_time} seconds and {new_magnitude} magnitude is: {prediction}")
