import yfinance as yf
import pandas as pd

from dsproject.utils.get_current_date import get_current_date

def download_data(
    ticker: str = "AAPL",
    start_date: str = "2015-01-01",
    end_date: str = get_current_date(),
    multi_level: bool = False
) -> pd.DataFrame:
    """
    Downloads historical stock market data for a specified ticker using Yahoo Finance API.

    Parameters
    ----------
    ticker : str, optional
        The stock ticker symbol (default is "AAPL")
    start_date : str, optional
        Start date for data collection in 'YYYY-MM-DD' format (default is "2020-01-01")
    end_date : str, optional
        End date for data collection in 'YYYY-MM-DD' format (default is "2020-12-31")
    multi_level : bool, optional
        If True, returns data with multi-level column index (default is False)

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the historical stock market data with columns:
        Date, Open, High, Low, Close, Adj Close, and Volume

    Example
    -------
    >>> df = download_data("MSFT", "2022-01-01", "2022-12-31")
    """

    result = (
        yf.download(ticker,
            start = start_date,
            end =  end_date,
            multi_level_index = multi_level
        ) \
        .reset_index()
    )

    return result

