
import dash
import dash_bootstrap_components as dbc
#import dash_core_components as dcc
#import dash_html_components as html
from dash import html
from dash import dcc

initial_html = open("/Users/chenyimin/PycharmProjects/knowledge_map/social_network1.html", 'r').read()
with open('/Users/chenyimin/PycharmProjects/knowledge_map/social_network2.html', 'r') as f:
    second_html = f.read()

with open('/Users/chenyimin/PycharmProjects/knowledge_map/social_network3.html', 'r') as f:
    third_html = f.read()

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
                        html.H2("Heading"),
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
                    html.Iframe(srcDoc=initial_html, width='65%', height='600')
                  ])
                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)

