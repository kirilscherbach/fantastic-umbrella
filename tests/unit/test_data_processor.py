from unittest.mock import patch
from app.utilities.data_processor import process_data

# We want to patch the `fetch_data` function in the `data_processor` module.
# The `patch` decorator intercepts calls to `fetch_data` and uses a mock instead.
@patch('app.utilities.data_processor.fetch_data')
def test_process_data(mock_fetch):
    # Here, we're telling the mock to return our fake data whenever it's called.
    mock_fetch.return_value = [1, 2, 3, 4, 5]

    result = process_data("http://fakeurl.com/data")

    assert result == 15  # because 1+2+3+4+5 = 15