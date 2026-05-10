import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- Sidebar: Identification ---
st.sidebar.title("Developer Info")
st.sidebar.write("**Name:** M.IBRAHIM SHAHID")
st.sidebar.write("**Roll No:** 25-ME-36")
st.sidebar.divider()

# --- App Header ---
st.title("⚙️ Mechanical Unit Converter & Density Checker")
st.markdown("---")

# --- Section 1: Unit Converter ---
st.header("1. Length/Pressure Converter")
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value:", value=1.0)
    conversion_type = st.selectbox("Select Category", ["Length (m to mm)", "Pressure (bar to psi)", "Pressure (Pa to bar)"])

with col2:
    if "Length" in conversion_type:
        result = value * 1000
        st.metric("Result (mm)", f"{result:,.2f}")
    elif "bar to psi" in conversion_type:
        result = value * 14.5038
        st.metric("Result (psi)", f"{result:,.2f}")
    elif "Pa to bar" in conversion_type:
        result = value / 100000
        st.metric("Result (bar)", f"{result:,.6f}")

# --- Section 2: Material Density Checker ---
st.markdown("---")
st.header("2. Material Density Checker")

# Dictionary of common engineering materials (kg/m^3)
densities = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Titanium": 4500,
    "Cast Iron": 7200,
    "Water": 1000
}

selected_material = st.selectbox("Select a Material:", list(densities.keys()))
density_value = densities[selected_material]

st.info(f"The density of **{selected_material}** is approximately **{density_value} kg/m³**.")

# Quick Weight Calculator
st.subheader("Quick Mass Calculator")
volume = st.number_input("Enter Volume (m³):", value=0.1)
mass = volume * density_value
st.success(f"Estimated Mass: **{mass:,.2f} kg**")
