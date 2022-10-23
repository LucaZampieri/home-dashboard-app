# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from yfinance_figure import create_figure, create_figure2, create_yfinance_figure


stocks = pd.read_csv("./stocks.csv", skipinitialspace=True)

app = Dash(__name__)


# layout_col_1 = [
#     dcc.Graph(id="example-graph", figure=fig),
# ]
# layout_col_2 = [
#     dcc.Graph(id="example-graph-2", figure=fig2),
# ]
# layout_col_3 = []
app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for your data.
        """
        ),
        html.Div(
            children=[
                dcc.Graph(
                    # id="example-graph-5",
                    figure=create_figure(),
                ),
            ],
            style={
                "display": "inline-block",
                "vertical-align": "top",
                "margin-left": "3vw",
                "margin-top": "3vw",
                "width": "30%",
            },  # , 'margin-left': '3vw', 'margin-top': '3vw'}
        ),
        html.Div(
            children=[
                dcc.Graph(
                    # id="example-graph-6",
                    figure=create_yfinance_figure(row),
                )
                for index, row in stocks.iterrows()
            ],
            style={
                "display": "inline-block",
                "vertical-align": "top",
                "width": "30%",
            },  # , 'margin-left': '3vw', 'margin-top': '3vw'}
        ),
        html.Div(
            children=[
                dcc.Graph(
                    # id="example-graph-",
                    figure=create_figure(),
                ),
            ],
            style={
                "display": "inline-block",
                "vertical-align": "top",
                "width": "30%",
            },  # , 'margin-left': '3vw', 'margin-top': '3vw'}
        ),
        # dbc.Col(
        # [
        #     dbc.Row(layout_col_1),
        #     dbc.Row(layout_col_2),
        #     dbc.Row(layout_col_3),
        # ]),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
