import os
from web3 import Web3
from dotenv import load_dotenv

# .envファイルから秘密鍵やRPCエンドポイントをロード
load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")

# ScrollのネットワークRPCエンドポイント
SCROLL_RPC_URL = f"https://scroll-testnet.infura.io/v3/{INFURA_PROJECT_ID}"

# Web3インスタンスを作成
w3 = Web3(Web3.HTTPProvider(SCROLL_RPC_URL))

# ウォレットアドレスの取得
account = w3.eth.account.from_key(PRIVATE_KEY)
wallet_address = account.address

# 必要に応じてチェーンIDやガス価格などもここで管理
CHAIN_ID = 534353  # ScrollのチェーンID
GAS_PRICE = w3.toWei('20', 'gwei')
