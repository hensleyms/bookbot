def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    counts = {}
    for character in text:
        if character in counts:
         counts[character] = counts[character] + 1
        else:
           counts.update({character:1})
    return counts