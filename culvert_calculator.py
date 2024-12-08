import streamlit as st

# Title of the app
st.title("Culvert Pipe Set Calculator")

# Input fields
pipe_size = st.number_input("Pipe Size (inches)", value=15, step=1)
cover = st.number_input("Cover (inches)", value=9, step=1)
ratio = st.number_input("Ratio (e.g., 4 for 4:1)", value=4, step=1)

# Calculation
set_length = (pipe_size + cover) * ratio / 12

# Display result
st.markdown("### Set Length (feet)")
st.write(round(set_length, 2))

# Notes
st.markdown("### Notes")
st.write("""
1. Add the pipe diameter (Pipe Size) to the cover.
2. Multiply the result by the ratio (e.g., 4:1 or 6:1).
3. Divide by 12 to convert inches to feet.
4. The result is the Set Length in feet.
""")