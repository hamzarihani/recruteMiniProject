# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 21:49:32 2023

@author: hamza
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine

# Connect to the MySQL database using SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/recruiteapp')

# Query to retrieve data from the 'poste' table
poste_query = "SELECT * FROM poste"
# Query to retrieve data from the 'candidat' table
candidat_query = "SELECT * FROM candidat"

# Read data from MySQL
poste_df = pd.read_sql(poste_query, engine)
candidat_df = pd.read_sql(candidat_query, engine)

# Merge DataFrames on a common column with specified suffixes
merged_df = pd.merge(candidat_df, poste_df, how='inner', on='ID_poste', suffixes=('_candidat', '_poste'))

# Select relevant columns for clustering
# Select relevant columns for clustering
selected_columns = ['salaire_candidat', 'experience_candidat', 'diplomeNum']
df = merged_df[selected_columns]


# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Number of clusters (adjust as needed)
k = 3

# Apply K-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)

# Plot the clusters
# Print the column names of the DataFrame
print(df.columns)

# Plot the clusters
plt.scatter(df['salaire_candidat'], df['experience_candidat'], c=df['cluster'], cmap='viridis')
plt.title('Clusters de salaire en fonction de l\'expérience')
plt.xlabel('Salaire ($)')
plt.ylabel('Expérience (années)')
plt.show()
