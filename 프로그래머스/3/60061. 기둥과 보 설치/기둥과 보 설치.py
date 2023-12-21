def solution(n, build_frame):
    def frame(a):
        for x,y,b in a:
            case1 = [x-1,y,1]
            case2 = [x,y,1]
            case3 = [x,y-1,0]
            case4 = [x+1,y-1,0]
            case5 = [x+1,y,1]
            if b ==0:
                if y==0 or case1 in a or case2 in a or case3 in a:
                    continue
                return False
            elif b ==1:
                if case3 in a or case4 in a or (case1 in a and case5 in a):
                    continue
                return False
        return True
    answer = []
    for build in build_frame:
        x,y,b,c = build
        if c ==1:
            answer.append([x,y,b])
            if not frame(answer):
                answer.remove([x,y,b])
        if c==0:
            answer.remove([x,y,b])
            if not frame(answer):
                answer.append([x,y,b])
    return sorted(answer)