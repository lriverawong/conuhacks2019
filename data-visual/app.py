# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        labels = ['Blue Bin','Grey Bin','Green Bin','Garbare'],
        values = [4500,2500,1053,500],
        colors = ['#375190', '#737680', '#4B8B4F', '#8B6D4B'],
        trace = go.Pie(labels=labels, values=values,
                hoverinfo='label+percent', textinfo='value + label',
                textfont=dict(size=30),
                marker=dict(colors=colors,
                            line=dict(color='#000000', width=1)))
        # figure={
            
        # }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=80)
