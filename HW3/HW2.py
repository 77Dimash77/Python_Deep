from collections import Counter
import re


def get_most_common_words(text, n=10):
    text = re.sub(r'[^\w\s]', '', text.lower())

    words = text.split()

    word_counts = Counter(words)

    return word_counts.most_common(n)


text = """
Python is an interpreted high-level general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. 
Python is often described as a "batteries included" language due to its comprehensive standard library.
"""

most_common_words = get_most_common_words(text)
print(most_common_words)
