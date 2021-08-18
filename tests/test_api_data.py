from unittest.mock import patch

import pandas as pd
from httpx import Response

from fire_data import api_data


@patch("httpx.get")
@patch("httpx.Response.raise_for_status")
def test_download_data(mock_raise, mock_get, mock_api_data):
    mock_response = Response(200, headers={"content-type": "application/json"}, json=mock_api_data)
    mock_get.return_value = mock_response
    mock_raise.return_value = None
    data = api_data.download_data("https://test.com")

    assert data.json() == mock_api_data


@patch("httpx.get")
@patch("httpx.Response.raise_for_status")
def test_load_data_to_dataframe(mock_raise, mock_get, mock_api_data):
    mock_response = Response(200, headers={"content-type": "application/json"}, json=mock_api_data)
    mock_get.return_value = mock_response
    mock_raise.return_value = None

    expected_df = pd.DataFrame(
        [x["properties"] for x in mock_api_data["features"] if x.get("properties")]
    )

    df = api_data.load_data_to_dataframe()
    assert df.equals(expected_df)
