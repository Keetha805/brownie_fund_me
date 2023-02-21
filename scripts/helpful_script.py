from brownie import MockV3Aggregator, accounts, network, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2 * (10**DECIMALS)
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAINS_ENVIROMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAINS_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Active network is{network.show_active()}")
    print("Deploying Mock...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Deployed Mock!")
