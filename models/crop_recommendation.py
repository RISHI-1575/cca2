def recommend_crops(location, soil_type, land_size, crop_data):
    filtered_data = crop_data[crop_data["Location"] == location]
    avg_prices = filtered_data.groupby("Crop")["Price"].mean()
    recommendations = avg_prices.sort_values(ascending=False).head(5)
    result = recommendations.reset_index()
    result.columns = ["Crop", "Profit Level"]
    result["Demand Level"] = ["High"] * len(result)
    return result