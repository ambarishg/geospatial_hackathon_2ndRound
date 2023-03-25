import geopandas as gpd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import psycopg2
from config import *

# create the sqlalchemy connection engine
db_connection_url = "postgresql://ambarish:%s@ambarishpgsql.postgres.database.azure.com/socioeconomic" % quote_plus("Kolkata@1234")

def make_postgrevar(var):
    return "\"" + var + "\""

def get_all_vars(choice):
    return make_postgrevar("NAME") + "," + \
        make_postgrevar(choice) + ",geometry "

def get_assembly_table_name(state):
    return vars_state[state] + "_assembly"

def get_parliament_table_name(state):
    return vars_state[state] + "_parliamentary"

def get_district_table_name(state):
    return "india_village_census_2001_" + vars_state[state] 

def get_assembly_census_table_name(state):
    return  vars_state[state] + "_assembly_village_census_2001"

def get_parliamentary_census_table_name(state):
    return  vars_state[state] + "_parliamentary_village_census_2001"

def get_assembly_census_query(state, ac,choice):
    return "SELECT " +  get_all_vars(choice) +" FROM " + \
        get_assembly_census_table_name(state) + \
            " WHERE ac_name = '" + ac + "'"

def get_parliament_census_query(state, pc,choice):
    return "SELECT " +  get_all_vars(choice) +" FROM " + \
        get_parliamentary_census_table_name(state) + \
            " WHERE pc_name = '" + pc + "'"

def get_district_census_query(state, district,choice):
    return "SELECT " + get_all_vars(choice) + " FROM " + \
        get_district_table_name(state) + \
            " WHERE " + "\"DISTRICT\"" + " = " + str(district)

def get_census_data_analysis_level(state, \
    analysis_level,choice, \
        pc='', ac='', district=''):
    if(analysis_level == 'Parliament'):
        query = get_parliament_census_query(state, pc,choice)
    elif(analysis_level == 'Assembly'):
        query = get_assembly_census_query(state, ac,choice)
    else:
        query = get_district_census_query(state, district,choice)
    
    
    con = create_engine(db_connection_url)

    df = gpd.GeoDataFrame.from_postgis(query,con,geom_col='geometry')
    return df

def get_lov(query):
    connection = psycopg2.connect(user="ambarish",
                                  password="Kolkata@1234",
                                  host="ambarishpgsql.postgres.database.azure.com",
                                  port="5432",
                                  database="socioeconomic")
    cursor = connection.cursor()
    
    postgreSQL_select_Query = query
    lov =[]
    cursor.execute(postgreSQL_select_Query)
    records = cursor.fetchall()
    for row in records:
        lov.append(row[0])
    connection.close()
    return lov

def get_assembly_data(state):
    query = "SELECT ac_name FROM " + get_assembly_table_name(state)
    return get_lov(query)

def get_parliament_data(state):
    query = "SELECT pc_name FROM " + get_parliament_table_name(state)
    return get_lov(query)

def get_district_data(state):
    query = "SELECT DISTINCT " + "\"DISTRICT\""+" FROM " + get_district_table_name(state)
    return get_lov(query)
