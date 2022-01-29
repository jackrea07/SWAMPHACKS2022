from pickle import TRUE
from turtle import onclick
import pandas as pd
import streamlit as st
from PIL import Image
import re
widget_values = {}

image = Image.open('logo.png')


df = pd.read_csv("Cleaned_DataNames.csv")
dfUse = df.copy()
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.title("Welcome to YOUniversity")
options = st.multiselect('What do you look for in a school?', ['Location', 'SAT Score Range', 'ACT Score Range', 'HBCU', 'Male Only', 'Female Only', 'Offers Graduate Degrees', 'Total Cost Before Financial Aid', 'Degree Area of Major'])
#st.multiselect(options, list)


if 'Location' in options: 
    Loc = st.text_input('Desired State (Acronym)', '', max_chars= 2)
    loc = Loc.upper()
    dfUse = dfUse[dfUse['STABBR'] == loc]
    
if 'SAT Score Range' in options:
    SAT= st.slider('Desired School Average SAT Score', min_value = 400, max_value = 1600,value=(700,900))
    dfUse = dfUse[(dfUse['SAT_AVG'] > SAT[0]) & (dfUse['SAT_AVG'] < SAT[1]) ] 
if 'ACT Score Range' in options :
    ACT =  st.slider('Desired School Average ACT Composite Score', min_value = 1, max_value = 36,value=(15,19))
    dfUse = dfUse[(dfUse['ACTCMMID'] > ACT[0]) & (dfUse['ACTCMMID'] < ACT[1]) ]
if 'Total Cost Range Before Financial Aid' in options:
    cost = st.slider('Desired Cost Range)', max_value= 99999, min_value = 1,value=(20000,60000))
    dfUse = dfUse[(dfUse['COSTT4_A'] > cost[0]) & (dfUse['COSTT4_A'] > cost[0])]
if 'HBCU' in options:
    dfUse = dfUse[dfUse['HBCU'] == 1]
if 'Male Only' in options:
    dfUse = dfUse[dfUse['MENONLY'] == 1]
if 'Female Only' in options:
    dfUse = dfUse[dfUse['WOMENONLY'] == 1]
if 'Offers Graduate Degrees' in options:
    dfUse = dfUse[dfUse['HIGHDEG'] == 4]
