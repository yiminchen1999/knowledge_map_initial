import dash
import dash_bootstrap_components as dbc
import dash_bootstrap_templates
from dash import Input, Output, dcc, html
from dash_bootstrap_templates import load_figure_template


# Set the app and the external stylesheet
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

# Set the figure template
load_figure_template("LUX")

# Set the sidebar and content styles
SIDEBAR_STYLE = "sidebar"
CONTENT_STYLE = "content"

# Define the sidebar
sidebar = html.Div(
    [
        dbc.Row([html.P("My App", className="display-6")]),
        html.Hr(),
        html.P(
            "Individual Knowledge Map visualization", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Individual Knowledge Map Week 1", href="/", active="exact"),
                dbc.NavLink("Individual Knowledge Map Week 1 & 2", href="/page-1", active="exact"),
                dbc.NavLink("Individual Knowledge Map Week 1 & 2 & 3", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className=SIDEBAR_STYLE,
)

# Define the content
div1 = html.Div([html.Iframe(src=app.get_asset_url("social_network1.html"), id="graph1")], className="iframe")
div2 = html.Div([html.Iframe(src=app.get_asset_url("social_network2.html"), id="graph2")], className="iframe")
div3 = html.Div([html.Iframe(src=app.get_asset_url("social_network3.html"), id="graph3")], className="iframe")

content = html.Div(id="page-content", className=CONTENT_STYLE)

# Define the app layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Define the callbacks
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname: str) -> html.Div:
    if pathname == "/":
        return html.Div([
            html.P("Individual Knowledge Map Week 1", className="title"),
            div1
        ])
    elif pathname == "/page-1":
        return html.Div([
            html.P("Individual Knowledge Map Week 1 & 2", className="title"),
            div2
        ])
    elif pathname == "/page-2":
        return html.Div([
            html.P("Individual Knowledge Map Week 1 & 2 &3", className="title"),
            div3
        ])

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

    # if __name__ == "__main__":
    # app.run_server(debug=True)

    if __name__ == "__main__":
        app.run_server(debug=True)