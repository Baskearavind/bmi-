import streamlit as st

# Page setup
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator App")
st.markdown("### Calculate your Body Mass Index easily!")

# Input fields
st.write("Enter your details below:")

weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0, step=0.1)
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight 😔"
            color = "lightblue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight 😊"
            color = "lightgreen"
        elif 25 <= bmi < 29.9:
            category = "Overweight 😐"
            color = "orange"
        else:
            category = "Obese 😟"
            color = "red"

        # Display results
        st.markdown(f"""
        <div style="background-color:{color};padding:15px;border-radius:10px;text-align:center;">
            <h2>Your BMI: {bmi:.2f}</h2>
            <h3>Category: {category}</h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid height.")
