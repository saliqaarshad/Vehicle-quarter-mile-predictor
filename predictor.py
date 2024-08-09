import pandas as pd
import streamlit as slt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from math import sqrt

# Import data
df = pd.read_csv('mtcars.csv')

# Split data into train and test sets
X = df.drop(columns=['model', 'qsec'])
y = df['qsec']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train decision tree
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)

# Streamlit app
slt.title('Quarter Mile Time Predictor')
slt.write("Enter the following values for your vehicle:")

mpg = slt.number_input("MPG:", min_value=0)
cyl = slt.number_input("Number of Cylinders:", min_value=0)
disp = slt.number_input("Displacement of Engine (cubic inches):", min_value=0)
hp = slt.number_input("Horsepower:", min_value=0)
drat = slt.number_input("Final Drive Ratio:", min_value=0.0)
wt = slt.number_input("Weight in tons:", min_value=0.0)
vs = slt.selectbox("Engine type (0 for V-shape, 1 for straight):", options=[0, 1])
am = slt.selectbox("Transmission type (0 for automatic, 1 for manual):", options=[0, 1])
gear = slt.number_input("Number of Gears:", min_value=0)
carb = slt.number_input("Number of Carburetors:", min_value=0)

Input_data = {
    'mpg': [mpg], 'cyl': [cyl], 'disp': [disp], 'hp': [hp],
    'drat': [drat], 'wt': [wt], 'vs': [vs], 'am': [am],
    'gear': [gear], 'carb': [carb]
}

data = pd.DataFrame(Input_data)
result = dt.predict(data)

# Show result
slt.write(f"Estimated quarter mile time for your vehicle is: {result[0]:.3f} seconds")

