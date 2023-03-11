import dash
from dash import Dash, html, dcc, Input, Output, MATCH, callback_context, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import dash_loading_spinners as dls
#pip install dash-loading-spinners
df = pd.read_csv('/Users/chenyimin/Desktop/week_keyword_table_s01_2021.csv',index_col=0)
fig = px.scatter(df, x='lasercut', y='lasercut',
                color='lasercut', hover_name='lasercut',
                 log_x=True, size_max=60)

initial_html = open("/Users/chenyimin/PycharmProjects/knowledge_map/index.html", 'r').read()
with open('/Users/chenyimin/PycharmProjects/knowledge_map/index2.html', 'r') as f:
    second_html = f.read()

with open('/Users/chenyimin/PycharmProjects/knowledge_map/index3.html', 'r') as f:
    third_html = f.read()

sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Find yourself here!',
                        style={'margin-top': '12px', 'margin-left': '24px'})
                ],
            style={"height": "5vh"},
            className='bg-primary text-white font-italic'
            ),
        dbc.Row(
            [
                html.Div([
                    html.P('Find your name to see individual weekly keywords',
                           style={'margin-top': '8px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(['Week1', 'Week2', 'Week3','Week4','Week5','Week6','Week7','Week8','Week9','Week10','Week11','Week12'], "Week1", multi=True),
                    html.P('Find your name to see your individual aggregated keywords in 4 weeks',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(['Week1', 'Week2', 'Week3','Week4','Week5','Week6','Week7','Week8','Week9','Week10','Week11','Week12'], "Week1", multi=True),
                    html.P('See keywords of the whole class in 4 weeks',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(['Week1', 'Week2', 'Week3','Week4','Week5','Week6','Week7','Week8','Week9','Week10','Week11','Week12'], "Week1", multi=True),
                    html.Button(id='my-button', n_clicks=0, children='apply',
                                style={'margin-top': '16px'},
                                className='bg-dark text-white'),
                    html.Hr()
                    ]
                    )
                ],
            style={'height': '50vh', 'margin': '8px'}),
        ]
    )



#div1 = html.Div([html.Iframe(src=app.get_asset_url("index1.html"), style={"width":"100%", "height":"700px"}, id="graph1")], style={"background":"transparent", "height":"700px"})
#div2 = html.Div([html.Iframe(src=app.get_asset_url("index2.html"), style={"width":"100%", "height":"700px"}, id="graph2")], style={"background":"transparent", "height":"700px"})
#div3 = html.Div([html.Iframe(src=app.get_asset_url("index3.html"), style={"width":"100%", "height":"700px"}, id="graph3")], style={"background":"transparent", "height":"700px"})

#content = html.Div(id="page-content", style=CONTENT_STYLE)


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
className="navbar navbar-expand-sm bg-dark .text-white navbar-dark sticky-top",
)

sidebar = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.Br(),html.Br(),
html.Div(
        [
            html.H5(["Find your keywords", dbc.Badge(" !", className="display-5")]),
            html.Hr(className="my-2"),
            html.Br(),
            html.P(
                "This study proposes a systematic approach to examining subject development"
            ), dbc.Button("View weekly distributions", color="light", outline=True,id="loading-button",
                            n_clicks=0),
            html.Div([
                html.P('See your individual weekly keywords',
                       style={'margin-top': '8px', 'margin-bottom': '4px'},
                       className='font-weight-bold'),
                dcc.Dropdown(['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10',
                              'Week11', 'Week12'], "Week1", multi=True,style={'width': '220px'}),
                html.P('See your individual aggregated keywords in 4 weeks',
                       style={'margin-top': '16px', 'margin-bottom': '4px'},
                       className='font-weight-bold'),
                dcc.Dropdown(['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10',
                              'Week11', 'Week12'], "Week1", multi=True,style={'width': '220px'}),
                html.P('See keywords of the whole class in 4 weeks',
                       style={'margin-top': '16px', 'margin-bottom': '4px'},
                       className='font-weight-bold'),
                dcc.Dropdown(['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10',
                              'Week11', 'Week12'], "Week1", multi=True,style={'width': '220px'}),
                html.Button(id='my-button', n_clicks=0, children='apply',
                            style={'margin-top': '16px'},
                            className='bg-dark text-white'),
            ],
            )
        ],
        className="h-100 p-5 text-white bg-dark rounded-3",
    ),
#html.H5(["Find your keywords", dbc.Badge("!!", className="ms-1")]),

                    ],
                    md=5,#the width of the black sidebar
                ),
            ],
        ),

    ],
    style={'height': '50vh', 'margin': '8px'}#className="pad-row",
)

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.Iframe(srcDoc=initial_html, width='90%', height='600',
                                    style={'height': '60vh', 'margin': '8px'}),
                    ]), #md=5,
                ),
                dbc.Col(
                    html.Div([
                        dcc.Graph(id='keywords', figure=fig)
                    ]), #md=10,
                ),
            ],style={'height': '50vh',
                   'margin': '8px'}),
        ], className="embed-responsive embed-responsive-21by9",
    )






app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = 'weekly keywords'
#app.layout = html.Div([navbar, sidebar,body])



app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navbar, width=14),
                dbc.Col(sidebar, width=8),
                dbc.Col(content, width=9),
                ]
            ),
        ],
    fluid=True
    )
if __name__ == "__main__":
    app.run_server(debug=True, port=8888)

