import streamlit as st
from utils.authentication import login, signup
from utils.data_processing import load_crop_data, load_user_data, load_company_posts
from utils.visualization import plot_price_prediction, display_recommendations, display_marketplace
from models.crop_price_model import predict_crop_prices
from models.crop_recommendation import recommend_crops
import pandas as pd

# Sidebar for navigation
st.sidebar.title("KrishiConnect")
menu = st.sidebar.radio("Navigation", ["Home", "Login", "Signup", "Crop Price Prediction", "Crop Recommendation", "Marketplace"])

# Load data
crop_data = load_crop_data("data/crop_data.csv")
user_data = load_user_data("data/user_data.csv")
company_posts = load_company_posts("data/company_posts.csv")

# Home Page
if menu == "Home":
    st.title("Welcome to KrishiConnect!")
    st.write("Connecting Karnataka's farmers and companies.")
    st.subheader("Current Average Crop Prices in Karnataka")
    avg_prices = crop_data.groupby("Crop")["Price"].mean().head(5)
    st.table(avg_prices)

# Login and Signup
elif menu == "Login":
    role = st.selectbox("Login as:", ["Farmer", "Company"])
    login(user_data, role)

elif menu == "Signup":
    role = st.selectbox("Signup as:", ["Farmer", "Company"])
    signup("data/user_data.csv", role)

# Crop Price Prediction
elif menu == "Crop Price Prediction":
    st.title("Crop Price Prediction")
    crop = st.selectbox("Select Crop", crop_data["Crop"].unique())
    location = st.selectbox("Select Location", crop_data["Location"].unique())
    if st.button("Predict"):
        prediction = predict_crop_prices(crop, location, crop_data)
        plot_price_prediction(prediction, crop)

# Crop Recommendation
elif menu == "Crop Recommendation":
    st.title("Crop Recommendation")
    location = st.selectbox("Select Location", crop_data["Location"].unique())
    soil_type = st.selectbox("Select Soil Type", ["Sandy", "Loamy", "Clayey"])
    land_size = st.number_input("Enter Land Size (in acres)", min_value=0.1, step=0.1)
    if st.button("Recommend"):
        recommendations = recommend_crops(location, soil_type, land_size, crop_data)
        display_recommendations(recommendations)

# Marketplace
elif menu == "Marketplace":
    st.title("Crop Marketplace")
    user_role = st.selectbox("I am a:", ["Farmer", "Company"])
    if user_role == "Company":
        st.subheader("Post Crop Requirements")
        crop = st.text_input("Crop")
        quantity = st.number_input("Quantity (in tons)", min_value=1)
        contact = st.text_input("Contact Information")
        location = st.text_input("Location")
        if st.button("Post"):
            new_post = pd.DataFrame(
                {"Crop": [crop], "Quantity": [quantity], "Contact": [contact], "Location": [location]}
            )
            new_post.to_csv("data/company_posts.csv", mode='a', header=False, index=False)
            st.success("Requirement posted successfully!")
    else:
        st.subheader("View Crop Requirements")
        display_marketplace(company_posts)