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

def sorted_count(data):
    sorted_items_by_value = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items_by_value)