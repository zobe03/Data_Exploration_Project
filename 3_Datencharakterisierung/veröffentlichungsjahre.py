import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("1_Datenset/netflix_titles.csv")

# Veröffentlichungsjahre visualisieren
plt.figure(figsize=(10,5))
sns.histplot(df['release_year'], bins=20, kde=True)
plt.title("Verteilung der Veröffentlichungsjahre")
plt.show()
