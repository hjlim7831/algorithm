import collections
import heapq

def solution(genres, plays):
    db = collections.defaultdict(list)
    genre_db = collections.defaultdict(int)
    for idx, item in enumerate(zip(genres, plays)):
        genre, play = item
        db[genre].append((idx, play))
        genre_db[genre] += play

    heap = []
    for genre in genre_db:
        heapq.heappush(heap, (-genre_db[genre], genre))
    
    answer = []
    while heap:
        _, genre = heapq.heappop(heap)
        genre_list = db[genre]
        genre_list.sort(key=lambda x:(x[1], -x[0]))
        answer.append(genre_list.pop()[0])
        if genre_list:
            answer.append(genre_list.pop()[0])
            
    return answer