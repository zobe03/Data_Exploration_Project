import pandas as pd
import plotly.express as px

# Daten laden
disney = pd.read_csv('1_Datenset/disney_plus_titles.csv')
netflix = pd.read_csv('1_Datenset/netflix_titles.csv')

# Genres extrahieren und binäre Matrix erstellen
disney_genres = disney['listed_in'].str.get_dummies(sep=', ')
netflix_genres = netflix['listed_in'].str.get_dummies(sep=', ')

# Korrelationsmatrix berechnen
disney_corr = disney_genres.corr()
netflix_corr = netflix_genres.corr()

# Korrelationsmatrix visualisieren mit Rot-Blau-Spektrum
fig_disney = px.imshow(disney_corr, title='Disney+ Genres Korrelationsmatrix', color_continuous_scale='RdBu')
fig_netflix = px.imshow(netflix_corr, title='Netflix Genres Korrelationsmatrix', color_continuous_scale='RdBu')

fig_disney.show()
fig_netflix.show()