Here’s a **simple-English `README.md`** you can use.

---

# Nadfun Python SDK (beta)

This is a small Python SDK to **get quotes** and **trade tokens** with the Nadfun contracts
(BondingCurve + Wrapper).

---

## What you can do

- **Quotes**

  - `get_amount_out(token, amount_in, is_buy)` → returns `(router_addr, amount_out)`
  - `get_amount_in(token, amount_out, is_buy)` → returns `(router_addr, amount_in)`

- **Curve info**

  - `get_curves(token)` → returns 8 numbers (reserves, k, etc.)
  - `is_listed(token)` → `True/False`

- **Trades**

  - `buy(router_addr, token_addr, to_addr, amount_in, amount_out_min)`
  - `sell(router_addr, token_addr, to_addr, amount_in, amount_out_min)`

---

## Requirements

- Python **3.11+** (CPython or PyPy)
- Packages: `web3`, `eth-account`, `eth-abi`, `eth-utils`, `python-dotenv` (for examples)

---

## Install

```bash
# (optional) create venv
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -U pip
pip install web3 eth-account eth-abi eth-utils python-dotenv
```

---

## Project layout (example)

```
your-project/
  src/
    nadfun_sdk/
      __init__.py
      router.py
      abi_loader.py
      constants.py        # must define: wrapperContractAddress, curveContractAddress
      abis/
        wrapper.json
        curve.json
        erc20Permit.json
  examples/
    buy.py
    sell.py
  .env
  README.md
```

`constants.py` must include the on-chain addresses:

```py
# src/nadfun_sdk/constants.py
wrapperContractAddress = "0x...."
curveContractAddress   = "0x...."
```

---

## .env file

Create a `.env` file in the project root:

```env
RPC_URL=https://your-rpc.example
PRIVATE_KEY=0xYOUR_PRIVATE_KEY
MY_ADDRESS=0xYourWalletAddress
```

---

## Quick start

```python
# examples/buy.py
from nadfun_sdk import NadfunSDK
from dotenv import load_dotenv
import os

load_dotenv()
RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MY_ADDRESS = os.getenv("MY_ADDRESS")

sdk = NadfunSDK(RPC_URL, PRIVATE_KEY)

TOKEN_ADDRESS = "0x62f0956153dD2261E97f32d505eE6aAca671D61e"  # example

print("\n=== BUY TEST ===")

amount_in_wei = 1 * 10**18  # 1 MON in wei

router_addr, amount_out = sdk.get_amount_out(TOKEN_ADDRESS, amount_in_wei, is_buy=True)
print(f"router_addr: {router_addr}")
print(f"amount_out: {amount_out}")

# 20% slippage
amount_out_min = int(amount_out * 0.8)

try:
    tx_hash = sdk.buy(router_addr, TOKEN_ADDRESS, MY_ADDRESS, amount_in_wei, amount_out_min)
    print(f"Buy tx_hash: {tx_hash}")
except Exception as e:
    print(f"Buy error: {e}")
```

```python
# examples/sell.py
from nadfun_sdk import NadfunSDK
from dotenv import load_dotenv
import os

load_dotenv()
RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MY_ADDRESS = os.getenv("MY_ADDRESS")

sdk = NadfunSDK(RPC_URL, PRIVATE_KEY)

TOKEN_ADDRESS = "0x62f0956153dD2261E97f32d505eE6aAca671D61e"  # example

print("\n=== SELL TEST ===")

amount_in_wei = 1_000_000 * 10**18  # 1,000,000 MEME (example)

router_addr, amount_out = sdk.get_amount_out(TOKEN_ADDRESS, amount_in_wei, is_buy=False)
print(f"router_addr: {router_addr}")
print(f"amount_out: {amount_out}")

# 20% slippage
amount_out_min = int(amount_out * 0.8)

try:
    tx_hash = sdk.sell(router_addr, TOKEN_ADDRESS, MY_ADDRESS, amount_in_wei, amount_out_min)
    print(f"Sell tx_hash: {tx_hash}")
except Exception as e:
    print(f"Sell error: {e}")
```

Run:

```bash
python examples/buy.py
python examples/sell.py
```

---

## How it works (short)

- The SDK creates a Web3 client with your `RPC_URL`.
- Your private key is loaded only in your process; transactions are **signed locally**.
- Gas:

  - uses `w3.eth.gas_price` (legacy) and fixed gas limits:

    - buy: `261000`
    - sell: `232000`

- Deadline: current time + 300 seconds.

If you need to change gas:

```py
# router.py
tx['gas'] = 261000  # adjust here
tx['gasPrice'] = self.w3.eth.gas_price  # or set your own number
```

---

## API (very short)

```py
sdk = NadfunSDK(rpc_url, private_key)

# quotes
router, out_amt = sdk.get_amount_out(token, amount_in, is_buy=True)   # returns tuple
router, in_amt  = sdk.get_amount_in(token, amount_out, is_buy=False)

# curve info
tuple8 = sdk.get_curves(token)
listed = sdk.is_listed(token)  # bool

# trades
tx_hash = sdk.buy(router, token, to, amount_in, amount_out_min)
tx_hash = sdk.sell(router, token, to, amount_in, amount_out_min)
```

**Notes**

- All token amounts are **wei**.
- `is_buy=True` means spending native coin (e.g., MON) to buy tokens.
- Addresses must be **checksum** (SDK converts with `to_checksum` internally).

---

## Troubleshooting

- `RPC connection failed` → check `RPC_URL` and network.
- `insufficient funds` → your wallet needs native coin for gas / buy value.
- `replacement fee too low` → raise `gasPrice`.
- Wrong token/router → always use `get_amount_out / get_amount_in` first; pass the returned **router address** into `buy/sell`.

---

## License

MIT (or your project’s license)
