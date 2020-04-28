found = len(set(needles) & set(haystack))

# another way:
found = len(set(needles).intersection(haystack))
