def solution(players, callings):
    p_dict = {}
    rank_dict = {}
    for i in range(len(players)):
        p_dict[players[i]] = i + 1
        rank_dict[i + 1] = players[i]
    
    for call in callings:
        call_rank = p_dict[call]
        for_rank = call_rank -1
        for_pl = rank_dict[for_rank]
        p_dict[call] = for_rank
        p_dict[for_pl] = call_rank
        rank_dict[for_rank] = call
        rank_dict[call_rank] = for_pl
    
    end_players = []
    for i in range(1, len(players) + 1):
        end_players.append(rank_dict[i])
    
    
    return end_players