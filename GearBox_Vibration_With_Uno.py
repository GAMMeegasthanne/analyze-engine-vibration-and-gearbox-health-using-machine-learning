import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from joblib import load
import serial
import time

# Load the trained model
model_file = 'trained_model.joblib'
clf = load(model_file)

# Define a function to predict the label
def predict_label(time, magnitude):
    new_data = {'Time(s)': [time], 'Magnitude': [magnitude]}
    df_new = pd.DataFrame(new_data)
    prediction = clf.predict(df_new)
    return prediction[0]

# Serial communication settings
arduino_port = 'COM3'  # Replace with the appropriate port
baud_rate = 9600

# Establish serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow time for establishing connection

# Read gyroscopic sensor data from Arduino
def read_sensor_data():
    data = ser.readline().decode().strip().split(',')
    time = float(data[0])
    magnitude = float(data[1])
    return time, magnitude

# Control LEDs on Arduino based on classification results
def control_leds(prediction):
    if prediction == 'bad':
        ser.write(b'R')  # Send command to turn on the red LED
    else:
        ser.write(b'G')  # Send command to turn on the green LED

# Main program loop
while True:
    try:
        # Read sensor data
        time, magnitude = read_sensor_data()

        # Predict label
        prediction = predict_label(time, magnitude)
        print(f"The label for {time} seconds and {magnitude} magnitude is: {prediction}")

        # Control LEDs based on classification results
        control_leds(prediction)

    except KeyboardInterrupt:
        print("Program terminated by user")
        break

# Close the serial connection
ser.close()
