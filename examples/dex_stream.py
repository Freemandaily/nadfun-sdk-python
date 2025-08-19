"""
Real-time DEX swap monitoring
"""

import asyncio
import os
from nadfun_sdk.stream import DexStream
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Configuration
    ws_url = os.getenv("WS_URL")
    tokens = os.getenv("TOKENS")
    
    print("DEX Swap Event Stream")
    print(f"WebSocket URL: {ws_url}")
    
    # Initialize stream based on configuration
    stream = DexStream(ws_url)
    
    if tokens:
        # Subscribe to single token
        print(f"Subscribing to token: {tokens}")
        stream.subscribe_tokens(tokens)
    else:
        print("Please set TOKEN environment variable")
        return
    
    print("-" * 50)
    print("Listening for swap events...")
    
    # Subscribe and process events
    async for event in stream.events():
        print(f"Event: {event['eventName']}")
        print(f"BlockNumber: {event['blockNumber']}")
        print(f"Pool: {event['pool']}")
        print(f"Sender: {event['sender']}")
        print(f"Recipient: {event['recipient']}")
        print(f"Amount0: {event['amount0']}")
        print(f"Amount1: {event['amount1']}")
        print(f"Liquidity: {event['liquidity']}")
        print(f"Tick: {event['tick']}")
        print(f"Price (sqrt X96): {event['sqrtPriceX96']}")
        print(f"Tx: {event['transactionHash']}")
        print("-" * 50)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStream stopped by user")