import plotly.express as px
from plotly.graph_objects import Figure

from dsproject import download_data
from dsproject.utils.get_current_date import get_current_date

def plot_stock_data(
    ticker: str, 
    start_date: str = "2015-01-01", 
    end_date: str = get_current_date()
) -> Figure:
    
    """Generates an interactive line plot of a stock's closing price.

    This function downloads historical stock data for a given ticker
    and visualizes the 'Close' price over the specified date range using
    Plotly Express.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
        start_date (str, optional): The starting date for the data fetch, 
            formatted as 'YYYY-MM-DD'. Defaults to "2015-01-01".
        end_date (str, optional): The ending date for the data fetch, 
            formatted as 'YYYY-MM-DD'. Defaults to today's date.

    Returns:
        plotly.express.Figure: An interactive Plotly figure object 
            showing the stock's closing price over time.
    """

    data = download_data(ticker, start_date, end_date)
    fig = px.line(
        data,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} Stock Price'
    )

    return fig