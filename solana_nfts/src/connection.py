import requests

from solana_nfts.src.constants import (
    TOKEN_VIEWER_BASE_URL
)

class SplTokenViewerApiClient(object):
    def __init__(self):
        self.base_url = TOKEN_VIEWER_BASE_URL

    def fetch_nfts_from_wallet_addresses(self, addresses):
        responses = []
        for address in addresses:
            responses.extend(self.fetch_nfts_from_wallet_adddress(address))
        return responses

    def fetch_nfts_from_wallet_address(self, address):
        url = '{}fetch_nft_data'.format(self.base_url)
        params = {'address': address}
        response = requests.get(url,params=params)
        return response.json()['nfts']

