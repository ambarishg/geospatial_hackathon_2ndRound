import village_ui
import streamlit as st
import roads

selection = st.sidebar.selectbox("Choose the Analysis Category",
                    ("",'Socio-Economic','Roads','Railways'))

if selection == 'Socio-Economic':
    village_ui.get_socio_economic_data()
elif selection == 'Roads':
    roads.get_roads_data()
elif selection == 'Railways':
    pass

