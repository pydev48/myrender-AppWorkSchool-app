import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__)

filepath = ("https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
)
df = pd.read_csv(filepath)

state_list = df["state"].unique()

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
                    html.H3(
                        f"Polar Charts of U.S. Agricultural Exports, 2011",
                        style={"textAlign": "center"},
                    ),
                    html.Div("Choose the radius scale:"),
                    dcc.RadioItems(
                        id="bar-polar-app-x-radio-items",
                        options=["Absolute", "Logarithmic"],
                        value="Logarithmic",
                    ),
                    html.Br(),
                    html.Div("Choose States:"),
                    dcc.Dropdown(
                        id="bar-polar-app-x-dropdown",
                        value=state_list[:6],
                        options=state_list,
                        multi=True,
                        style={'color': 'black'},
                    ),
                    dcc.Graph(id="bar-polar-app-x-graph", figure={}),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])
#-----------------
@callback(
    Output("bar-polar-app-x-graph", "figure"),
    Input("bar-polar-app-x-dropdown", "value"),
    Input("bar-polar-app-x-radio-items", "value"),
)
def update_graph(state, radius_scale):
    filtered_df = df[df["state"].isin(state)]
    log_r = True if radius_scale == "Logarithmic" else False

    fig = px.bar_polar(
        filtered_df,
        r=filtered_df["total exports"],
        theta=filtered_df["state"],
        color=filtered_df["total exports"],
        template="plotly_white",
        color_continuous_scale=px.colors.sequential.Plasma,
        log_r=log_r,
    )
    return fig