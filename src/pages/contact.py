import dash
from dash import dcc #take out html
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Webster Chen', className='mt-3'),
    dcc.Markdown('### Fox Factory Inc. Taiwan ', className='mb-5'),
    dcc.Markdown('### Personal info', style={'color':'gray'}),
    dcc.Markdown('Address', style=green_text),
    dcc.Markdown('Taichung, Taiwan 40854'),
    dcc.Markdown('Phone Number', style=green_text),
    dcc.Markdown('0921-787-938'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('awesomewei.career@gmail.com'),
    # dcc.Markdown('Linkedin', style=green_text),
    # dcc.Markdown('[www.linkedin.com/in/cooper-chen-0968b21a1/](https://www.linkedin.com/in/cooper-chen-0968b21a1//)', link_target='_blank'),
    # dcc.Markdown('?', style=green_text),
    # dcc.Markdown('[www.youtube.com/charmingdata](https://www.youtube.com/charmingdata)', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')