# 给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？输出需要删除的字符个数。

# abcda->2
# google->2

def find_seq(a, b):
    result = ''
    index = 0
    for i in a:
        find_index = b.find(i, index)
        if find_index != -1:
            result = result + b[find_index]
            index = find_index + 1
    return result

def solution():
    try:
        while True:
            s = list(input())
            rev = list(reversed(s))
            
            res = find_seq(''.join(s), ''.join(rev))
            print(len(s) - len(res))

    except EOFError:
        pass

solution()