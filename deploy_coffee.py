import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os
import warnings # imported to use warnings

warnings.filterwarnings("ignore", category = UserWarning) # I am using RPC from Alchemy. Alchemy has probably disabled the debug API... most likely because they are computationally expensive. And I keep getting a warning concerning it when I deploy this script

load_dotenv()

rpc = os.getenv("RPC_URL")

env = NetworkEnv(EthereumRPC(rpc))
boa.set_env(env)

price_feed = os.getenv("PRICE_FEED")

key = os.getenv("KEY")
account = Account.from_key(key)
boa.env.add_account(account, force_eoa = True)

def main():
    print("Reading into contract \n......")
    coffee_contract = boa.load("buy_me_coffee.vy", price_feed)
    # print(coffee_contract)

    coffee_amount = coffee_contract.getRate(1)
    print(coffee_amount)

if __name__ == "__main__":
    main()

