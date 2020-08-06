def no_dups(s):
    # Your code here
    d = {}
    stringArr = s.lower().split()
    newStr = ""

    for word in stringArr:
        if word not in d:
            d[word] = True
            newStr += f"{word} "

    return newStr.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))