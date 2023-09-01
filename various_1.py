import streamlit as st

st.title('Various Services')

center_h = st.number_input('Center of the work should be:')
height = st.number_input('Height of Work')
width = st.number_input('Width of Work')   
from_top = st.number_input('Frame Allowance')
# from_edge = st.number_input('From Edge')
space_width = st.number_input('Space Width')

center_wall = space_width/2
screw_height = (center_h + (height/2)) - from_top 

st.write('The Screw Height should be ' + str(screw_height) + ' inches')
st.write('The Center of the Wall should be ' + str(center_wall) + ' inches')