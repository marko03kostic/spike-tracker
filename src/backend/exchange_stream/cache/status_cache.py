from dataclasses import dataclass

from src.backend.exchange_stream.definitions import BetfairStatusMessage
from src.backend.exchange_stream.enums import StatusCode, ErrorCode

@dataclass
class StatusCache:
    connections_available: int = 10
    connection_closed: bool = False

    def update(self, message: BetfairStatusMessage) -> None:
        self.connection_closed = message.get('connectionClosed', False)
        self.connections_available = message.get('connectionsAvailable')

        status_code = message.get('statusCode')
        
        error_code = message.get('errorCode')
        error_message = message.get('errorMessage')
        
        if status_code == StatusCode.SUCCESS:
            pass
        elif status_code == StatusCode.FAILURE:
            print(error_code)
            print(error_message)