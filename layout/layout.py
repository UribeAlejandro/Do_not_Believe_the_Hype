import dash_html_components as html
import dash_core_components as dcc
from layout.sidebar.sidebar import CONTENT_STYLE, sidebar


content = html.Div(id="page-content", style=CONTENT_STYLE)
layout = html.Div([dcc.Location(id="url"), sidebar, content])
