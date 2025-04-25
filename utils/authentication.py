import pandas as pd
import streamlit as st

def load_user_data(file_path):
    return pd.read_csv(file_path)

def login(user_data, role):
    st.title(f"{role} Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = user_data[(user_data["Username"] == username) & (user_data["Password"] == password) & (user_data["Role"] == role)]
        if not user.empty:
            st.success(f"Welcome, {user.iloc[0]['Name']}!")
        else:
            st.error("Invalid credentials or role.")

def signup(file_path, role):
    st.title(f"{role} Signup")
    name = st.text_input("Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    location = st.text_input("Location")
    if st.button("Signup"):
        new_user = pd.DataFrame({"Name": [name], "Username": [username], "Password": [password], "Role": [role], "Location": [location]})
        new_user.to_csv(file_path, mode='a', header=False, index=False)
        st.success("Signup successful!")