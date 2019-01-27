import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='ktrnklmv', api_key='pyFLAnrG0KjfKFkNfOvt')

trace = {'x':[1,2], 'y':[1,2]}
data = [trace]
layout = {}
fig = go.Figure (
data = data, layout = layout)

plot_url = py.plot(fig)