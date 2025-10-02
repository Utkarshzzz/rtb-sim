# my_strategy.py
class ThresholdBidder:
    def __init__(self, base_bid=50, max_bid=100):
        self.base_bid = base_bid
        self.max_bid = max_bid

    def bid(self, user_score: float) -> float:
        """
        Simple heuristic: bid = base_bid * user_score, capped at max_bid.
        user_score is between 0.0 and 1.0.
        """
        bid_value = self.base_bid * user_score
        return min(bid_value, self.max_bid)
