import requests
from django.conf import settings

API_URL = "http://api.exchangeratesapi.io/v1/latest"
API_PARAMS = {
    "base": "EUR",
    "access_key": settings.EXCHANGE_API_KEY,
}


def get_conversion_rate(origin: str, destination: str) -> float:
    """
    Return the conversion rate between two currencies.

    The external API always returns rates relative to EUR, so
    we convert by comparing each currency to EUR first.

    Args:
        origin (str): e.g. "BRL"
        destination (str): e.g. "USD"

    Returns:
        float: rate from origin to destination

    Raises:
        RuntimeError: for any network/JSON/key‑lookup problems
    """
    try:

        data = requests.get(API_URL, params=API_PARAMS, timeout=5).json()
        rates = data["rates"]

        origin_rate = 1 if origin == "EUR" else rates[origin]
        dest_rate = 1 if destination == "EUR" else rates[destination]

        return dest_rate / origin_rate

    except Exception as exc:
        raise RuntimeError(f"Failed to fetch exchange rate: {exc}") from exc
