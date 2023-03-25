
import sys
from collections import Counter

input_str = sys.stdin.readline().lower().strip()

# if (len(input_str) == 1):
#     print(input_str[0].upper())
# else:
#     char_counter = list(Counter(input_str).items())
#     char_counter.sort(key=lambda x: (-x[1]))
#     if (char_counter[0][1] == char_counter[1][1]):
#         print("?")
#     else:
#         print(char_counter[0][0].upper())

# refactored
if (len(input_str) == 1):
    print(input_str.upper())
else:
    char_counter = Counter(input_str)
    first, second = char_counter.most_common(2)  # 가장 자주 등장한 단어 1, 2등
    if (first[1] == second[1]):
        print("?")
    else:
        print(first[0].upper())
