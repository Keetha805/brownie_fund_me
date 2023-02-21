from brownie import FundMe
from scripts.helpful_script import get_account
from scripts.deploy import deploy_fund_me


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entranceFee = fund_me.getEntranceFee()
    print(f"Current Entrance Fee Is: {entranceFee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entranceFee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    entranceBalance = fund_me.getBalance()
    print(f"Current Balance is: {entranceBalance}")
    print("Withdrawing...")
    fund_me.withdraw({"from": account})
    entranceBalance = fund_me.getBalance()
    print(f"Current Balance is: {entranceBalance}")
    print(f"Owner: {fund_me.getOwner()}, withdrawer: {account}")


def main():
    fund()
    withdraw()
