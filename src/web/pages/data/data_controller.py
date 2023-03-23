import json
from src.web.app import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


@app.callback(Output('filter-query-input', 'style'), Output('filter-query-output', 'style'),
              Input('filter-query-read-write', 'value'))
def query_input_output(val):
    input_style = {'width': '100%'}
    output_style = {}
    if val == 'read':
        input_style.update(display='none')
        output_style.update(display='inline-block')
    else:
        input_style.update(display='inline-block')
        output_style.update(display='none')
    return input_style, output_style


@app.callback(
    Output('datatable-advanced-filtering', 'filter_query'),
    Input('filter-query-input', 'value'))
def write_query(query):
    if query is None:
        return ''
    return query


@app.callback(Output('filter-query-output', 'children'),
              Input('datatable-advanced-filtering', 'filter_query'))
def read_query(query):
    if query is None:
        return "No filter query"
    return dcc.Markdown('`filter_query = "{}"`'.format(query))


@app.callback(
    Output('datatable-query-structure', 'children'),
    Input('datatable-advanced-filtering', 'derived_filter_query_structure')
)
def display_query(query):
    if query is None:
        return ''
    return html.Details([
        html.Summary('Derived filter query structure'),
        html.Div(dcc.Markdown('''```json
{}
```'''.format(json.dumps(query, indent=4))))
    ])
