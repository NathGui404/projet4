import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests


st.title('Bienvenue sur ADN Tour, votre référence tourisme en France')
df_adn = pd.read_csv("df_bus_retards.csv")

images = ['logo_adn.png']
st.sidebar.image(images, width=150)

with st.sidebar :
option_ligne = df_adn['schema'].unique()
lignes = st.sidebar.selectbox(
	"Type de point d'intérêt",
	option_ligne
	)

# Table 
df_adn_poi = df_adn[df_adn['schema']==lignes]
st.write('Liste des',lignes)


