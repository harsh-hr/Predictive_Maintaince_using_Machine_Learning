import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
st.title('Predictive Maintenance Web App') 
st.markdown('To predict machine health of a wood cutting machine instantly.')
st.markdown('The specific type of problem is also indicated to expedite failure preemption.')
air = st.number_input('Air Temperature [K]:') 
process = st.number_input('Process Temperature [K]:') 
rotation = st.number_input('Rotational Speed[rpm]:') 
torque = st.number_input('Torque [Nm]:') 
tool_wear = st.number_input('Tool Wear [min]:') 
result = 10
if st.button("Predict"):
	result = predict(np.array([[air, process, rotation, torque, tool_wear]]))
if result == 0:
	st.text("Machine is in optimal state.")
elif result == 1:
	st.text("Machine is about to undergo a power failure. Take preemptive care now.")
elif result == 2:
	st.text("Machine is about to undergo a tool wear failure. Take preemptive care now.")
elif result == 3:
	st.text("Machine is about to undergo an overstrain failure. Take preemptive care now.")
elif result == 4:
	st.text("Machine is about to undergo a random failure. Take preemptive care now.")
elif result == 5:
	st.text("Machine is about to undergo a heat dissipation failure. Take preemptive care now.")

