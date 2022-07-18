
#importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import plotly.express as px
import plotly.graph_objects as go
import os


attacks = pd.read_csv("/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/output/attacks_updated.csv")

#country and hypotheses testing
##count unique occurrences of countries
set(attacks["country"])

##function country - hemisphere
North=['ADMIRALTY ISLANDS',' TONGA','AMERICAN SAMOA','ARUBA', 'AZORES','BARBADOS','BAHAMAS', 'BERMUDA', 'BELIZE','BRITISH ISLES',
      'DOMINICAN REPUBLIC','COSTA RICA','CROATIA','CUBA','ENGLAND','CHINA','IRAQ','IRAN','ISRAEL','ITALY','JAPAN','COLUMBIA','CANADA','CENTRAL PACIFIC',
       'CARIBBEAN SEA', 'TURKS & CAICOS','ST. MAARTIN','ST. MARTIN', 'TRINIDAD & TOBAGO', 'TONGA','TAIWAN','VIETNAM','THAILAND','USA', 'SOUTH CHINA SEA', 'SOUTH KOREA','UNITED KINGDOM','UNITED ARAB EMIRATES (UAE)','UNITED ARAB EMIRATES','SRI LANKA', 'PUERTO RICO','PHILIPPINES','TURKEY','SPAIN','SINGAPORE','PALESTINIAN TERRITORIES','SOMALIA','SIERRA LEONE','PANAMA','SENEGAL', 'SAUDI ARABIA','SCOTLAND','RUSSIA','PORTUGAL','PALA','OKINAWA','NICARAGUA','NIGERIA','MICRONESIA','NEW BRITAIN','MID ATLANTIC OCEAN','MARSHALL ISLANDS', 'MALAYSIA','JAMAICA', 'INDIA', 'HONG KONG','HONDURAS','GUINEA','GUAM','GRENADA','EL SALVADOR', 'CAYMAN ISLANDS','GRAND CAYMAN','FEDERATED STATES OF MICRONESIA', 'MALTA', 'GREECE','FRANCE','MEXICO','NORWAY','BRITISH VIRGIN ISLANDS', 'BRITISH WEST INDIES',]
South=['ARGENTINA','PAPUA NEW GUINEA', 'WESTERN SAMOA','URUGUAY','TANZANIA', 'SOLOMON ISLANDS','SAMOA','SEYCHELLES','ANDAMAN / NICOBAR ISLANDAS', 'AUSTRALIA', 'BRAZIL','BRITISH NEW GUINEA','CHILE','EGYPT ','EGYPT','CAPE VERDE','ECUADOR','FIJI','Fiji',
      'DIEGO GARCIA','NEW GUINEA','VANUATU','VENEZUELA','SOUTH AFRICA','NEW CALEDONIA','MOZAMBIQUE','NEW ZEALAND', 'KENYA','KIRIBATI','MADAGASCAR','MAURITIUS', 'MALDIVES','FRENCH POLYNESIA','INDONESIA',]

def hemisphere(country):
   
    if country in North:
        return 'North Hemisphere'
    elif country in South:
        return 'South Hemisphere'
    else:
        return ''

##new column hemisphere
attacks['hemisphere']=attacks['country'].apply(lambda x: hemisphere(x))

##function hemisphere - code
North_dict={'Dec':'winter','Jan':'winter','Feb':'winter','Mar':'spring','Apr':'spring','May':'spring','Jun':'summer',
           'Jul':'summer','Aug':'summer','Sep':'autumn','Oct':'autumn','Nov':'autumn'}
South_dict={'Dec':'summer','Jan':'summer','Feb':'summer','Mar':'autumn','Apr':'autumn','May':'autumn','Jun':'winter',
           'Jul':'winter','Aug':'winter','Sep':'spring','Oct':'spring','Nov':'spring'}


def season_hemisphere(month,hemisphere):
   
    if hemisphere == 'North Hemisphere':
        return North_dict[month]
    elif hemisphere == 'South Hemisphere':
        return South_dict[month]
    else:
        return ''

##new column season per month and hemisphere
attacks['season_hemisphere']=attacks.apply(lambda x: season_hemisphere(x['month'],x['hemisphere']),1)
attacks

##Which hemisphere has more attacks?
def hemisphere_count():
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.countplot(ax=ax,x=attacks.loc[attacks['hemisphere']!=''].hemisphere)
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/Attacks_per_hemisphere.png')


##creating x and y for plotly
def plot_season():
    y_axis=['summer','winter','spring','autumn']
    x_axis=[len(attacks.loc[attacks['season_hemisphere']=='summer']),
        len(attacks.loc[attacks['season_hemisphere']=='winter']),
        len(attacks.loc[attacks['season_hemisphere']=='spring']),
        len(attacks.loc[attacks['season_hemisphere']=='autumn'])]

##Do most attsacks happen during summer?
def plot_attacks_season():
    fig=go.Figure(go.Bar(x=x_axis,y=y_axis,orientation='h'))
    fig.show()

##Do most attacks happen during summer and winter comparing hemispheres?
def plot_hemisphere_season():
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.countplot(ax=ax,data=attacks.loc[attacks['hemisphere']!=''], x="hemisphere", hue="season_hemisphere")
    fig.savefig('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/figures/Attacks_per_hemisphere_season.png')


##save dataset updated
attacks.to_csv('/Users/Juliana/Desktop/Ironhack/Projects/Ironhack-Project/output/attacks_updated.csv',index=False)