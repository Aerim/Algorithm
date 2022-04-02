def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for i in new_id:
        if i.isalpha() == True or i.isdigit() == True or i in ['_','-','.']:
            answer += i

    while '..' in answer :
        answer = answer.replace('..','.')

    if answer[0] == '.':
        if len(answer) -1 > 0:
            answer = answer[1:]
        else:
            answer = 'a'

    if answer[-1] == '.':
        if len(answer) -1 > 0:
            answer = answer[:-1]
        else:
            answer = 'a'

    if len(answer) == 0:
        answer += a

    if len(answer) >= 16:
        answer = answer[:15]

        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:

        while len(answer) < 3:
            answer += answer[-1]

    return answer