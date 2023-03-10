
import dash
import dash_bootstrap_components as dbc
#import dash_core_components as dcc
#import dash_html_components as html
from dash import html
from dash import dcc
import dash
import dash_bootstrap_components as dbc
import dash_bootstrap_templates
from dash import Input, Output, dcc, html
import dash
import dash_bootstrap_components as dbc
import dash_bootstrap_templates
from jupyter_dash import JupyterDash
from dash import Input, Output, dcc, html
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import sys
import os
import time

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
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Keyword Matrix",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Heading"),

                        html.P(
                            """\
                            This study proposes a systematic approach to examining subject development 
  and collaboration dynamics over time in educational research communities 
    by utilizing social network analysis on time-evolving co-authorship networks 
      and natural language processing. """
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],

                    md=4,
                ),
                dbc.Col(
                    html.Div([
                        html.Iframe(srcDoc=initial_html, width='70%', height='600',
                                    style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw',
                                           'margin-top': '3vw'}),
                    ]),
                )


            ],
        ),

    ],
    className="pad-row",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)

