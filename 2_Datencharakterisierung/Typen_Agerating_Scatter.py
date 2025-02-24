import matplotlib.pyplot as plt
import pandas as pd

# Daten laden
disney_df = pd.read_csv('1_Datenset/erstellte/cleaned/disney_plus_titles_cleaned.csv')
netflix_df = pd.read_csv('1_Datenset/erstellte/cleaned/netflix_titles_cleaned.csv')

# Ratings und deren Anzahlen für Disney+
disney_ratings = disney_df.groupby(['rating', 'type']).size().reset_index(name='count')
disney_ratings['source'] = disney_ratings['type'].apply(lambda x: 'Disney+ Movie' if x == 'Movie' else 'Disney+ Serie')
disney_ratings = disney_ratings.drop(columns=['type'])

# Ratings und deren Anzahlen für Netflix
netflix_ratings = netflix_df.groupby(['rating', 'type']).size().reset_index(name='count')
netflix_ratings['source'] = netflix_ratings['type'].apply(lambda x: 'Netflix Movie' if x == 'Movie' else 'Netflix Serie')
netflix_ratings = netflix_ratings.drop(columns=['type'])

# Zusammenführen der beiden DataFrames
all_ratings = pd.concat([disney_ratings, netflix_ratings])

# Gruppieren der Daten nach rating und source
grouped_ratings = all_ratings.groupby(['rating', 'source']).sum().unstack()

# Plot erstellen
fig, ax = plt.subplots()

# Scatterplot für jede Quelle erstellen
for source in grouped_ratings.columns.levels[1]:
    ax.scatter(grouped_ratings.index, grouped_ratings['count'][source], label=source)

# Diagramm anpassen
plt.title('Anzahl der Inhalte nach Altersfreigabe')
plt.xlabel('Altersfreigabe')
plt.ylabel('Anzahl der Inhalte')
plt.grid(True)
plt.legend(title='')


# Diagramm anzeigen
plt.show()