import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# ---------- Import and clean data (importing csv into pandas)
df = pd.read_csv("smallbusinessesHALI.csv")
print(df.columns)

df1 = df.drop_duplicates(subset=["NS Small Business"])
print(df.head)

dff1 = pd.read_csv("output.csv")
dff2 = dff1.dropna(0, how='any')

#start of the app
app.layout = dbc.Container([
dbc.Jumbotron(
    [dbc.Container([
                html.H1("DEAR NOVA SCOTIA", className="display-3"),
                html.P(
                    "Small business owners need your support!",
                    className="lead",
                ),
                html.P(
                    "Use this dashboard to find local businesses to support!",
                    className="lead",
                ),
                html.P(
                    "Due to the months of Covid-19 closures many of our beloved small busniesses have experienced a financial strain.           "
                           "The purpose of this dashboard is to help locals find small businesses. " 
                           "The businesses included in this dashboard are not necessarily in financial strain, but are considered small businesses and they have received on of two provinvial Impact or Repoening Grants "
                           "These businesses are in no way connected to this dashboard, this data is open to the public.",
                    className="lead",
        ),
            ],fluid=True,)], fluid=True,
),
    dbc.Row(
        # dbc.Col(html.H1("NOVA SCOTIAN BUSINESSES",
        #                 className='text-center text-primary mb-4'),
        #         width=12)
    ),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                [
                    html.H4("Purpose of this Dashboard", className="card-title"),
                    # html.H6("To support Local!", className="card-subtitle"),
                    html.P("",
                            className="card-text",
            ),
            dbc.CardLink("Link to Data", href="https://data.novascotia.ca/Business-and-Industry/Applicants-and-Recipients-of-Small-Business-Impact/xaty-cfpq"),
        ]
    ),
    #style={"width": "18rem"},
    )
        ]),
        dbc.Col([
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Type of Business', 'value': 'Type of Business'},
                     {'label': 'Received Impact Grant', 'value': 'Received Small Business Impact Grant'},
                     {'label': 'Received Reopening & Support Grant', 'value': 'Received Small Business Reopening and Support Grant'},
            ],
            value='Type of Business',
            multi=False,
            clearable=False,
            style={"width": "70%"}
        ),
            dcc.Graph(id='the_graph')
        ]# #width={'size': 5, 'offset': 0, 'order': 2},
           #xs=12, sm=12, md=12, lg=5, xl=5
        )
    ]),
    html.Div([
        # dcc.Graph(id='the_graph')
    ]),

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df1

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            #title=my_dropdown
            #hover_data=my_dropdown, labels=my_dropdown,
            #hole=.3,
            )
    piechart.update_traces(hoverinfo='percent+label')
    piechart.update_layout(margin=dict(t=5, b=5, l=5, r=5))
    piechart.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.01
    ))
    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)
