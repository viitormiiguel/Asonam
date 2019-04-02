import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   y=['Iron Man', 'Thor', 'Hulk', 'Captain America', 'Black Widow', 'Doctor Strange', 'Spider-Man', 'Gamora', 'Thanos'],
                   x=['Morning', 'Afternoon', 'Evening', 'Morning', 'Afternoon', 'Evening'])
data=[trace]
plot(data, filename='heat-map')