if 'Degree Area of Major' in options:
    degreeOptions = st.multiselect('What Degree Area are you interested in?', ['Agriculture',	'Natural Resources',	'Architecture	', 'Ethnic and Gender Studies', 'Communication/Journalism',	'Communication Technologies',	'Computer and Information Sciences',	'Personal and Culinary Services',	'Education','	Engineering', 'Engineering Technologies and Related Fields',	'Foreign Languages, Literatures, and Linguistics',	'Consumer Science/Human Sciences', 'Legal Professions and Studies',	'English Language/Literature','Liberal Arts Sciences, General Studies, and Humanities',	'Library Science', 'Bio-Med/Biology'	, 'Math/Statistics',	'Multi-Interdisciplinary Studies', 'Parks-Recreation, Leisure, and Fitness Studies'	, 'Philosophy and Religious Studies',	'Theology and Religious Vocations', 'Physical Sciences',	'Psychology','Homeland Security and Protective Services',	'Public Administration and Social Service',	'Social Sciences'	,'Construction Trades',	'Transportation and Materials Moving',	'Visual and Performing Arts',	'Health Professions and Related Programs',	'Business Management/Marketing',	'History'])
    #st.multiselect(options1, list1)
    
    if 'Agriculture' in degreeOptions:
        dfUse = dfUse[dfUse['Agriculture'] > 0]
    
    if 'Natural Resources' in degreeOptions:
        dfUse = dfUse[dfUse['Natural Resources'] > 0]
    
    if 'Architecture' in degreeOptions:
        dfUse = dfUse[dfUse['Architecture'] > 0]
    
    if 'Ethnic and Gender Studies' in degreeOptions:
        dfUse = dfUse[dfUse['Ethnic and Gender Studies'] > 0]
    
    if 'Communication/Journalism' in degreeOptions:
        dfUse = dfUse[dfUse['Communication Journalism'] > 0]   

    if 'Computer and Information Sciences' in degreeOptions:
        dfUse = dfUse[dfUse['Computer and Info Sciences'] > 0]
    
    if 'Personal and Culinary Services' in degreeOptions:
        dfUse = dfUse[dfUse['Personal and Culinary Services'] > 0]
    
    if 'Education' in degreeOptions:
        dfUse = dfUse[dfUse['Education'] > 0]
    
    if 'Engineering' in degreeOptions:
        dfUse = dfUse[dfUse['Engineering'] > 0]
    
    if 'Engineering Technologies and Related Fields' in degreeOptions:
        dfUse = dfUse[dfUse['Engineering Technologies and Related Fields'] > 0]
    
    if 'Foreign Languages, Literatures, and Linguistics' in degreeOptions:
        dfUse = dfUse[dfUse['Foreign Languages, Literatures, and Linguistics'] > 0]
    
    if 'Consumer Science/Human Sciences' in degreeOptions:
        dfUse = dfUse[dfUse['Consumer Science/Human Sciences'] > 0]
    
    if 'Legal Professions and Studies' in degreeOptions:
        dfUse = dfUse[dfUse['Legal Proffessions and Studies'] > 0]
    
    if 'English Language/Literature' in degreeOptions:
        dfUse = dfUse[dfUse['English Lang/Lit'] > 0]
    
    if 'Liberal Arts Sciences, General Studies, and Humanities' in degreeOptions:
        dfUse = dfUse[dfUse['Liberal Arts Sciences, General Studies, Humanities'] > 0]
    
    if 'Library Science' in degreeOptions:
        dfUse = dfUse[dfUse['Library Science'] > 0]
    
    if 'Bio-Med/Biology' in degreeOptions:
        dfUse = dfUse[dfUse['Bio-Med/Biology'] > 0]
    
    if 'Math/Statistics' in degreeOptions:
        dfUse = dfUse[dfUse['Math/Stats'] > 0]
    
    if 'Multi-Interdisciplinary Studies' in degreeOptions:
        dfUse = dfUse[dfUse['Multi-Interdisciplinary Studies'] > 0]
    
    if 'Parks-Recreation, Leisure, and Fitness Studies' in degreeOptions:
        dfUse = dfUse[dfUse['Fitness Studies'] > 0]
    
    if 'Philosophy and Religious Studies' in degreeOptions:
        dfUse = dfUse[dfUse['Philosophy and Religious Studies'] > 0]
    
    if 'Theology and Religious Vocations' in degreeOptions:
        dfUse = dfUse[dfUse['Theology and Religious Vocations'] > 0]
    
    if 'Physical Sciences' in degreeOptions:
        dfUse = dfUse[dfUse['Physical Sciences'] > 0]
    
    if 'Psychology' in degreeOptions:
        dfUse = dfUse[dfUse['Psychology'] > 0]
    
    if 'Homeland Security and Protective Services' in degreeOptions:
        dfUse = dfUse[dfUse['Homeland Security, Homeland Security, Protective Services'] > 0]
    
    if 'Public Administration and Social Service' in degreeOptions:
        dfUse = dfUse[dfUse['Public Administration and Social Service'] > 0]
    
    if 'Social Sciences' in degreeOptions:
        dfUse = dfUse[dfUse['Social Sciences'] > 0]
    
    if 'Construction Trades' in degreeOptions:
        dfUse = dfUse[dfUse['Construction Trades'] > 0]
    
    if 'Transportation and Materials Moving' in degreeOptions:
        dfUse = dfUse[dfUse['Transportation and Materials Moving'] > 0]
    
    if 'Visual and Performing Arts' in degreeOptions:
        dfUse = dfUse[dfUse['Visual and Performing Arts'] > 0]
    
    if 'Health Professions and Related Programs' in degreeOptions:
        dfUse = dfUse[dfUse['Health Professions and Related Programs'] > 0]
    
    if 'Business Management/Marketing' in degreeOptions:
        dfUse = dfUse[dfUse['Business Management Marketing'] > 0]
    
    if 'History' in degreeOptions:
        dfUse = dfUse[dfUse['History'] > 0]   

if st.button('Find My Dream Schools'):
   # col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
   # col1.metric("Institution", value = dfUse['INSTNM'])
   # col2.metric("CITY", value = dfUse['CITY'])
    #col3.metric("STATE", value = dfUse['STABBR'])
   # col4.metric("Webstie", value = dfUse['INSTURL'])
   # col5.metric("ACT Average", value = dfUse['ACTCMMID'])
   # col6.metric("SAT Average", value = dfUse['SAT_AVG'])
   # col7.metric("Admissions Rate", value = dfUse['ADM_RATE'])
    dfUse.rename(columns = {"INSTNM":"Institution", "STABBR":"State", "INSTURL":"Website", "ACTCMMID" : "ACT Average","ADM_RATE": "Admissions Rate", "CITY" : "City", "SAT_AVG" : "SAT Average" }, inplace = True)
    st.write(dfUse[['Institution','City','State','Website','ACT Average','SAT Average','Admissions Rate']])
    st.map(dfUse)