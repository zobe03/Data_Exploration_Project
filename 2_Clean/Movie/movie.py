import pandas as pd

# Lade die CSV-Dateien
movies_df = pd.read_csv('/Users/student/Desktop/Data_Exploration_Project/1_Datenset/movies.csv')
netflix_df = pd.read_csv('/Users/student/Desktop/Data_Exploration_Project/1_Datenset/netflix_titles.csv')

# Extrahiere die relevanten Spalten
movies_titles = movies_df['original_title']
netflix_titles = netflix_df['title']

# Finde die gemeinsamen Filme
common_titles = set(movies_titles).intersection(set(netflix_titles))

# Gib die gemeinsamen Filme aus
print("Gemeinsame Filme in beiden Datensets:")
for title in common_titles:
    print(title)

# Gib die Anzahl der gemeinsamen Filme aus
print(f"Anzahl der gemeinsamen Filme: {len(common_titles)}")