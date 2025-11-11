import datetime

def get_current_date():
    """Returns the current date in 'YYYY-MM-DD' format.

    This function uses the 'datetime' module to retrieve today's date and
    formats it as a string following the ISO 8601 standard.

    Returns:
        str: The current date formatted as 'YYYY-MM-DD' (e.g., '2025-11-11').
    """

    today = datetime.date.today() \
        .strftime("%Y-%m-%d")
    return today