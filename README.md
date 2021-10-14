[![Twitter][twitter]](https://twitter.com/cryptomafiagg)
[![Pypi][pypi]](https://pypi.org/project/solana-nfts/)

<br/>
<p align="center">
    <a href="https://github.com/Cryptomafiagg/solana-nfts-python">
        <img src="https://github.com/Cryptomafiagg/solana-nfts-python/blob/7d694afa42e28a9ca8bcd29bf763e750277046d6/assets/doges.gif" alt="" width="150" height="150">
    </a>
    <h3 align="center">
        Solana-Nfts-Python
    </h3>
    <h4 align="center">
        Cryptomafia
    </h4>
    <p align="center">
        🎨 A python client for querying the nfts in your wallet.
    </p>

</p>

## Table of Contents

- [I. Overview](#overview)
- [II. Install](#install)
- [III. Usage](#usage)
- [IV. Notes](#notes)

[twitter]: https://img.shields.io/twitter/follow/CryptomafiaGG?style=social
[pypi]: https://img.shields.io/pypi/v/solana_nfts

## I. Overview <a name="overview"></a>

Query your Metaplex Spl Tokens with easy to use apis.

## II. Install <a name="install"></a>

```
pip install solana_nfts==0.0.5
```

## III. Usage <a name="usage"></a>

```
from solana_nfts import Client`

nft_client = Client()

address = "<YOUR_SOLANA_PUBLIC_ADDRESS>"

nfts = nft_client.fetch_nfts_from_wallet_address(address)

```

The following returns an array `nfts` of json objects.

Each element of this array contains a json object with the following schema:

<li> The `arweave_metadata` key gives us a json object containing the arweave metadata for the nft.</li>

<li>The `token_metadata` key gives us a json object containing the solana token metadata for the nft.</li>

```

{
    "arweave_metadata": {
        "attributes": [
            {
                "trait_type": "Mint Number",
                "value": 2353
            },
            {
                "trait_type": "Generation",
                "value": 1
            },
            {
                "trait_type": "Name",
                "value": "Jane"
            },
            {
                "trait_type": "Species",
                "value": "Doge"
            },
            {
                "trait_type": "Rarity",
                "value": "Legendary"
            },
            {
                "trait_type": "Race",
                "value": "Northern"
            },
            {
                "trait_type": "Outline",
                "value": "None"
            },
            {
                "trait_type": "Head",
                "value": "Gold Helmet"
            },
            {
                "trait_type": "Face",
                "value": "Beard"
            },
            {
                "trait_type": "Mouth",
                "value": "None"
            },
            {
                "trait_type": "Ear",
                "value": "None"
            },
            {
                "trait_type": "Boots",
                "value": "Iceskating Boots"
            },
            {
                "trait_type": "Top",
                "value": "None"
            },
            {
                "trait_type": "Pants",
                "value": "None"
            },
            {
                "trait_type": "Tail",
                "value": "Fire Tail"
            },
            {
                "trait_type": "Necklace",
                "value": "None"
            }
        ],
        "description": "Jane (#2353) is a unique, adorable, and algorithmically generated doge with Proof of Ownership on the Solana Blockchain.",
        "external_url": "",
        "image": "https://www.arweave.net/wY60DNoCoNzFQXYTVnDCH8I9axZY1dbHnyJW1FMRAEE?ext=png",
        "name": "Jane",
        "properties": {
            "category": "image",
            "files": [
                {
                    "type": "image/png",
                    "uri": "REDACTED"
                }
            ]
        },
        "seller_fee_basis_points": 500,
        "symbol": ""
    },
    "token_metadata": {
        "account": "REDACTED",
        "lamports": 1461600,
        "metadata": {
            "data": {
                "creators": [
                    {
                        "address": "REDACTED",
                        "share": 0,
                        "verified": 1
                    },
                    {
                        "address": "REDACTED",
                        "share": 100,
                        "verified": 0
                    }
                ],
                "name": "Jane",
                "sellerFeeBasisPoints": 500,
                "symbol": "",
                "uri": "REDACTED"
            },
            "isMutable": 1,
            "key": 4,
            "mint": "REDACTED",
            "primarySaleHappened": 1,
            "type": "metaplex",
            "updateAuthority": "REDACTED"
        },
        "ownerProgram": "REDACTED",
        "rentEpoch": 233,
        "tokenInfo": {
            "decimals": 0,
            "name": "Jane",
            "supply": "1",
            "symbol": "",
            "tokenAuthority": "REDACTED",
            "type": "nft"
        },
        "type": "token_account"
    }
}

```

## IV. Notes <a name="usage"></a>

1) The shape of "arweave_metadata" will vary depending on how the nft was defined.
2) TODO: Finish Go routines for the cryptomafia api.
3) TODO: Parse json into python classes

<p align="center">
    Designed with ❤️ by Sieve Labs
</p>


