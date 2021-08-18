from __future__ import annotations

from functools import lru_cache

import httpx
import pandas as pd


@lru_cache
def download_data(api_url: str) -> httpx.Response:
    """Download the data from the API.

    This data gets cached so subsequent calls will be faster.

    Args:
        api_url: The url to use for the download

    Returns:
        The httpx response

    Raises:
        HTTPStatusError
    """
    data = httpx.get(api_url)
    data.raise_for_status()
    return data


def load_data_to_dataframe(
    api_url: str = "https://opendata.arcgis.com/datasets/8b90b56df08a4bd5bc1b868396873b61_11.geojson",
) -> pd.DataFrame:
    """Converts the propertry data into a DataFrame.

    Args:
        api_url: The url to use for the download. Defaults to
            "https://opendata.arcgis.com/datasets/8b90b56df08a4bd5bc1b868396873b61_11.geojson".

    Returns:
        A DataFrame containing the property data

    Raises:
        HTTPStatusError
    """
    data = download_data(api_url)
    properties = [x["properties"] for x in data.json()["features"] if x.get("properties")]

    return pd.DataFrame(properties)
