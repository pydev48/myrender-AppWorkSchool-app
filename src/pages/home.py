import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('# WEBSTER CHEN', style={'textAlign':'center'}),
    dcc.Markdown('Taichung, Taiwan', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('Results-driven Project Lead with extensive experience in managing complex projects from initiation to'
                 ' completion.  \n'
                 'Proven track record of leading cross-functional teams and ensuring project milestones are met on time\n'
                 ' '
                 'and within budget. Passionate about leveraging data to drive business growth. ',
                 style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Project implementation and coordination
            * Effective communication
            * Process development and improvement
            ''')
        ], width={"size": 4, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Cross-functional team leadership 
            * Data manipulation and analytical skill
            * Problem solving
            ''')
        ], width={"size": 4})
    ], justify='center'),

    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('09/2020 to current', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Manufacturing Engineering Project Lead \n'
                         'Fox Factory Inc. Taiwan',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Led a new product development team of 5 engineers in the successful development and deployment'),
                html.Li('Collected and manipulated multiple Excel files to visualize and analyze Engineering test builds using Python programming language(see Projects - App3)'),
                # html.Li(''),
                html.Li('Collaborated with cross-functional teams to implement project plans, ensuring quality and improving scalability for future growth')
            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2016 to 08/2020',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Worldwide Process Development Engineer \n'
                         'Corning Incorporated Taiwan',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Worked on engineering project management and process development in the early stage, mainly, for '
                    'ultra thin glass projects with members from different countries or various departments'),
                html.Li(
                    'Led or engaged in new equipment development for production capability upgrade and continuous process improvement'),
                html.Li(
                    'Analyzed process data, responded to the result, and optimized to improve the engineering performance and quality'),

            ])
        ], width=7)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('09/2015 to 02/2016',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Senior Program Engineer \n'
                         'Gogoro Taiwan Limited',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Identified requirements and potential risks, allocated resources, and communicated extensively '
                    'with venders and project staff to ensure successful daily battery production and establish the '
                    'cordial working relationship'),
                html.Li(
                    'Issued and circulated engineering change request (ECR) and maintained bill of material (BOM) '
                    'regularly to provide the right parts in the right quantities at the right time'),
                html.Li(
                    'Arranged, traced and reviewed the progress of sample plans to enhance the performance of battery'),

            ])
        ], width=7)
    ], justify='center'),

    dbc.Row([
            dbc.Col([
                dcc.Markdown('01/2010 to 05/2014',
                             style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                dcc.Markdown('Camera Lens Assembly Department Supervisor \n'
                             'Hon Hai Precision Ind.',
                             style={'white-space': 'pre'},
                             className='ms-3'),
                html.Ul([
                    html.Li(
                        'Adjusted, calibrated and optimized the performance of lens assembly machines to ensure the '
                        'successful completion of sample build during the NPI process'),
                    html.Li(
                        'Handled at least 10 projects at a time in an effective manner, eliminated bottlenecks and '
                        'achieved the daily production goal'),
                    html.Li(
                        'Managed the department of lens assembly for more than 600 employees, identified required '
                        'resources and coordinated with project stakeholders to ensure success of projects'),

                ])
            ], width=7)
        ], justify='center'),


    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('02/2008 to 06/2008',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Exchange Student Program\n'
                         'Czech Technical University(CTU) - Prague, CZ',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=7)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('09/2006 to 09/2008',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Master of Science Degree in Mechanical Engineering\n'
                         'National Taiwan University of Science and Technology(NTUST) - Taipei, TW',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=7)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('09/2004 to 06/2006',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Bachelor of Science Degree in Mechanical Engineering\n'
                         'National Taiwan University of Science and Technology(NTUST) - Taipei, TW',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=7)
    ], justify='center'),
])