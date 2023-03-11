import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('/Users/chenyimin/Desktop/week_keyword_table_s01_2021.csv',index_col=0)
fig = px.scatter(df, x='lasercut', y='lasercut',
                color='lasercut', hover_name='lasercut',
                 log_x=True, size_max=60)

initial_html = open("/Users/chenyimin/PycharmProjects/knowledge_map/index.html", 'r').read()
with open('/Users/chenyimin/PycharmProjects/knowledge_map/index2.html', 'r') as f:
    second_html = f.read()

with open('/Users/chenyimin/PycharmProjects/knowledge_map/index3.html', 'r') as f:
    third_html = f.read()
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("TLTL Lab Link💡", href="https://tltlab.org/")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu📚",
            children=[
                dbc.DropdownMenuItem("homepage"),
                dbc.DropdownMenuItem("analysis"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("conclusion"),
            ],
        ),
    ],
    brand="Keyword Matrix📝",
    brand_href="#",
    sticky="top",
className="navbar navbar-expand-sm bg-dark .text-white navbar-dark sticky-top" ,
)
sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Find yourself here!',
                        style={'margin-top': '12px', 'margin-left': '24px'})
            ],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [
                html.Div([ html.Hr(),
                    html.P('Find your name to see individual weekly keywords',
                           style={'margin-top': '8px', 'margin-bottom': '4px'},
                           className='bg-dark text-white'),
                    dcc.Dropdown(['student1', 'student2', 'student3','student4','student5','student6','student7','student8','student9','student10','student11','student12'], "student1",  multi=False,
                                 #options=[{'label': x, 'value': x} for x in XX], if we need larger sample size in the future
                                 style={'width': '220px'}
                                 ),

                    html.P('Find your name to see your individual aggregated keywords in 4 weeks',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='bg-dark text-white'),
                    dcc.Dropdown(
                        ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8',
                         'student9', 'student10', 'student11', 'student12'], "student1", multi=False,
                        # options=[{'label': x, 'value': x} for x in XX], if we need larger sample size in the future
                        style={'width': '220px'}
                        ),

                    html.P('See keywords of the whole class in 4 weeks',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='bg-dark text-white'),
                    dcc.Dropdown(
                        ['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10',
                         'Week11', 'Week12'], "Week1", multi=False,
                        # options=[{'label': x, 'value': x} for x in XX], if we need larger sample size in the future
                        style={'width': '220px'}
                        ),
                    html.Button(id='my-button', n_clicks=0, children='apply',
                                style={'margin-top': '16px'},
                                className='bg-dark text-white'),
                    html.Hr()
                ]
                )
            ],
            style={'height': '50vh', 'margin': '8px'}),html.Hr(),
        dbc.Row(
            [
                html.P('Brief instruction: xxxxxx', className='bg-dark text-white')
            ],
            style={"height": "45vh", 'margin': '8px'}
        )
    ]
)

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('individual weekly keywords',className='font-weight-bold'),
                        html.Iframe(srcDoc=initial_html, width='90%', height='600',
                                    style={'height': '45vh'}),

                        ]),
                dbc.Col(
                    [
                        html.P('individual aggregated keywords',className='font-weight-bold'),
                        html.Iframe(srcDoc=second_html, width='90%', height='600',
                                    style={'height': '45vh'}),
                    ])
            ],
            style={"height": "50vh"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('keywords of the whole class'),
                    html.Div([
                        dcc.Graph(id='keywords', figure=fig)
                    ]), #md=10,

                    ])
            ],
            style={"height": "50vh", 'margin': '8px'}
            )
        ]
    )

app.layout = dbc.Container(
    [dbc.Row(dbc.Col(navbar, width=40)),
html.Hr(),
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-dark'),
                dbc.Col(content, width=9)
                ]
            ),
        ],
    fluid=True
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=1234)