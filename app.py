import streamlit as st
from pyXSteam.XSteam import XSteam

# Initialize the Steam Table (using Metric Units: bar, C)
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS) 

# --- Display Credentials ---
st.title("Vapor Thermodynamics Solver")
st.subheader("Developed by: Awais Ahmad")
st.write("**Roll Number:** 25-ME-108")
st.divider()

# --- User Inputs ---
st.sidebar.header("Input Parameters")
pressure = st.sidebar.number_input("Pressure (bar)", min_value=0.01, value=1.0, step=0.1)
calc_type = st.sidebar.selectbox("Known Condition", ["Saturated Vapor", "Saturated Liquid", "Specific Temperature"])

# --- Calculation Logic ---
st.header("Numerical Results")

try:
    if calc_type == "Saturated Vapor":
        t_sat = steamTable.tsat_p(pressure)
        h_v = steamTable.hV_p(pressure)
        s_v = steamTable.sV_p(pressure)
        
        st.success(f"Saturation Temperature: {t_sat:.2f} °C")
        st.write(f"Enthalpy of Saturated Vapor (hg): **{h_v:.2f} kJ/kg**")
        st.write(f"Entropy of Saturated Vapor (sg): **{s_v:.2f} kJ/kg·K**")

    elif calc_type == "Saturated Liquid":
        t_sat = steamTable.tsat_p(pressure)
        h_l = steamTable.hL_p(pressure)
        s_l = steamTable.sL_p(pressure)
        
        st.success(f"Saturation Temperature: {t_sat:.2f} °C")
        st.write(f"Enthalpy of Saturated Liquid (hf): **{h_l:.2f} kJ/kg**")
        st.write(f"Entropy of Saturated Liquid (sf): **{s_l:.2f} kJ/kg·K**")

    elif calc_type == "Specific Temperature":
        temp = st.sidebar.number_input("Temperature (°C)", min_value=0.01, value=100.0)
        h = steamTable.h_pt(pressure, temp)
        st.write(f"Enthalpy at {pressure} bar and {temp} °C: **{h:.2f} kJ/kg**")

except Exception as e:
    st.error(f"Error in calculation: {e}")

st.info("Note: Calculations are based on IAPWS IF-97 formulations via pyXSteam.")
