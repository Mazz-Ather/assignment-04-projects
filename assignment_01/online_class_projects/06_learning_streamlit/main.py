import streamlit as st
import joblib
import os
import numpy as np
from sklearn.linear_model import LinearRegression

# Check if model exists, if not create and save a simple model
model_path = 'linear_regression_model.pkl'
if not os.path.exists(model_path):
    # Create a simple linear regression model
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])  # Simple y = 2x relationship
    model = LinearRegression()
    model.fit(X, y)
    # Save the model
    joblib.dump(model, model_path)
    st.info("Created a new model file as it didn't exist.")
else:
    # Load existing model
    model = joblib.load(model_path)

st.title('Linear Regression Prediction App')
st.write('Enter a value to predict:')
feature_value = st.number_input('Enter a value for the feature:', min_value=0.0, max_value=100.0, value=2.0)

if st.button('Predict'):
    prediction = model.predict([[feature_value]])
    st.write(f'The predicted target value is: {prediction[0]:.2f}')