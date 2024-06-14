from abc import ABC, abstractmethod
import requests
from typing import Any, Dict, Optional, Set, List

class BaseAPIClient(ABC):

    def __init__(self, main_app_instance) -> None:
        self._main_app_instance = main_app_instance
        self.BASE_URL = None
        self.timeout = None

    @property
    @abstractmethod
    def headers(self) -> Dict[str, str]:
        """Headers to be used in the request."""
        pass

    def _request(self, method: str, endpoint: str, json_data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=json_data, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except requests.ConnectionError:
            raise Exception("A connection error occurred")
        except requests.Timeout:
            raise Exception("The request timed out")
        except requests.RequestException as e:
            raise Exception(f"An error occurred: {e}")

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", endpoint, json_data=json_data)

    def put(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("PUT", endpoint, json_data=json_data)

    def delete(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("DELETE", endpoint, json_data=json_data)

    def _handle_response(self, response: requests.Response) -> Any:
        if response.status_code >= 400:
            self._handle_api_specific_errors(response)
            raise Exception(f"HTTP {response.status_code}: {response.text}")
        try:
            return response.json()
        except ValueError:
            raise Exception("Invalid JSON response")

    @abstractmethod
    def _handle_api_specific_errors(self, response: requests.Response) -> None:
        """Handle API-specific errors."""
        pass
