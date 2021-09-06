import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html


df = pd.read_parquet('./data/songs.parquet')
df['id'] = df['title']


layout = html.Div([

    dcc.RadioItems(
        id='filter-query-read-write',
        options=[
            {'label': 'Read filter_query', 'value': 'read'},
            {'label': 'Write to filter_query', 'value': 'write'}
        ],
        value='read'
    ),

    html.Br(),
    dcc.Input(id='filter-query-input', placeholder='Enter filter query'),
    html.Div(id='filter-query-output'),
    html.Hr(),

    dash_table.DataTable(
        id='datatable-advanced-filtering',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in df.columns
            if i != 'id'
        ],
        data=df.to_dict('records'),
        editable=True,
        page_action='native',
        page_size=15,
        filter_action="native"
    ),
    html.Hr(),
    html.Div(id='datatable-query-structure', style={'whitespace': 'pre'})
])

