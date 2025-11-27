from itertools import combinations
from collections import Counter

# Step 1: Define the deck of cards
ranks = ['6','7','8','9','10','J','Q','K','A']
suits = ['H','D','C','S']
deck = [r+s for r in ranks for s in suits]  # 36 cards total

# Step 2: Map ranks to numeric values for easy straight detection
rank_map = {r: i for i, r in enumerate(ranks)}

# Step 3: Function to check if ranks form a straight
def is_straight(ranks_in_hand):
    vals = sorted(rank_map[r] for r in ranks_in_hand)
    return all(vals[i] + 1 == vals[i + 1] for i in range(len(vals) - 1))

# Step 4: Function to classify a 5-card hand
def classify(hand):
    suits = [c[-1] for c in hand]
    ranks_in_hand = [c[:-1] for c in hand]
    counts = sorted(Counter(ranks_in_hand).values(), reverse=True)

    flush = len(set(suits)) == 1
    straight = is_straight(ranks_in_hand)

    if flush and straight:
        return "Straight Flush"  # Five consecutive cards, all same suit
    if counts == [4, 1]:
        return "Four of a Kind"  # Four cards of the same rank
    if counts == [3, 2]:
        return "Full House"      # Three of a kind plus a pair
    if flush:
        return "Flush"           # All five cards same suit, not consecutive
    if straight:
        return "Straight"        # Five consecutive cards, different suits
    if counts == [3, 1, 1]:
        return "Three of a Kind" # Three cards of the same rank
    if counts == [2, 2, 1]:
        return "Two Pair"        # Two different pairs
    if counts == [2, 1, 1, 1]:
        return "One Pair"        # One pair of cards with same rank
    return "High Card"           # None of the above, highest card wins

# Step 5: Initialize counters and descriptions for each hand category
total = 0
counts = {
    "Straight Flush": 0,  # Five consecutive cards, all same suit
    "Four of a Kind": 0,  # Four cards of the same rank
    "Full House": 0,      # Three of a kind plus a pair
    "Flush": 0,           # All five cards same suit, not consecutive
    "Straight": 0,        # Five consecutive cards, different suits
    "Three of a Kind": 0, # Three cards of the same rank
    "Two Pair": 0,        # Two different pairs
    "One Pair": 0,        # One pair of cards with same rank
    "High Card": 0        # None of the above, highest card wins
}

descriptions = {
    "Straight Flush": "Five consecutive cards, all same suit",
    "Four of a Kind": "Four cards of the same rank",
    "Full House": "Three of a kind plus a pair",
    "Flush": "All five cards same suit, not consecutive",
    "Straight": "Five consecutive cards, different suits",
    "Three of a Kind": "Three cards of the same rank",
    "Two Pair": "Two different pairs",
    "One Pair": "One pair of cards with same rank",
    "High Card": "None of the above, highest card wins"
}

# Step 6: Generate and classify all possible 5-card hands
for hand in combinations(deck, 5):
    category = classify(hand)
    counts[category] += 1
    total += 1

# Step 7: Output results with descriptions
print(f"Total outcomes (5-card hands): {total}")
print("\nEvents (hand categories), their descriptions, and probabilities:\n")
for category, count in counts.items():
    probability = count / total
    print(f"{category:<15}: {count:>6} outcomes | Probability: {probability:.6f} | {descriptions[category]}")
