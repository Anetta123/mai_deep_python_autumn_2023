import unittest
from unittest.mock import AsyncMock, patch
from fetcher import handle_url


class TestHandleUrl(unittest.TestCase):
    @patch('aiohttp.ClientSession.get', new_callable=AsyncMock)
    async def test_handle_url_success(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        async with aiohttp.ClientSession() as session:
            await handle_url("http://testurl.com", session)

        mock_get.assert_called_once_with("http://testurl.com", ssl=False)

    @patch('aiohttp.ClientSession.get', new_callable=AsyncMock)
    async def test_handle_url_error(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 404
        mock_get.return_value.__aenter__.return_value = mock_response

        async with aiohttp.ClientSession() as session:
            await handle_url("http://testurl.com", session)

        mock_get.assert_called_once_with("http://testurl.com", ssl=False)


if __name__ == '__main__':
    unittest.main()
