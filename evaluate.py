# evaluate.py
from my_strategy import ThresholdBidder
import random
import statistics

def simulate_auction(runs=1000):
    bidder = ThresholdBidder()
    wins = 0
    prices = []
    for _ in range(runs):
        user_score = random.random()
        my_bid = bidder.bid(user_score)
        competitor_bid = random.uniform(10, 100)
        if my_bid > competitor_bid:
            wins += 1
            prices.append(competitor_bid)
    win_rate = wins / runs
    avg_price = statistics.mean(prices) if prices else 0
    return win_rate, avg_price

if __name__ == "__main__":
    wr, ap = simulate_auction(10000)
    print(f"Win rate: {wr:.4f}, Avg clearing price: {ap:.2f}")
