# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:13:39 2023

@author: hamza
"""

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Connect to the MySQL database using SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/recruiteapp')

# Query to retrieve data from the 'poste' table
poste_query = "SELECT * FROM poste"
# Query to retrieve data from the 'candidat' table
candidat_query = "SELECT * FROM candidat"

poste_df = pd.read_sql(poste_query, engine)
candidat_df = pd.read_sql(candidat_query, engine)

# Merge DataFrames on a common column with specified suffixes
data = pd.merge(candidat_df, poste_df, how='inner', on='ID_poste', suffixes=('_candidat', '_poste'))

# Séparer les données en variables indépendantes (X) et la variable dépendante (y)
X = data[['salaire_candidat', 'diplomeNum']]
y = data['experience_candidat']

# Initialiser le modèle de régression linéaire
model = LinearRegression()

# Entraîner le modèle sur l'ensemble de données
model.fit(X, y)

# Faire des prédictions sur l'ensemble de données
y_pred = model.predict(X)


# Afficher les coefficients du modèle
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Afficher le graphique tridimensionnel
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['salaire_candidat'], data['diplomeNum'], data['experience_candidat'], c='r', marker='o')
ax.set_zlabel('Experience')
ax.set_ylabel('Diplome')
ax.set_xlabel('Salaire')
ax.set_title("Graphique 3D des prédictions par rapport aux vraies valeurs")
plt.show()