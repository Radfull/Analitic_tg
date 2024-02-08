import sqlite3
import time
from threading import Timer
from api_requests import *


def list_stab(data):
    lis = list()
    for i in range(len(data)):
        lis.append(data[i][0])
    return lis

def write_data():



    pairs = get_info()

    for i in range(len(pairs)):
        print(f"{i} из {len(pairs)}")
        try:
            ticker = get_ticker(pairs[i])
            trades = get_trades(pairs[i])

            connection = sqlite3.connect("pars.db")
            cursor = connection.cursor()
            cursor.execute(f'''
            INSERT INTO {pairs[i]} (date,avg, vol, buy, sell)
            VALUES (CURRENT_TIMESTAMP,?, ?, ?, ?)
            ''', (ticker[0], ticker[1], trades[0], trades[1]))
            connection.commit()
            connection.close()
        except:
            continue



def create_data():

    connection = sqlite3.connect("pars.db")
    cursor = connection.cursor()
    pairs = get_info()

    for i in range(len(pairs)):

        try:
            cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {pairs[i]} (
            date TIMESTAMP,
            avg REAL,
            vol REAL,
            buy INTEGER,
            sell INTEGER
            )
            ''')
        except sqlite3.OperationalError:
            print(pairs[i], " Error")

    connection.commit()
    connection.close() 

def graph_data_buy(coin):

    connection = sqlite3.connect("pars.db")
    cursor = connection.cursor()
    buy = [list(i) for i in cursor.execute(f'''
    SELECT buy
    FROM {coin}_usd
    ORDER BY date DESC
    LIMIT 10
    ''')]
    connection.commit()
    connection.close()
    buy = list_stab(buy)
    return buy

    # connection = sqlite3.connect("pars.db")
    # cursor = connection.cursor()
    # query = "SELECT TIME(date) FROM btc_usd ORDER BY date DESC LIMIT 10"
    # cursor.execute(query)
    # result = cursor.fetchall() #result = (1,2,3,) or  result =((1,3),(4,5),)
    # final_result = [list(i) for i in result]
    # return final_result

def graph_data_sell(coin):

    connection = sqlite3.connect("pars.db")
    cursor = connection.cursor()
    sell = [list(i) for i in cursor.execute(f'''
    SELECT sell
    FROM {coin}_usd
    ORDER BY date DESC
    LIMIT 10
    ''')]
    connection.commit()
    connection.close()
    sell = list_stab(sell)
    return sell

def graph_data_time(coin):

    connection = sqlite3.connect("pars.db")
    cursor = connection.cursor()
    date = [list(i) for i in cursor.execute(f'''
    SELECT TIME(date)
    FROM {coin}_usd
    ORDER BY date DESC
    LIMIT 10
    ''')]
    connection.commit()
    connection.close()
    date = list_stab(date)
    return date[::-1]

def main():
    #print(get_info())
    #print(get_ticker())
    #print(get_ticker(coin1="eth"))
    #print(get_depth())

    # delay = 600

    # while True:
    #     write_data()
    #     time.sleep(delay)
    write_data()
    
    
if __name__ == "__main__":

    main()

write_data()
