from urllib import request, parse
import json

from src.backend.graphs_api.definitions import LoadRunnerChart, RunnerChartResult
from src.backend.graphs_api.enums import Endpoint

class GraphsAPIClient:
    
    def __init__(self) -> None:
        self.BASE_URL = 'https://graphs.betfair.com/'
        self.headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-GB,en;q=0.9',
                    'priority': 'u=0, i',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                }
        
    def load_runner_chart(self,
                        market_id: str,
                        selection_id: int,
                        handicap: float) -> RunnerChartResult:
        
        params = LoadRunnerChart(marketId=market_id,
                        selectionId=selection_id,
                        handicap=handicap,
                        alt='json')

        req = request.Request(f'{self.BASE_URL}{Endpoint.LOAD_RUNNER_CHART.value}?{parse.urlencode(params)}', headers=self.headers, method='GET')

        try:
            with request.urlopen(req) as response:
                data = response.read().decode('utf-8')
                return RunnerChartResult(json.loads(data))
        except Exception as e:
            print(f'Error: {e}')
