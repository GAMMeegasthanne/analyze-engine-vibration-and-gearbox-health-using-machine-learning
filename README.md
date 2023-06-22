# analyze-engine-vibration-and-gearbox-health-using-machine-learning
analyze gearbox health condition with engine vibration with machine learning using Arduino and Python


https://github.com/GAMMeegasthanne/analyze-engine-vibration-and-gearbox-health-using-machine-learning/assets/80336398/8c5091a3-092e-43d7-bfb6-5392c21cf797

# Analyze Engine Vibration and Gearbox Health Using Machine Learning

This project aims to develop a machine learning-based solution for analyzing engine vibration data and assessing the health of a gearbox. By leveraging sensor data and advanced data analysis techniques, we can detect and classify the condition of the gearbox as either "good" or "bad". This analysis can help identify potential issues and enable timely maintenance, ultimately improving the reliability and performance of the engine and gearbox system.

## Features
- Acquire engine vibration data using gyroscopic sensors or similar devices.
- Preprocess and clean the raw sensor data to remove noise and outliers.
- Extract relevant features from the vibration signals, such as time and magnitude characteristics.
- Utilize a trained machine learning model, specifically a Random Forest classifier, to classify the gearbox condition as "good" or "bad".
- Visualize the classification results and provide insights into the health status of the gearbox.
- Integrate with an Arduino board to control LEDs for real-time indication of the gearbox condition.

## Dependencies
- Python: pandas, scikit-learn, joblib
- Arduino: Arduino IDE, compatible Arduino board

## Usage
1. Connect the gyroscopic sensor to the Arduino board and upload the provided Arduino script to control the LEDs.
2. Collect engine vibration data using the gyroscopic sensor and feed it to the Python script.
3. Train the Random Forest classifier on labeled datasets of "good" and "bad" gearbox conditions.
4. Save the trained model using joblib for later use.
5. Use the `predict_label()` function in the Python script to predict the gearbox condition based on new vibration data.
6. The Arduino board will receive the prediction results and illuminate the corresponding LED (green for "good" and red for "bad").
7. Analyze the gearbox health based on the LED indication and take appropriate maintenance actions if necessary.

## Acknowledgments
This project is developed with the help of open-source libraries and frameworks. We would like to express our gratitude to the developers and contributors of pandas, scikit-learn, joblib, and Arduino for their valuable tools and resources.

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, raise issues, or provide suggestions for further enhancements. Let's work together to improve engine performance and gearbox reliability through machine learning analysis of vibration data.
