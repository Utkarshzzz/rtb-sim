# RTB Auction Simulator 

This is a small **prototype / learning implementation** inspired by `amazon-science/auction-gym` (link: https://github.com/amazon-science/auction-gym).

## What I added
- `my_strategy.py` — `ThresholdBidder`: bids = base_bid * user_score, capped at max_bid.
- `evaluate.py` — runs N simulated auctions (second-price logic), prints:
  - Win rate
  - Average clearing price

## How to view (no runtime artifacts here)
Files are visible in this repo. This is a demo implementation prepared to explain auction logic and bidding strategy

