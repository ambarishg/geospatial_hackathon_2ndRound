import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np  
from village_data import *
from config import *

def found_item(choice):
    found = False
    for name in vars_map_pop_up:
        if(name == choice):
            found = True
            break
    return found

def intialize_vars():
    analysis_level, pc, ac, district, page_category='', '', '', '', ''
    return(analysis_level, pc, ac, district, page_category)

def set_analysis_labels(analysis_level, pc, ac, district, page_category, state):
    if(analysis_level == 'Parliament'):
        st.subheader( 
        page_category + " in the parliament constituency " + pc + 
        " in " + state)
    elif(analysis_level == 'Assembly'):
        st.subheader( 
        page_category + " in the assembly constituency " + ac + 
        " in " + state)
    else:
        st.subheader( 
    page_category + " in the district " + str(district) + 
    " in " + state)

def set_summary_stats_label(analysis_level, pc, ac, district, page_category):
    if(analysis_level == 'Parliament'):
        st.subheader("Summary " + page_category + " Statistics of the parliament constituency " + pc)   
    elif(analysis_level == 'Assembly'):
        st.subheader("Summary " + page_category + " Statistics of the assembly constituency " + ac)
    else:
        st.subheader("Summary " + page_category + " Statistics of the district " + str(district))

def set_maps_label(analysis_level, pc, ac, district, page_category):
    if(analysis_level == 'Parliament'):
        st.subheader(page_category + \
            " map of the parliament constituency " + pc)
    elif(analysis_level == 'Assembly'):
        st.subheader(page_category + \
            " map of the assembly constituency " + ac)
    else:
        st.subheader(page_category + \
            " map of the district " + str(district))


def set_summary_stats(choice, df):
    st.write("Median  :" + str(df[choice].median()))
    st.write("Maximum  :" + str(df[choice].max()))
    st.write("Minimum  :" + str(df[choice].min()))
    st.write("Standard Deviation  :" + str(df[choice].std()))

def get_socio_economic_data ():

    analysis_level, pc, ac, district, page_category= intialize_vars()
    mx=None 

    state = st.sidebar.selectbox("Choose the State",
                (vars_state_list))    

    if(state == ''):
        return

    page_category = st.sidebar.selectbox("Choose the Indicator",
                (vars_indicators))

    if(page_category == ''):
        return
    choice = vars_book[page_category]
    analysis_level = st.sidebar.selectbox("Choose the Analysis Level",
                (vars_analysis_level))

    if(analysis_level == 'Parliament'):
        assembly_data = get_parliament_data(state)

        pc_all = assembly_data
        pc_all = np.sort(pc_all)

        pc = st.sidebar.selectbox("Choose the Parliament Constituency",
                    pc_all)    
        
        if(pc==''):
            return

        mx = get_census_data_analysis_level(state, \
            analysis_level,pc = pc,choice=choice)

        
    elif(analysis_level == 'Assembly'):
        assembly_data = get_assembly_data(state)

        ac_all = assembly_data
        ac_all = np.sort(ac_all)

        ac = st.sidebar.selectbox("Choose the Assembly Constituency",
                    ac_all)    
        if(ac == ''):
            return
                  

        mx = get_census_data_analysis_level(state, \
            analysis_level,ac = ac,choice=choice)

    elif(analysis_level == 'District'):
        district_all = get_district_data(state)
        district_all = np.sort(district_all)
        district = st.sidebar.selectbox("Choose the District",
                (district_all))
        if (district == ''):
            return
        mx = get_census_data_analysis_level(state, \
            analysis_level,district=district,choice=choice)

    st.title("Village Level Data for " + state )

   
    set_analysis_labels(analysis_level, pc, ac, district, page_category, state)
    

    if(mx is None):
        return

    df = mx[["NAME",choice]].sort_values(by=[choice],ascending = False)
    st.dataframe(df.head(10),use_container_width = True)

    
    set_summary_stats_label(analysis_level, pc, ac, district, page_category)
    set_summary_stats(choice, df)

    set_maps_label(analysis_level, pc, ac, district, page_category)
    ax = mx.plot(
    column=choice,  # Data to plot
    figsize=(15, 10),
    scheme="Quantiles",  # Classification scheme
    cmap="Reds",  # Color palette
    edgecolor="k",  # Borderline color
    linewidth=0.1,  # Borderline width
    legend=True,  # Add legend
    legend_kwds={
    "fmt": "{:.0f}"
    },  # Remove decimals in legend (for legibility)
    missing_kwds={
    "color": "lightgrey",
    "edgecolor": "red",
    "hatch": "///",
    "label": "Missing values",}
    )
    ax.set_axis_off()
    plt.savefig(GEOSPATIAL_FILE_PATH + 'Choice.png')
    st.image(GEOSPATIAL_FILE_PATH + 'Choice.png',width=1000)
    
    vars_map_pop_up = ["NAME"]
    vars_map_pop_up.append(choice)
    m=mx.explore(popup=vars_map_pop_up,tooltip=vars_map_pop_up)
    st.components.v1.html(m._repr_html_(),height=800,width=800)

















