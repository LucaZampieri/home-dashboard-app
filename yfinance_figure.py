import pandas as pd
import plotly.express as px
import yfinance as yf

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)


def create_yfinance_figure(row):
    ticker = row["ticker"]
    period = row["period"]

    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df["Date"] = df.index
    a = df.iloc[-1]["Date"]
    closing_value = df.iloc[-1]["Close"]
    fig = px.line(
        df,
        "Date",
        "Close",
        title=f"{ticker}-closing on {a.day_name()} {a.day}/{a.month}/{a.year}: {closing_value:0.2f}",
    )
    return fig


# create_figure(ticker="tsla")
# create_figure(ticker="vwrl.as")

# def create_figure():
#     return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
def create_figure():
    return px.bar(df, x="Fruit", y="Amount", color="Amount", barmode="group")


def create_figure2():
    return px.bar(df, x="Fruit", y="Amount", color="Amount", barmode="group")
