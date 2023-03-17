from loader import binanceapi
from loader import okxapi
from loader import bybitapi
from loader import coinbaseapi
from loader import kucoinapi
from loader import dydxapi


import aiohttp
import asyncio 
import websockets
import time
from pprint import pp




class ARBITRX:

    binanceapi = binanceapi
    okxapi = okxapi
    bybitapi = bybitapi
    coinbaseapi = coinbaseapi
    kucoinapi = kucoinapi
    dydxapi = dydxapi
    
    
    SPREAD = 0.01

    def __init__(self): 
        self.EXCHANGES = [self.binanceapi, self.okxapi, self.bybitapi, self.coinbaseapi, self.kucoinapi, self.dydxapi]
    
    
    async def test(self, args):
        
        
        
        await self.binanceapi.websocket()
        
    # buy = 100
    # sell = 105
    # 
        
    
    # @staticmethod
    def check_spreed(self, orderbook): 
        res = []
        for book_ask in orderbook: 
            for book_bid in orderbook: 
                if book_ask['name'] == book_bid['name']: continue
                buy_price  = float(book_ask['asks'][0][0])
                sell_price = float(book_bid['bids'][0][0])
                print(buy_price)
                print(sell_price)
                spread = (sell_price*100/buy_price) - 100
                print(f"{book_ask['name']} to {book_bid['name']} spread: {spread:6f} %")
                    
                if spread >= self.SPREAD: 
                    res.append({"from":book_ask['name'], "to":book_bid['name'], 'spread': spread})
        return res
    
    
    async def main(self, args): 
        
        connections = set()
        connections.add('wss://api.foo.com:8765')
        connections.add('wss://api.bar.com:8765')
        connections.add('wss://api.foobar.com:8765')

        async def handle_socket(uri, ):
            async with websockets.connect(uri) as websocket:
                async for message in websocket:
                    print(message)

        async def handler():
            await asyncio.wait([handle_socket(uri) for uri in connections])

        asyncio.get_event_loop().run_until_complete(handler())
        
    #     for pair in WATCH_PAIR_CURRENCIES: 
    #         resp = await self.binanceapi.get_one_currency(s, 'BTCUSDT')
    #         pp(resp)
            
            
    # async def main(self, args): 
                    
    #     for pair in WATCH_PAIR_CURRENCIES: 
    #         resp = await self.binanceapi.get_one_currency(s, pair)
    #         print(pair)
    #         pp(resp)
            

    # def compare_pairs(self,total_usd): 
    #     ...

if __name__ == '__main__':
    API = ARBITRX()
    API.binanceapi.arm.run_function_with_exception(API.test, 'API', otladka=True)