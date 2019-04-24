import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

tweet1 = go.Bar(
    x=['So Bad'],
    y=[9266],
    name='So Bad',
    marker=dict(
        color='rgb(144, 91, 39)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

tweet2 = go.Bar(
    x=['Bad'],
    y=[16318],
    name='Bad',
    marker=dict(
        color='rgb(184, 115, 40)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

tweet3 = go.Bar(
    x=['Good'],
    y=[25792],
    name='Good',
    marker=dict(
        color='rgb(242, 210, 89)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

tweet4 = go.Bar(
    x=['So Good'],
    y=[37376],
    name='So Good',
    marker=dict(
        color='rgb(248, 232, 145)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

data = [tweet1, tweet2, tweet3, tweet4]
layout = go.Layout(
    title='Aquaman: Premiere Tweets',
)

fig = go.Figure(data=data, layout=layout)
plot(fig, filename='text-hover-bar')