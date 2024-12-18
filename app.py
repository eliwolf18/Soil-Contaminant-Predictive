import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import joblib
import pandas as pd  # Required for DataFrame creation

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the pre-trained model
model = joblib.load("soil_contamination_model.pkl")

app.layout = html.Div(style={"backgroundImage": "url('/assets/Green.png')",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
    "minHeight": "100vh",
    "paddingTop": "30px"}, children=[
    # Title Section
    html.Div([
        html.H1("🌱 Soil Contamination Predictive Tool 🌱",
                style={"textAlign": "center", "marginTop": "40px", "marginBottom": "10px"}),
        html.H4("by Eli Kekombe",
                style={"textAlign": "center", "color": "black", "fontStyle": "italic", "marginBottom": "30px"}),
    ]),

    # Subtitle/Instructions
    html.P(
    "The goal of this data product is to help people in the environmental sector make fast predictions in determining if a soil is contaminated based on the numbers obtained from soil samples. The model was intensively trained and tested using a machine learning algorithm.",
    style={"textAlign": "center", "marginBottom": "20px", "fontSize": "12px", "color": "black", "fontStyle": "italic", "lineHeight": "1.6"}
),
    
    # Input fields
    dbc.Container([
        dbc.Row([
            dbc.Col([html.Label("Sand %", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="sand", type="number", min=0, max=100, step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Clay %", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="clay", type="number", min=0, max=100, step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Silt %", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="silt", type="number", min=0, max=100, step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("pH", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="ph", type="number", min=4, max=10, step=0.1, style={"width": "100%"})], width=3),
        ]),

        dbc.Row([
            dbc.Col([html.Label("EC mS/cm", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="ec", type="number", step=0.01, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Organic Matter %", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="om", type="number", step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("CACO3 %", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="caco3", type="number", step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Nitrate (N_NO3 ppm)", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="n_no3", type="number", step=0.1, style={"width": "100%"})], width=3),
        ]),

        dbc.Row([
            dbc.Col([html.Label("Phosphorus (P ppm)", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="p_ppm", type="number", step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Potassium (K ppm)", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="k_ppm", type="number", step=0.1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Magnesium (Mg ppm)", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="mg_ppm", type="number", step=1, style={"width": "100%"})], width=3),
            dbc.Col([html.Label("Iron (Fe ppm)", style={"fontWeight": "bold", "color": "black"}), 
                     dcc.Input(id="fe_ppm", type="number", step=0.1, style={"width": "100%"})], width=3),
        ]),
    ], style={"marginBottom": "30px"}),

    # Submit Button
    html.Div([
        dbc.Button("Predict", id="predict-button", color="primary", n_clicks=0)
    ], style={"textAlign": "center", "marginBottom": "30px"}),

    # Output Section with Progress Bar
    html.Div([
        html.Div(id="prediction-output-text", 
                 style={"textAlign": "center", "fontSize": "20px", "color": "black", "marginBottom": "20px"}),

        dbc.Progress(id="progress-bar", value=0, striped=True, animated=True, 
                     style={"height": "30px", "width": "50%", "margin": "auto"}, label="0%"),
    ], style={"marginTop": "30px"}),

   # Legend Section
html.Div([
    html.H5("📝 Legend: Explanation of Abbreviations", 
            style={"textAlign": "center", "marginTop": "40px", "fontWeight": "bold"}),

    dbc.Container([
        dbc.Row([
            # First column with 6 items
            dbc.Col([
                html.Ul([
                    html.Li([html.Span("Sand %: ", style={"fontWeight": "bold"}), 
                             "Proportion of sand in the soil sample"]),
                    html.Li([html.Span("Clay %: ", style={"fontWeight": "bold"}), 
                             "Proportion of clay in the soil sample"]),
                    html.Li([html.Span("Silt %: ", style={"fontWeight": "bold"}), 
                             "Proportion of silt in the soil sample"]),
                    html.Li([html.Span("pH: ", style={"fontWeight": "bold"}), 
                             "Measure of acidity or alkalinity of the soil"]),
                    html.Li([html.Span("EC mS/cm: ", style={"fontWeight": "bold"}), 
                             "Electrical Conductivity, indicating salt concentration"]),
                    html.Li([html.Span("O.M. %: ", style={"fontWeight": "bold"}), 
                             "Organic Matter percentage in the soil"]),
                ])
            ], width=6),

            # Second column with 6 items
            dbc.Col([
                html.Ul([
                    html.Li([html.Span("CACO3 %: ", style={"fontWeight": "bold"}), 
                             "Calcium Carbonate percentage"]),
                    html.Li([html.Span("N_NO3 ppm: ", style={"fontWeight": "bold"}), 
                             "Nitrate Nitrogen in parts per million"]),
                    html.Li([html.Span("P ppm: ", style={"fontWeight": "bold"}), 
                             "Phosphorus concentration in parts per million"]),
                    html.Li([html.Span("K ppm: ", style={"fontWeight": "bold"}), 
                             "Potassium concentration in parts per million"]),
                    html.Li([html.Span("Mg ppm: ", style={"fontWeight": "bold"}), 
                             "Magnesium concentration in parts per million"]),
                    html.Li([html.Span("Fe ppm: ", style={"fontWeight": "bold"}), 
                             "Iron concentration in parts per million"]),
                ])
            ], width=6),
        ])
    ], style={"marginTop": "20px", "marginBottom": "50px", "maxWidth": "1200px"})
])
])

# Callback for predictions
@app.callback(
    [Output("prediction-output-text", "children"),
     Output("progress-bar", "value"),
     Output("progress-bar", "label")],
    [Input("sand", "value"), Input("clay", "value"), Input("silt", "value"), Input("ph", "value"),
     Input("ec", "value"), Input("om", "value"), Input("caco3", "value"), Input("n_no3", "value"),
     Input("p_ppm", "value"), Input("k_ppm", "value"), Input("mg_ppm", "value"), Input("fe_ppm", "value"),
     Input("predict-button", "n_clicks")]
)
def predict_contamination(sand, clay, silt, ph, ec, om, caco3, n_no3, p_ppm, k_ppm, mg_ppm, fe_ppm, n_clicks):
    if n_clicks > 0:
        input_values = [sand, clay, silt, ph, ec, om, caco3, n_no3, p_ppm, k_ppm, mg_ppm, fe_ppm, 0, 0, 0, 0]
        feature_names = ["Sand %", "Clay %", "Silt %", "pH", "EC mS/cm", "O.M. %", "CACO3 %",
                         "N_NO3 ppm", "P ppm", "K ppm ", "Mg ppm", "Fe ppm", "Zn ppm", "Mn ppm",
                         "Cu ppm", "B ppm"]
        input_data = pd.DataFrame([input_values], columns=feature_names)
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        contamination_prob = probabilities[1] * 100
        result = "Contaminated" if prediction == 1 else "not Contaminated"
        return f"Prediction: The Soil is {result} with a probability of {contamination_prob:.2f}%.", contamination_prob, f"{contamination_prob:.2f}%"
    return "", 0, "0%"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8080)