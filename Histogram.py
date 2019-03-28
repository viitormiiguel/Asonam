import re 
import plotly.plotly as py 
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

trace0 = go.Bar(
    x=['Apr-20', 'Apr-21', 'Apr-22', 'Apr-23', 'Apr-24', 'Apr-25', 'Apr-26', 'Apr-27', 'Apr-29', 'Apr-30', 'May 01','May 02','May 03','May 04'],
    y=[6805,17711,20480,39924,65654,77098,89144,84259,162899,215512, 153673, 99806, 68257 , 64133 ],
    name='Primary Product',
    marker=dict(
        color='rgb(49,130,189)'
    )
)
trace1 = go.Bar(
    x=['Apr-20', 'Apr-21', 'Apr-22', 'Apr-23', 'Apr-24', 'Apr-25', 'Apr-26', 'Apr-27', 'Apr-29', 'Apr-30', 'May 01','May 02','May 03','May 04'],
    y=[5064,7848, 6223,10261,21389,25565,33294,53551, 93811, 189997, 141511, 85937, 58163,34715 ],
    name='Secondary Product',
    marker=dict(
        color='rgb(204,204,204)',
    )
)

data = [trace0, trace1]
layout = go.Layout(
    xaxis=dict(tickangle=-45),
    barmode='group',
)

fig = go.Figure(data=data, layout=layout)
plot(data, filename='Histogram')