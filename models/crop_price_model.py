from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_crop_prices(crop, location, crop_data):
    filtered_data = crop_data[(crop_data["Crop"] == crop) & (crop_data["Location"] == location)]
    X = filtered_data[["Month", "Year"]]
    y = filtered_data["Price"]
    model = LinearRegression()
    model.fit(X, y)
    future_months = pd.DataFrame({"Month": [4, 5, 6, 7, 8, 9], "Year": [2025] * 6})
    predictions = model.predict(future_months)
    return predictions