import random
import math
from collections import defaultdict

# -------------------------
# Step 1: Sample training text
# -------------------------
text = """
Language models are powerful tools for natural language processing.
They can generate new sentences based on previous words.
An n-gram model uses the previous n-1 words to predict the next word.
"""

# -------------------------
# Step 2: Preprocess text
# -------------------------
tokens = text.lower().replace('\n', ' ').split()
tokens = ['<s>'] + tokens + ['</s>']  # start and end tokens

# Choose n (2 for bigram, 3 for trigram)
n = 2

# -------------------------
# Step 3: Build n-gram counts
# -------------------------
ngrams = defaultdict(int)
contexts = defaultdict(int)

for i in range(len(tokens) - n + 1):
    ngram = tuple(tokens[i:i+n])
    context = tuple(tokens[i:i+n-1])
    ngrams[ngram] += 1
    contexts[context] += 1

# -------------------------
# Step 4: Compute conditional probabilities
# -------------------------
probs = {}
for ngram, count in ngrams.items():
    context = ngram[:-1]
    probs[ngram] = count / contexts[context]

# -------------------------
# Step 5: Text generation
# -------------------------
def generate_text(length=15):
    context = ('<s>',)
    result = []
    for _ in range(length):
        candidates = [ngram for ngram in probs if ngram[:-1] == context]
        if not candidates:
            break
        next_words = [ngram[-1] for ngram in candidates]
        next_probs = [probs[ngram] for ngram in candidates]
        next_word = random.choices(next_words, weights=next_probs)[0]
        if next_word == '</s>':
            break
        result.append(next_word)
        context = (next_word,)
    return ' '.join(result)

print("Generated Text:")
print(generate_text())

# -------------------------
# Step 6: Evaluate using Perplexity
# -------------------------
def calculate_perplexity(tokens, probs, n):
    N = 0
    log_prob_sum = 0
    for i in range(len(tokens) - n + 1):
        ngram = tuple(tokens[i:i+n])
        prob = probs.get(ngram, 1e-6)  # smoothing
        log_prob_sum += math.log(prob)
        N += 1
    perplexity = math.exp(-log_prob_sum / N)
    return perplexity

perplexity = calculate_perplexity(tokens, probs, n)
print(f"\nModel Perplexity: {perplexity:.4f}")
