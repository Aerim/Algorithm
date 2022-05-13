def solution(citations):
    answer = 0

    citations = sorted(citations)

    for h in range(len(citations)):
        # 현재 인덱스 값이 인용 횟수보다 크면
        # 배열안에서 현재 인덱스 값보다 원소 갯수
        if citations[h] >= len(citations) - h:
            return len(citations) - h
    return 0