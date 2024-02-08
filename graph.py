import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from main import graph_data_buy, graph_data_sell, graph_data_time


def data_graph(coin):
    buy = graph_data_buy(coin)
    sell = graph_data_sell(coin)
    date = graph_data_time(coin)


    plt.figure(figsize=(9, 4))

    plt.plot(date, buy,'-go')
    plt.plot(date, sell,'-ro')
    plt.yticks(np.arange(4000, 9000, step=1000))
    plt.grid()
    plt.xlabel("Время")
    plt.ylabel("Стоимость, $")
    plt.savefig(f"graphs/{coin}_usd.png")

def data_graph_delete(coin):
    os.remove(f"graphs/{coin}_usd.png")


