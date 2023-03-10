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

SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "25rem",
        "padding": "2rem 1rem",
        "background-color": "rgba(205, 237, 240,  1)",
    }
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
}


#div1 = html.Div([html.Iframe(src=app.get_asset_url("index1.html"), style={"width":"100%", "height":"700px"}, id="graph1")], style={"background":"transparent", "height":"700px"})
#div2 = html.Div([html.Iframe(src=app.get_asset_url("index2.html"), style={"width":"100%", "height":"700px"}, id="graph2")], style={"background":"transparent", "height":"700px"})
#div3 = html.Div([html.Iframe(src=app.get_asset_url("index3.html"), style={"width":"100%", "height":"700px"}, id="graph3")], style={"background":"transparent", "height":"700px"})

content = html.Div(id="page-content", style=CONTENT_STYLE)


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
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.Br(),html.Br(),
html.Div(
        [
            html.H5(["Find your keywords", dbc.Badge(" !!", className="display-6")]),
            html.Hr(className="my-2"),
            html.Br(),
            html.P(
                "This study proposes a systematic approach to examining subject development and collaboration dynamics over time in educational research communities by utilizing social network analysis on time-evolving co-authorship networks and natural language processing."
                
                ""
            ), dbc.Button("View weekly distributions", color="light", outline=True,id="loading-button",

                            n_clicks=0),
            html.Div([
                            dcc.Dropdown(['Week1', 'Week2', 'Week3','Week4','Week5','Week6','Week7','Week8','Week9','Week10','Week11','Week12'], "Week1", multi=True)
                        ]),

        ],
        className="h-100 p-5 text-white bg-dark rounded-3",
    ),
#html.H5(["Find your keywords", dbc.Badge("!!", className="ms-1")]),
                        html.Br(),
                       html.Br(),
                        dbc.Button("use for later",outline=True, color="dark"),
                        html.Div([
                            dcc.Dropdown(['Week1', 'Week2', 'Week3','Week4','Week5','Week6','Week7','Week8','Week9','Week10','Week11','Week12'], "Week1", multi=True)
                        ])
                    ],



                    md=4,
                ),
                dbc.Col(
                    html.Div([
                        html.Iframe(srcDoc=initial_html, width='70%', height='600',
                                    style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw',
                                           'margin-top': '3vw'}),
                    ]), md=8,
                ),
dbc.Col(
    html.Div([
        dcc.Graph(id='keywords', figure=fig)
    ]),
       ),



            ],
        ),

    ],
    className="pad-row",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'weekly keywords'
app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)

