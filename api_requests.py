import requests

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

    #with open("fails/info.txt", 'w') as file:
    data = list(response.json()["pairs"])
    data_up = list()

    for i in range(len(data)):
        if "_usd" in data[i]:
            data_up.append(data[i])

        #file.write(str(data_up))
    
    return data_up

def get_ticker(coin):

    #response = requests.get(url="https://yobit.net/api/3/ticker/eth_btc-xrp_btccc?ignore_invalid=1")
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin}?ignore_invalid=1")    

    #with open("fails/ticker.txt", 'w') as file:
        #file.write(response.text)

    ticker = [round(response.json()[f"{coin}"]["avg"], 2), round(response.json()[f"{coin}"]["vol"], 2)]

    return ticker

def get_depth(coin1="btc", coin2="usd", limit=150):
    response= requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

    with open("fails/depth.txt", 'w') as file:
        file.write(response.text)
    
    bids = response.json()[f"{coin1}_usd"]["bids"]

    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount=item[1]

        total_bids_amount += price * coin_amount

    return f"Total bids: {total_bids_amount} $"


def get_trades(coin, limit=2000):
    response = requests.get(url= f"https://yobit.net/api/3/trades/{coin}?limit={limit}&ignore_invalid=1")

    # with open("fails/trades.txt", 'w') as file:
    #     file.write(response.text)

    total_trade_ask = 0
    total_trade_bid = 0

    for item in response.json()[f"{coin}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]
        else:
            total_trade_bid += item["price"] * item["amount"]

    info = f"[-] TOTAL {coin} SELL: {round(total_trade_ask, 2)} $\n[+] TOTAL {coin} BUY: {round(total_trade_bid, 2)} $"

    trades = [round(total_trade_ask, 2), round(total_trade_bid, 2)]
    return trades

