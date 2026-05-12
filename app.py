import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Energy Foundry")
st.subheader("Interactive Solar Energy Analysis Dashboard")

# Sidebar Inputs
st.sidebar.header("System Inputs")

panel_area = st.sidebar.slider("Panel Area (m²)", 1, 50, 10)
efficiency = st.sidebar.slider("Efficiency", 0.1, 0.3, 0.2)

weather = st.sidebar.selectbox(
    "Weather Condition",
    ["Sunny", "Partly Cloudy", "Cloudy"]
)

# Weather loss factor
if weather == "Sunny":
    weather_factor = 1.0
elif weather == "Partly Cloudy":
    weather_factor = 0.75
else:
    weather_factor = 0.5

# Time simulation
hours = np.arange(6, 19)

# Irradiance simulation
irradiance = np.sin((hours - 6) / 12 * np.pi)
irradiance = np.maximum(irradiance, 0)

# Power calculation
power = irradiance * panel_area * efficiency * weather_factor

# Total energy
total_energy = np.sum(power)

# Plot graph
fig, ax = plt.subplots()

ax.plot(hours, power, marker='o')
ax.set_title("Solar Power Generation Over a Day")
ax.set_xlabel("Time (Hours)")
ax.set_ylabel("Power Output")

st.pyplot(fig)

# Metrics
st.metric("Total Energy Generated", f"{total_energy:.2f} units")

# Performance message
if total_energy > 10:
    st.success("System is performing efficiently.")
else:
    st.warning("System performance is reduced under current conditions.")

# Explanation
st.write("""
This dashboard simulates rooftop solar power generation 
based on weather conditions, panel area, and efficiency.
""")