from brownie import MockV3Aggregator, FundMe, network, config
from scripts.helpful_script import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAINS_ENVIROMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAINS_ENVIROMENTS:
        priceFeed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        priceFeed = MockV3Aggregator[-1].address

    print("seguimos")
    fund_me = FundMe.deploy(
        priceFeed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"ContractDeployTo: {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
