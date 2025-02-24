import pandas as pd
import plotly.express as px

# Daten laden
disney = pd.read_csv('1_Datenset/ursprüngliche/disney_plus_titles.csv')
netflix = pd.read_csv('1_Datenset/ursprüngliche/netflix_titles.csv')

# Kombiniere die Datensätze
all_titles = pd.concat([disney, netflix])

# Extrahiere die Top 10 Schauspieler
top_actors = all_titles['cast'].str.split(', ', expand=True).stack().value_counts().index.tolist()

# Extrahiere die Top 10 Regisseure
top_directors = all_titles['director'].str.split(', ', expand=True).stack().value_counts().index.tolist()

# Erstelle eine leere DataFrame für die Korrelationsmatrix
correlation_matrix = pd.DataFrame(index=top_actors, columns=top_directors)

# Fülle die Korrelationsmatrix
for actor in top_actors:
    for director in top_directors:
        count = all_titles[all_titles['cast'].str.contains(actor, na=False) & all_titles['director'].str.contains(director, na=False)].shape[0]
        correlation_matrix.loc[actor, director] = count

# Konvertiere die Werte zu numerischen Typen
correlation_matrix = correlation_matrix.astype(float)

# Plotten der Korrelationsmatrix
fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto", title="Korrelationsmatrix der Top 10 Schauspieler und Regisseure")
fig.show()