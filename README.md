🌱 Soil Contamination Predictive Tool

Overview

The Soil Contamination Predictive Tool is a data product designed to help environmental specialists quickly determine whether soil samples are contaminated based on input properties. It leverages a Machine Learning model trained on soil data to provide accurate predictions.

Features
	•	Input soil properties (e.g., pH, Sand %, Clay %).
	•	Predict whether the soil is Contaminated or Not Contaminated.
	•	Displays the probability of contamination in an interactive progress bar.
	•	User-friendly interface built with Dash.
	•	Deployed using Render for easy accessibility.

How It Works
	1.	Enter soil properties such as:
	•	Sand %, Clay %, Silt %, pH
	•	Electrical Conductivity (EC), Organic Matter %, and more.
	2.	Click the Predict button.
	3.	View:
	•	The contamination result.
	•	The probability of contamination visually displayed in a progress bar.

Prerequisites
	•	Python 3.8 or higher.
	•	Required libraries (see requirements.txt).

 Clone the repository: git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>

Install the dependencies: pip install -r requirements.txt

Run the app locally: python app.py

	4.	Open the app in your browser at http://127.0.0.1:8050.
