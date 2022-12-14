import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests


st.title('Analyse du réseau de transports en commun de la ville de Rennes')
df_bus = pd.read_csv("df_bus_retards.csv")

images = ['logo_star.png', 'Bus-100x100.png']
st.sidebar.image(images, width=150)

with st.sidebar :
	with st.expander("Réseau Star BUS :"):
		st.write("Lignes de bus : 152")
		st.image("bus.jpg")

option_ligne = df_bus['ligne'].unique()
lignes = st.sidebar.selectbox(
	'Choix ligne de bus ?',
	option_ligne
	)

# Table 
df_bus_ligne = df_bus[df_bus['ligne']==lignes]
st.write('Retards les plus importants par ligne de bus et par arrêt')
df_bus_ligne=df_bus_ligne[df_bus_ligne['retard_a']=='oui'][['ligne','destination','nom_arret','arrivee_theorique','retard_arrivee']].sort_values(by='retard_arrivee',ascending=False)
df_bus_ligne

df_bus_tard = df_bus[(df_bus['ligne']==lignes)&(df_bus['retard_a']=='oui')]
st.write('Retards supérieurs à 3 minutes')
st.map(df_bus_tard[['latitude','longitude']])

