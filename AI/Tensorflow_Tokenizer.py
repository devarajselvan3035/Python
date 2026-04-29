import re


class SimpleTokenizer:
    def __init__(self, num_words=None, oov_token="<OOV>"):
        self.num_words = num_words
        self.oov_token = oov_token
        self.word_index = {}
        self.index_word = {}
        self.word_counts = {}

    def _clean_text(self, text):
        # Lowercase and remove punctuation using regex
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text

    def fit_on_texts(self, texts):
        """Creates the vocabulary based on a list of sentences."""
        for sentence in texts:
            cleaned = self._clean_text(sentence)
            words = cleaned.split()
            for word in words:
                self.word_counts[word] = self.word_counts.get(word, 0) + 1

        # Sort words by frequency (standard behavior)
        sorted_words = sorted(
            self.word_counts.items(), key=lambda x: x[1], reverse=True
        )

        # Add the Out-of-Vocabulary token at index 1
        self.word_index[self.oov_token] = 1
        self.index_word[1] = self.oov_token

        for i, (word, count) in enumerate(sorted_words, start=2):
            if self.num_words and i > self.num_words:
                break
            self.word_index[word] = i
            self.index_word[i] = word

    def texts_to_sequences(self, texts):
        """Converts sentences into lists of integers."""
        sequences = []
        for sentence in texts:
            cleaned = self._clean_text(sentence)
            words = cleaned.split()
            seq = [
                self.word_index.get(w, self.word_index[self.oov_token]) for w in words
            ]
            sequences.append(seq)
        return sequences


# Sample Data
sentences = [
    "I love machine learning!",
    "Machine learning is great.",
    "I love coding in Python.",
]

# Initialize and Train
tokenizer = SimpleTokenizer(oov_token="<UNK>")
tokenizer.fit_on_texts(sentences)

# Transform text to numbers
sequences = tokenizer.texts_to_sequences(sentences)

print(f"Word Index: {tokenizer.word_index}")
print(f"Sequences: {sequences}")
