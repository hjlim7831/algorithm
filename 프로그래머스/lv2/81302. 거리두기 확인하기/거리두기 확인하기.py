from itertools import combinations

def solution(places):
    answer = []
    for idx, place in enumerate(places):
        ans_idx = 1
        print(idx)
        people = []
        # 사람 위치 구하기
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    people.append((r, c))
        for p1, p2 in combinations(people, 2):
            # 두 사람 사이의 거리 구하기
            dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            # print("dist:",dist)
            # [1] 거리 2 초과 : 거리두기 성공
            if dist > 2:
                continue
            # [2] 거리 2 미만 : 거리두기 실패
            # 바로 옆에 붙어있음!
            elif dist < 2:
                ans_idx = 0
                break
            # [3] 거리가 2인 경우 : 케이스 따지기
            else:
                # 직선으로 있는 경우
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    # 사이에 있는 공간이 파티션이어야 함
                    ir, ic = (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2
                    if place[ir][ic] != "X":
                        # print("case 1")
                        # print(p1, p2)
                        ans_idx = 0
                        break                    
                # 대각선에 있는 경우
                else:
                    if place[p1[0]][p2[1]] != "X":
                        # print("case 3")
                        # print(p1, p2)
                        ans_idx = 0
                        break
                    if place[p2[0]][p1[1]] != "X":
                        # print("case 4")
                        # print(p1, p2)
                        ans_idx = 0
                        break
                        
        answer.append(ans_idx)
        
    return answer