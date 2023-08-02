regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.
# 문자열이 정확히 저 형태여야 하는 경우이므로
# 시작(^)과 끝($)을 추가

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())