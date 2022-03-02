from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # -1 is for the latest deployement and
    #  0 is the first deployment
    # ABI - brownie knows
    # Address - brownie knows
    print(simple_storage.retrieve())


def main():
    read_contract()
