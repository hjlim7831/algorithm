import java.util.*;
import java.io.*;
import java.lang.*;

class Solution {
    static int ans_cnt = 0;
    static int ans_purc = 0;
    
    public int[] solution(int[][] users, int[] emoticons) {
        int l = emoticons.length;
        search_emo(new int[users.length], users, emoticons, 0, l);
        int[] answer = new int[]{ans_cnt, ans_purc};
        return answer;
    }
    
    public static void search_emo(int[] tot_purc, int[][] users, int[] emoticons, int d, int l) {
        if (d == l) {
            int cnt = 0, purc = 0;
            for (int j = 0; j < users.length; j++) {
                if (tot_purc[j] >= users[j][1]) {
                    cnt++;
                } else {
                    purc += tot_purc[j];
                }
            }
            if (cnt > ans_cnt) {
                ans_cnt = cnt;
                ans_purc = purc;
            } else if (cnt == ans_cnt && purc > ans_purc) {
                ans_purc = purc;
            }
            return;
        }

        int value = emoticons[d];

        for (int i = 1; i <= 4; i++) {
            int[] update_purc = tot_purc.clone();
            double disc_val = value * (1 - 0.1 * i);
            for (int j = 0; j < users.length; j++) {
                if (i * 10 >= users[j][0]) {
                    update_purc[j] += disc_val;
                }
            }
            search_emo(update_purc, users, emoticons, d+1, l);
        }
    }
}