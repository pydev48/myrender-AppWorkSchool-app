import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__)

url = 'https://drive.google.com/file/d/16XN_nv6vSOb5tWFO6hnwmUFUml0_dNqr/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

df = pd.read_csv(dwn_url)
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])
projects_list = df['NPD Projects'].unique()
composite_list = ['MY23|8756|Crank, ERA ', 'MY23|9617|Crank, ERA, eMTB',
                  'MY24|9073|Chainring, Mountain 1x, ERA',
                  'MY25|23084|Handlebar, ERA 780 x 20, FOX in-house',
                  'MY25|22056|Crank, ETOR, ERA',
                 ]

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('NPD Build Schedule 2023',
                            style={'textAlign':'center'},
                    ),
                    html.Hr(),
                    html.Div('Choose Projects:'),
                    dcc.Dropdown(
                        id="dropdown",
                        options=projects_list,
                        value=composite_list,
                        multi=True,
                        style={'color': 'black'},
                    ),
                    dcc.Graph(id="gantt-graph"),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])


@callback(
    Output(component_id="gantt-graph", component_property="figure"),
    Input(component_id="dropdown", component_property="value"),
)
def create_gantt_chart(projects):
    dff = df[df["NPD Projects"].isin(projects)]
    fig = px.timeline(
        dff,
        x_start="Start",
        x_end="Finish",
        y="NPD Projects",
        color='Types of Build',
        title='NPD Gantt Chart 2023',
    )
    fig.update_yaxes(autorange="reversed")  # otherwise tasks are listed from the bottom up
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

        # add vertical line indicating specific date (e.g. today)

    today = '2023-04-24'
    fig.update_layout(shapes=[
        dict(
            type='line',
            yref='paper', y0=0, y1=1,
            xref='x', x0=today, x1=today
        )
    ])

    return fig

