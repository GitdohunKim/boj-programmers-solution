def solution(participant, completion):
    participant_dict = {}  # 이름과 개수를 저장할 딕셔너리
    
    # 참가자 명단을 딕셔너리로 변환하여 이름과 개수를 저장합니다.
    for name in participant:
        if name in participant_dict:
            participant_dict[name] += 1
        else:
            participant_dict[name] = 1
    
    # 완주한 선수들을 딕셔너리에서 빼줍니다.
    for name in completion:
        participant_dict[name] -= 1
    
    # 남은 선수가 완주하지 못한 선수입니다.
    for name, count in participant_dict.items():
        if count > 0:
            answer = name
            break
    
    return answer
