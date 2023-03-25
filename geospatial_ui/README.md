# Overview                 

## Problem    

**Socio Economic** Data  can be used by policy makers of the country to guide the administration for proper functioning of the country. Unfortunately the data is distributed in various formats such as shapefiles , tabular format. Insights and proper decision making is difficult since the data is not consolidated. The data is also not available to the decision makers in the format they can utilize   

## Solution / Idea 
The solution would be to develop the **SocioEconomic Hub** for India.  
The socio economic data would be consolidated with geospatial data as well as tabular data. The data would be cleaned and accurate. 
The data would be presented to the decision makers in the format they can utilize            

**Geospatial conflation** will be used to merge various sources of geospatial data and tabular data to produce meaningful insights    


# Current Implementation    

This project shows the **socio economic** data of Indian States. The data presently shown are 
* Scheduled Tribes,              
* Scheduled Caste,          
* Literacy,           
* Government Canal,          
* Private Canal,          
* Tank Irrigation,         
* River Irrigation,          
* Lake Irrigation,          
* Total Irrigation,          
* Number of Primary School,        
* Number of Middle School,           
* Number of Secondary School,        
* Number of Senior Secondary School,      
* Number of College, Number of Industrial School,       
* Number of Training School,           
* Number of Adult literacy Class/Centre        
       

The socio economic indicators are presently shown for  
*  Assam     
*  West Bengal   
*  Uttar Pradesh    
*  Union Territories              

This can be **easily extended** for other `socio economic indicators and other Indian States`
    
The indicators are shown in the Village level for the following levels     
*   District    
*   Parliamentary Constituency   
*   Assembly Constituency         

## Geospatial conflation       

Here the **Parliamentary and Assembly** constituency data is `overlayed` on the village level data to produce data at the Parliamentary and Assembly level.       


## Data for the Current Impelementation  

The data for the Socio Economic Data has been downloaded from   
* [West Bengal 2001 Socio Economic Data](https://geodata.lib.utexas.edu/catalog/nyu-2451-34360)         
* [Assam 2001 Socio Economic Data](https://geodata.lib.utexas.edu/catalog/nyu-2451-42187)     
* [Uttar Pradesh 2001 Socio Economic Data](https://geodata.lib.utexas.edu/catalog/nyu-2451-60250)     
* [GIS shapefiles for India's parliamentary and assembly constituencies including polling booth localities](https://pub.uni-bielefeld.de/record/2674065)     

# Technology      

Primary technologies used for development is   
* Python 
* Streamlit  
* Azure Database for PostgreSQL servers    

Main libraries used are GeoPandas for geospatial analysis and Folium     

## Deployment        
Deployment is done using **Microsoft Azure** using the following technologies     

* Azure File Share for storing the shapefiles    
* Docker for building the container image   
* Azure Kubernetes Service for the actual deployment        

# Key Implementation Steps for the Full Solution   

The `present solution` considers the following states    
*  Assam     
*  West Bengal   
*  Uttar Pradesh       
