import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import sys
import os
#sys.path.append(path)
print(os.getcwd())
#os.chdir('/Users/chenyimin/PycharmProjects/knowledge_map/')
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "25rem",
    "padding": "2rem 1rem",
    "background-color": "rgba(205, 237, 240,  1)",
}
#"/Users/chenyimin/PycharmProjects/knowledge_map
#
#cd C:/Users/chenyimin/PycharmProjects/knowledge_map
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
}

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
    style=SIDEBAR_STYLE,
)

div1 = html.Div([html.Iframe(src=app.get_asset_url("social_network1.html"), style={"width":"100%", "height":"700px"}, id="graph1")], style={"background":"transparent", "height":"700px"})
div2 = html.Div([html.Iframe(src=app.get_asset_url("/knowledge_map/social_network2.html"), style={"width":"100%", "height":"700px"}, id="graph2")], style={"background":"transparent", "height":"700px"})
div3 = html.Div([html.Iframe(src=app.get_asset_url("/knowledge_map/social_networ3.html"), style={"width":"100%", "height":"700px"}, id="graph3")], style={"background":"transparent", "height":"700px"})

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])     

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [html.P("Individual Knowledge Map Week 1", style={"background":"rgba(205, 237, 240,  1)", 
                "height":"45px", "text-align":"center", "line-height":"45px", "border-radius":"4px", "font-size":"20px"}), div1]
    elif pathname == "/page-1":
        return [html.P("Individual Knowledge Map Week 1 & 2", style={"background":"rgba(205, 237, 240,  1)", 
                "height":"45px", "text-align":"center", "line-height":"45px", "border-radius":"4px", "font-size":"20px"}), div2]
    elif pathname == "/page-2":
        return [html.P("Individual Knowledge Map Week 1 & 2 &3", style={"background":"rgba(205, 237, 240,  1)", 
                "height":"45px", "text-align":"center", "line-height":"45px", "border-radius":"4px", "font-size":"20px"}), div3]

    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run_server(debug=True)
