def solution(id_list, report, k):
    # dictionary 안에 set을 넣을까?
    report_dict = {}
    mail = {}
    for user_id in id_list:
        report_dict[user_id] = set()
        mail[user_id] = 0
    
    for re in report:
        user_id, report_id = re.split()
        report_dict[report_id].add(user_id)
    
    
    for user_id in id_list:
        # 해당 유저가 정지될 경우
        if len(report_dict[user_id]) >= k:
            # 신고했던 사람들에게 모두 메일 보내기
            for mail_id in report_dict[user_id]:
                mail[mail_id] += 1

    mail_ans = []
    for user_id in id_list:
        mail_ans.append(mail[user_id])
        
    
    
    return mail_ans