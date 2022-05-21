def solution(n, words):
    answer = []

    _word = []
    _word.append(words[0])
    prev = words[0]

    # 번호,차례
    for w in range(1,len(words)):

        if words[w] not in _word:
            if prev[-1] == words[w][0]:
                _word.append(words[w])
                prev = words[w][-1]
            else:
                if (w + 1) % n == 0:
                    num = n
                else:
                    num = (w + 1) % n
                return [num, w // n + 1]
        else:
            if (w + 1) % n == 0:
                num = n
            else:
                num = (w + 1) % n
            return [num, w // n + 1]        

    return [0,0]