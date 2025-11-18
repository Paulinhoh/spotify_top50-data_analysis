import pandas as pd
import plotly.express as px


table = pd.read_csv("top50.csv", encoding="latin1")
table = table.rename(
    columns={
        "Beats.Per.Minute": "BPM",
        "Loudness..dB..": "Volume",
        "Valence.": "Valence",
    }
)
table = table[["BPM", "Volume", "Energy", "Danceability", "Valence"]]

# Normalize BPM and Volume columns
table["BPM"] = table["BPM"] / 2
table["Volume"] = (table["Volume"] + 11) * 10
print(table.describe())

# Median
table_median = table.median()
print(table_median)

# Create radar chart
graph = px.line_polar(
    r=table_median.values,
    theta=table_median.index,
    range_r=[0, 100],
    line_close=True,
    title="Top 50 Spotify Songs - Average Attributes",
)
graph.show()
