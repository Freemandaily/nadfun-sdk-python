"""
Real-time bonding curve event monitoring
"""

import asyncio
import os
from nadfun_sdk.stream import CurveStream, EventType
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Configuration
    ws_url = os.getenv("WS_URL")
    
    print("Bonding Curve Event Stream")
    print(f"WebSocket URL: {ws_url}")
    
    # Initialize stream
    stream = CurveStream(ws_url)
    stream.subscribe([EventType.BUY,EventType.SELL])
    
    print("-" * 50)
    print("Listening for events...")
    
    # Subscribe and process events
    async for event in stream.events():
        print(f"Event: {event['eventName']}")
        print(f"BlockNumber: {event['blockNumber']}")
        print(f"Token: {event['token']}")
        print(f"Amount In: {event['amountIn']}")
        print(f"Amount Out: {event['amountOut']}")
        print(f"Tx: {event['transactionHash']}")
        print("-" * 50)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStream stopped by user")