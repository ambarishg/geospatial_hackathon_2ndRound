GEOSPATIAL_FILE_PATH =""

vars_state_list = ["","Assam",'West Bengal',
'Union Territories','Uttar Pradesh']

vars_state = {'West Bengal': 'westbengal',
    'Assam': 'assam',
    'Uttar Pradesh': 'uttarpradesh',}

vars_analysis_level = ["","Parliament",'Assembly','District']

vars_indicators =["","Scheduled Tribes",'Scheduled Caste',
    'Literacy','Government Canal',
    'Private Canal','Tank Irrigation',
    'River Irrigation','Lake Irrigation',
    'Total Irrigation','Number of Primary School',
    'Number of Middle School','Number of Secondary School',
    'Number of Senior Secondary School',
    'Number of College','Number of Industrial School',
    'Number of Training School',
    'Number of Adult literacy Class/Centre']

vars_book = {'Scheduled Tribes': 'P_ST', 
    'Scheduled Caste': 'P_SC', 'Literacy': 'P_LIT',
    'Government Canal':'CANAL_GOVT','Private Canal':'CANAL_PVT',
    'Tank Irrigation':'TANK_IRR','River Irrigation':'RIVER_IRR',
    'Lake Irrigation':'LAKE_IRR','Total Irrigation':'TOT_IRR',
    'Number of Primary School':'P_SCH','Number of Middle School':'M_SCH',
    'Number of Secondary School':'S_SCH','Number of Senior Secondary School':'S_S_SCH',
    'Number of College':'COLLEGE','Number of Industrial School':'IND_SCH',
    'Number of Training School':'TR_SCH','Number of Adult literacy Class/Centre':'ADLT_LT_CT',}
    
vars_map_pop_up = ["NAME"]

class postgresql_creds:
    host = "ambarishpgsql.postgres.database.azure.com"
    port = 5432
    database = "socioeconomic"
    user = ""
    password = ""