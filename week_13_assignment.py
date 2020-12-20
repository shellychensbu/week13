#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:43:08 2020

@author: shellychen
"""

import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time


#pull in the file
def load_hospitals():
    df_hospital_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_2

def load_inpatient():
    df_inpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_2

#title for my website
st.title('Stony Brook Hospital Statistics Comparison')
st.write('Hello Professor Hants! :computer: :smile:')

#I am going to go over the hospital csv first
st.subheader('Comparison between Stony Brook, Mount Sinai, NYU Langone, and NY Presbyterian with Ratings')

#only pulling dataframe of all the hospitals and inpatient from csv for assignment
df_hospital_2 = load_hospitals()
df_inpatient_2 = load_inpatient()

#dataframe of all the hospitals in NY so I can find the name of the hospitals
hospitals_ny = df_hospital_2[df_hospital_2['state'] == 'NY']
inpatient_ny = df_inpatient_2[df_inpatient_2['provider_state'] == 'NY']

#dataframe of the hospitals I will be comparing from hospital csv
Stony_Brook = df_hospital_2[df_hospital_2['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']

Mount_Sinai = df_hospital_2[df_hospital_2['hospital_name'] == 'MOUNT SINAI HOSPITAL']

NYU_Langone_Medical_Center = df_hospital_2[df_hospital_2['hospital_name'] == 'NEW YORK UNIVERSITY LANGONE MEDICAL CENTER']

NY_Presbyterian_Queens = df_hospital_2[df_hospital_2['hospital_name'] == 'NEW YORK-PRESBYTERIAN/QUEENS']

#dataframe of the hospitals I will be comparing from inpatient csv matching address to those listed above
Stony_Brook_2 = df_inpatient_2[df_inpatient_2['provider_name'] == 'UNIVERSITY HOSPITAL ( STONY BROOK )']

Mount_Sinai_2 = df_inpatient_2[df_inpatient_2['provider_name'] == 'MOUNT SINAI HOSPITAL']

NYU_Langone_2 = df_inpatient_2[df_inpatient_2['provider_name'] == 'NYU HOSPITALS CENTER']

NY_Presbyterian_2 = df_inpatient_2[df_inpatient_2['provider_name'] == 'NEW YORK-PRESBYTERIAN/QUEENS']

#I want to group all the hospitals into one dataframe from hospitals csv
result = pd.concat([hospitals_ny], axis=0, join='outer', ignore_index=False)

hospitals_compared = pd.concat([Stony_Brook, Mount_Sinai, NYU_Langone_Medical_Center, NY_Presbyterian_Queens])

#I want to group all the hospitals into one dataframe from inpatient csv
result = pd.concat([inpatient_ny], axis=0, join='outer', ignore_index=False)

inpatient_compared = pd.concat([Stony_Brook_2, Mount_Sinai_2, NYU_Langone_2, NY_Presbyterian_2])

#compare location of hospitals 
st.subheader('Locations')
bar1 = hospitals_compared['city'].value_counts().reset_index()
st.dataframe(bar1)

st.write('The locations of the four hospitals include Stony Brook, New York, and Flushing. Location may affect the rating of the categories for each hospital.')

#compare ownership of hospitals
st.subheader('Hospital Ownership')
bar1 = hospitals_compared['hospital_ownership'].value_counts().reset_index()
st.dataframe(bar1)

st.write('The table shows ownership of the four hospitals being compared. Stony Brook is the only government owned hospital while the other three hospitals are voluntary non-profit, privately owned hospitals. This may be one of the explanations to the hospital ratings. Government owned hospitals provide care for patients with a variety of insurances while privately owned hospitals accept specific insurances. Because of this difference, Stony Brook may see more patients, leading to outstretched resources which can diminish their hospital ratings.')

#do they have emergency services
st.subheader('Emergency Services')
bar = hospitals_compared['emergency_services'].value_counts().reset_index()
fig = px.pie(bar, values='emergency_services', names='index')
st.plotly_chart(fig)

st.text('All four hospitals have emergency services.')

#do they meet meaningful use of ehr
st.subheader('Meaningful Use')
bar = hospitals_compared['meets_criteria_for_meaningful_use_of_ehrs'].value_counts().reset_index()
fig = px.pie(bar, values='meets_criteria_for_meaningful_use_of_ehrs', names='index')
st.plotly_chart(fig)

st.text('All four hospitals meet the criteria for meaningful use of ehrs.')

#compare effectiveness of care
st.subheader('Effectiveness of Care')
hospitals =['Stony Brook', 'Mount Sinai', 'NYU Langone', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=['Same', 'Same', 'Above', 'Same' ])])
st.plotly_chart(fig2)

st.write('Stony Brook is the same as the national average when it comes to effectiveness of care. Stony Brook has the same rating as Mount Sinai and NY Presbyterian and is doing worse compared to NYU Langone.')

#compare readmissions
st.subheader('Hospital Readmissions')
hospitals =['Stony Brook', 'Mount Sinai', 'NYU Langone', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=['Below', 'Above', 'Above', 'Below' ])])
st.plotly_chart(fig2)

st.write('Even though Stony Brook is the same as the national average when it comes to effectiveness of care, Stony Brook is below the national average when it comes to readmissions. This is kind of interesting because it can mean that Stony Brook has an effective care plan which causes a lower readmission rate. Stony Brook has the same rating as NY Presbyterian and has a better rating compared to Mount Sinai and NYU Langone.')

#compare timeliness of care
st.subheader('Timeliness of Care')
bar = hospitals_compared['timeliness_of_care_national_comparison'].value_counts().reset_index()
fig = px.pie(bar, values='timeliness_of_care_national_comparison', names='index')
st.plotly_chart(fig)

st.text('All four hospitals are below the national average when it comes to timeliness of care.')

#compare safety of care
st.subheader('Safety of Care')
hospitals =['NYU Langone', 'Stony Brook', 'Mount Sinai', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=['Below', 'Above', 'Above', 'Above' ])])
st.plotly_chart(fig2)

st.write('Stony Brook is above the national average when it comes to safety of care. Stony Brook has the same rating as Mount Sinai and NY Presbyterian and is doing better compared to NYU Langone.')

#compare patient experience
st.subheader('Patient Experience')
hospitals =['Stony Brook', 'Mount Sinai','NYU Langone', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=['Below', 'Below', 'Same', 'Below' ])])
st.plotly_chart(fig2)

st.write('Stony Brook is below the national average when it comes to patient experience. Stony Brook has the same rating as Mount Sinai and NY Presbyterian and is doing worse compared to NYU Langone.')

#compare mortality
st.subheader('Mortality')
bar = hospitals_compared['mortality_national_comparison'].value_counts().reset_index()
fig = px.pie(bar, values='mortality_national_comparison', names='index')
st.plotly_chart(fig)

st.text('All four hospitals are above the national average when it comes to mortality.')

#compare use of medical imaging
st.subheader('Efficient Use of Medical Imaging')
hospitals =['Stony Brook', 'Mount Sinai','NYU Langone', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=['Same', 'Same', 'Above', 'Same' ])])
st.plotly_chart(fig2)

st.write('Stony Brook is the same as the national average when it comes to efficient use of medical imaging. Stony Brook has the same rating as Mount Sinai and NY Presbyterian and is doing worse compared to NYU Langone.')

#compare the overall hospital ratings 
st.subheader('Hospital Overall Rating')
hospitals =['Stony Brook', 'Mount Sinai', 'NYU Langone', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=[4, 4, 5, 2 ])])
st.plotly_chart(fig2)

st.write('The hospital rating is out of a score of 5. Stony Brook has a rating of 4, which is relatively high and comparatively better than NY Presbyterian. However, NYU Langone shows the highest rating of 5, which is higher than Stony Brook. All the categories above, including effectiveness of care, readmissions, timeliness of care, safety of care, patient experience, mortality, and efficient use of medical imaging may all have affected the overall ranking.')

#I am going over the inpatient csv 
st.subheader('Comparison between Stony Brook, Mount Sinai, NYU Langone, and NY Presbyterian with Costs and Discharges')

#compare inpatient discharges 
SB_inpatient_count = sum(Stony_Brook_2['total_discharges'])

MS_inpatient_count = sum(Mount_Sinai_2['total_discharges'])

NYU_inpatient_count = sum(NYU_Langone_2['total_discharges'])

NYP_inpatient_count = sum(NY_Presbyterian_2['total_discharges'])

st.subheader('Total Discharges Per Hospital')
hospitals =['Stony Brook', 'Mount Sinai', 'NYU Langone', 'NY Presbyterian']
fig2 = go.Figure([go.Bar(x=hospitals, y=[9065, 13377, 8527, 5882])])
st.plotly_chart(fig2)

st.write('Stony Brook has 9,065 discharges, Mount Sinai has 13,377 discharges, NYU Langone has 8,527 discharges, and NY Presbyterian has 5,882 discharges.')

#compare the reasoning for the discharges 
st.subheader('Reason for Discharge')
SB_common_discharges = Stony_Brook_2.groupby('drg_definition')['total_discharges'].sum().reset_index()

MS_common_discharges = Mount_Sinai_2.groupby('drg_definition')['total_discharges'].sum().reset_index()

NYU_common_discharges = NYU_Langone_2.groupby('drg_definition')['total_discharges'].sum().reset_index()

NYP_common_discharges = NY_Presbyterian_2.groupby('drg_definition')['total_discharges'].sum().reset_index()

st.write('Stony Brook Discharges')
st.dataframe(SB_common_discharges)
st.text('The top discharge reason in Stony Brook Hospital is due to septicemia or severe sepsis.')

st.write('Mount Sinai Discharges')
st.dataframe(MS_common_discharges)
st.text('The top discharge reason in Mount Sinai is due to septicemia or severe sepsis.')

st.write('NYU Langone Discharges')
st.dataframe(NYU_common_discharges)
st.text('The top discharge reason in NYU Langone is due to joint replacement.')

st.write('NY Presbyterian Discharges')
st.dataframe(NYP_common_discharges)
st.text('The top discharge reason in NY Presbyterian is due to septicemia or severe sepsis.')

#compare costs by condition
st.subheader('Compare Costs by Condition')

SB_costs_condition = Stony_Brook_2.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.write("Stony Brook Costs by Condition - Average Total Payments")
st.dataframe(SB_costs_condition)

MS_costs_condition = Mount_Sinai_2.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.write("Mount Sinai Costs by Condition - Average Total Payments")
st.dataframe(MS_costs_condition)

NYU_costs_condition = NYU_Langone_2.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.write("NYU Langone Costs by Condition - Average Total Payments")
st.dataframe(NYU_costs_condition)

NYP_costs_condition = NY_Presbyterian_2.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.write("NY Presbyterian Costs by Condition - Average Total Payments")
st.dataframe(NYP_costs_condition)

st.write('At a glance, Stony Brook Hospital has a higher average total payment per condition compared to Mount Sinai, NYU Langone, and NY Presbyterian.')

