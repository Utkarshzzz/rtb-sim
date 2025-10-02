# Real-Time Bidding (RTB) Simulator — Prototype 

### Overview
Designed a **prototype of a Real-Time Bidding (RTB) system** inspired by programmatic advertising platforms.  
Implemented a simple **Threshold Bidder strategy** and an **auction evaluator** to simulate second-price auctions.

This aligns with my resume project:
*“Built a scalable, low-latency simulation of an RTB system inspired by programmatic advertising platforms.”*

---

### Tech Stack
- **Language**: Python 3  
- **Libraries**: Random, Statistics (standard library)  
- **Concepts**: Concurrency in bidding, second-price auctions, ad-tech latency constraints

---

### Concepts Demonstrated
- **Auction Logic**: Highest bid wins, winner pays the second-highest price.  
- **Bidder Strategy**: Threshold-based bidding (`base × user_score`, capped by `max_bid`).  
- **Evaluation**: Measures **win rate** and **average clearing price** across N auctions.  

---

### Files
- `my_strategy.py` → Implements `ThresholdBidder` strategy.  
- `evaluate.py` → Runs N auctions, prints win rate & avg clearing price.  
- `results.txt` (optional) → Example simulation output.  

---

### How to Use
```bash
python evaluate.py
