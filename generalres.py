import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# x = ['Avengers Infinite War', 'Aquaman', 'Captain Marvel']
# mneg = [86488, 11850, 23182]
# mpos = [138819,41028,182832]
# neg = [189997, 12066, 34014]
# pos = [215512, 26690, 153656]

#  x=['So Bad', 'Bad', 'Good', 'So Good'],
#     y=[86488, 189997, 215512, 138819]

tweet1 = go.Bar(
    x=['So Bad'],
    y=[86488],
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
    y=[189997],
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
    y=[215512],
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
    y=[138819],
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
    title='Avengers Infinite War: Premiere Tweets',
)

fig = go.Figure(data=data, layout=layout)
plot(fig, filename='text-hover-bar')