import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

disney = pd.read_csv('1_Datenset/ursprüngliche/disney_plus_titles.csv')
Typ_Disney = disney['type'].value_counts()

netflix = pd.read_csv('1_Datenset/ursprüngliche/netflix_titles.csv')
Typ_Netflix = netflix['type'].value_counts()

netflix_kleiner_teil_index = Typ_Netflix.idxmin()
netflix_kleiner_teil_wert = Typ_Netflix.min()
netflix_großer_teil_wert = Typ_Netflix.sum() - netflix_kleiner_teil_wert

# Disney+ (rechts)
disney_kleiner_teil_index = Typ_Disney.idxmin()
disney_kleiner_teil_wert = Typ_Disney.min()
disney_großer_teil_wert = Typ_Disney.sum() - disney_kleiner_teil_wert

fig = make_subplots(rows=1, cols=1, specs=[[{'type':'xy'}]])

# Netflix und Disney+ in einem Diagramm
fig.add_trace(go.Bar(name='Netflix', x=Typ_Netflix.index, y=[netflix_großer_teil_wert, netflix_kleiner_teil_wert],
                     marker=dict(color=['#7D2020', '#7D2020']),
                     text=[netflix_großer_teil_wert, netflix_kleiner_teil_wert], textposition='auto',
                     textfont=dict(family="Arial", size=14, color="white")))

fig.add_trace(go.Bar(name='Disney+', x=Typ_Disney.index, y=[disney_großer_teil_wert, disney_kleiner_teil_wert],
                     marker=dict(color=['#7EAAD3', '#7EAAD3']),
                     text=[disney_großer_teil_wert, disney_kleiner_teil_wert], textposition='auto',
                     textfont=dict(family="Arial", size=14, color="black")))

fig.update_layout(title='<i><b>Content type provided by Netflix and Disney+</b></i>', 
                   title_font=dict(family='cursive', size=30, color='black'),
                   title_x=0.5,
                   legend=dict(
                       x=1,
                       y=1,
                       traceorder="normal",
                       font=dict(
                           family="Droid Serif",
                           size=15,
                           color="black"),
                       bgcolor="lightgrey",
                       title='Platform'
                   ))

fig.show()

# Überprüfe auf fehlende Werte in der Spalte 'type' für beide Datensätze
fehlende_werte_netflix = netflix['type'].isnull().sum()
fehlende_werte_disney = disney['type'].isnull().sum()

print(f"Fehlende Werte in 'type' Spalte bei Netflix: {fehlende_werte_netflix}")
print(f"Fehlende Werte in 'type' Spalte bei Disney+: {fehlende_werte_disney}")
