import random
import time
from web3 import Web3
from .config import w3, wallet_address, PRIVATE_KEY, CHAIN_ID, GAS_PRICE

# Ambient DEXのアドレスとコントラクトABI（必要に応じて修正）
AMBIENT_DEX_ADDRESS = "0x..."  # Ambient DEXのアドレスを指定
AMBIENT_DEX_ABI = [...]  # DEXのコントラクトABI

# ETHとUSDCのトークンアドレス
ETH_TOKEN_ADDRESS = "0x0000000000000000000000000000000000000000"  # ETHはネイティブ
USDC_TOKEN_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eb48"  # USDCのアドレス

# コントラクトインスタンスを作成
dex_contract = w3.eth.contract(address=AMBIENT_DEX_ADDRESS, abi=AMBIENT_DEX_ABI)

def swap_eth_to_usdc(amount_in_wei):
    # トランザクションの作成
    txn = dex_contract.functions.swap(
        ETH_TOKEN_ADDRESS,  # From token (ETH)
        USDC_TOKEN_ADDRESS,  # To token (USDC)
        amount_in_wei,  # スワップするETHの量
        wallet_address  # 受け取りアドレス
    ).buildTransaction({
        'from': wallet_address,
        'value': amount_in_wei,
        'gas': 200000,
        'gasPrice': GAS_PRICE,
        'nonce': w3.eth.getTransactionCount(wallet_address),
        'chainId': CHAIN_ID
    })

    # トランザクションに署名
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

    # トランザクションの送信
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    # トランザクションハッシュの表示
    print(f"Swap Transaction sent with hash: {tx_hash.hex()}")

    # トランザクションの確認
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Transaction receipt: {receipt}")

def run_swap_bot():
    while True:
        # スワップするETHの量（例として0.01 ETH）
        eth_amount = w3.toWei(0.01, 'ether')

        # スワップを実行
        swap_eth_to_usdc(eth_amount)

        # ランダムな待機時間（例: 30〜60秒）
        wait_time = random.randint(30, 60)
        print(f"Waiting for {wait_time} seconds before next swap...")
        time.sleep(wait_time)
