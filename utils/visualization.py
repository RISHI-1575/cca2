import streamlit as st
import matplotlib.pyplot as plt

def plot_price_prediction(predictions, crop):
    """Plot crop price predictions for the next 6 months."""
    months = ["April", "May", "June", "July", "August", "September"]
    plt.figure(figsize=(10, 5))
    plt.plot(months, predictions, marker='o', color='green')
    plt.title(f"Price Prediction for {crop}")
    plt.xlabel("Month")
    plt.ylabel("Price (in INR)")
    plt.grid(True)
    st.pyplot(plt)

def display_recommendations(recommendations):
    """Display crop recommendations in a table."""
    st.subheader("Recommended Crops")
    st.table(recommendations)

def display_marketplace(company_posts):
    """Display marketplace posts in a table."""
    st.subheader("Crop Requirements")
    if not company_posts.empty:
        st.table(company_posts)
    else:
        st.write("No crop requirements posted yet.")