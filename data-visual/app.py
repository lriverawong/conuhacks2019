# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# bluebin_count_file = open("../object-count/bluebin-count","r")
# bluebin_count = bluebin_count_file.readlines()[0]
# bluebin_count_file.close()

# garbage_count_file = open("../object-count/garbage-count","r")
# garbage_count = garbage_count_file.readlines()[0]
# garbage_count_file.close()

# greenbin_count_file = open("../object-count/greenbin-count","r")
# greenbin_count = greenbin_count_file.readlines()[0]
# greenbin_count_file.close()

# greybin_count_file = open("../object-count/greybin-count","r")
# greybin_count = greybin_count_file.readlines()[0]
# greybin_count_file.close() 

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='TrashSort',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bluebin'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Greybin'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Greenbin'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Garbage'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=80)   
