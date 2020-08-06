import re

def word_count(s):
    # Your code here
    d = {}

    fixedString = re.sub('["\\:\\;\\,\\.\\-\\+\\=\\/\\\\\|\\[\\]\\{\\}\\(\\)\\*\\^\\&]', '', s).lower().split()

    for word in fixedString:
        if word not in d:
            d[word] = 0

        d[word] += 1

    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))