import urllib.request
import re  # Add this import
import nltk
from collections import defaultdict, Counter
import string
import matplotlib.pyplot as plt

url = 'https://www.gutenberg.org/cache/epub/730/pg730.txt'
try:
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        print(text)  # for testing
except Exception as e:
    print("An error occurred:", e)

###Part 2 Processing the Text

#Cleaning the Text

start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

if start_marker in text and end_marker in text:
    main_text = text.split(start_marker)[1]        # Everything after the start marker
    main_text = main_text.split(end_marker)[0]     # Everything before the end marker
    cleaned_text = main_text.strip()               # Remove leading/trailing whitespace
else:
    cleaned_text = text

print(cleaned_text)

#Lowercase the Text

lowercase_text = cleaned_text.lower()
print(lowercase_text)

#removing stop words 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords  # Uncomment this line
import string

stop_words = set(stopwords.words('english'))

# Remove punctuation & split into words
translator = str.maketrans('', '', string.punctuation)
words = lowercase_text.translate(translator).split()

# Filter out stop words
filtered_words = [word for word in words if word not in stop_words]

#3. Word Frequency Analysis

from collections import Counter

word_counts = Counter(filtered_words)
print(word_counts.most_common(20))  # Top 20 most frequent words

#4. Text Statistics

# Top 10 most frequent words
top_10 = word_counts.most_common(10)

# Average word length
avg_word_length = sum(len(word) for word in filtered_words) / len(filtered_words)

# Sentence statistics (basic splitting, could be improved)
sentences = cleaned_text.split('.')  # crude split on periods
avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)

# Document statistics
total_words = len(filtered_words)
unique_words = len(set(filtered_words))
vocab_richness = unique_words / total_words

print("Top 10 words:", top_10)
print(f"Average word length: {avg_word_length:.2f}")
print(f"Average sentence length: {avg_sentence_length:.2f} words")
print(f"Vocabulary richness: {vocab_richness:.4f}")

#5. Data Visualization

import matplotlib.pyplot as plt

top_words, top_counts = zip(*top_10)
plt.figure(figsize=(10,6))
plt.bar(top_words, top_counts)
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words')
plt.show()

# --- 6. Concordance (word -> sentences that contain it) + Collocations (bigrams/trigrams) ---

# 6A) Sentence split (simple, in-scope)
sentences = [s.strip() for s in re.split(r'[.!?]+', cleaned_text) if s.strip()]

# Normalize sentences to word lists (lowercase, no punctuation)
punct_trans = str.maketrans('', '', string.punctuation)
sent_words = [
    [w for w in s.lower().translate(punct_trans).split() if w and w not in stop_words]
    for s in sentences
]

# Build a concordance: word -> sorted unique sentence indices
concordance = defaultdict(set)
for i, ws in enumerate(sent_words):
    for w in ws:
        concordance[w].add(i)

# Helper to inspect a term’s occurrences (prints a few sentences around matches)
def show_concordance(term, k=3):
    term = term.lower()
    idxs = sorted(concordance.get(term, []))
    print(f"'{term}' occurs in {len(idxs)} sentences.")
    for j, i in enumerate(idxs[:k], start=1):
        left = sentences[max(0, i-1)]
        mid  = sentences[i]
        right = sentences[min(len(sentences)-1, i+1)]
        print(f"\nMatch {j} (sentence {i}):")
        print(f"... {left[-120:]}." if left else "")
        print(f">>> {mid[:300]}.")
        print(f"{right[:120]} ..." if right else "")

# Try it:
# show_concordance("whale")
# show_concordance("captain")

# 6B) Collocations with tuples (bigrams & trigrams) using your filtered_words
bigrams  = list(zip(filtered_words, filtered_words[1:]))
trigrams = list(zip(filtered_words, filtered_words[1:], filtered_words[2:]))

bigram_counts  = Counter(bigrams).most_common(20)
trigram_counts = Counter(trigrams).most_common(20)

print("\nTop 20 bigrams:")
for (w1, w2), c in bigram_counts:
    print(f"{w1} {w2}: {c}")

print("\nTop 20 trigrams:")
for (w1, w2, w3), c in trigram_counts:
    print(f"{w1} {w2} {w3}: {c}")

# 6C) Quick visualization of bigrams (still in basic matplotlib territory)
top_bi, top_bi_counts = zip(*bigram_counts[:15])
labels = [' '.join(b) for b in top_bi]

plt.figure(figsize=(12,6))
plt.bar(labels, top_bi_counts)
plt.xticks(rotation=45, ha='right')
plt.title('Top 15 Bigrams (Stopwords removed)')
plt.tight_layout()
plt.show()

