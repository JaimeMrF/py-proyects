
def common_long_prefix(words):
    if not words:
        return ''
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return '*'
    return prefix
words = []
M = int(input())
while M > 0:
    M -= 1
    words.append(input().lower())
print(common_long_prefix(words))