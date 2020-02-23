import plotly.graph_objects as go

import pandas as pd

# Read in Medicaid 2017 Opioid Data
df = pd.read_csv('https://raw.githubusercontent.com/traneric/SacHacksProject2020/master/data/mapdataSorted.csv')
df.head()

df['text'] = df['name'] + '<br>Aggregate ' + (df['Total']).astype(str)
limits = [(0,1),(2,74),(75,205),(206,449),(450,3000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 4000
fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['Total']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig.update_layout(
        title_text = '2017 Total Opioid 30-day-fill-count by US City<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )
fig.show()
