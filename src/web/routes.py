from app import app
from pages.info import info_view
from pages.home import home_view
from pages.data import data_view
from pages.about import about_view
from pages.lyrics import lyrics_view
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home_view.layout
    elif pathname == "/data":
        return data_view.layout
    elif pathname == "/lyrics_gen":
        return lyrics_view.layout
    elif pathname == "/info":
        return info_view.layout
    elif pathname == "/about":
        return about_view.layout
    else:
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised...")
            ]
        )
