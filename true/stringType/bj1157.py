# 문제 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 다양한 패키지를 사용하면 짧게 코드를 작성가능하다.
# from collections import Counter
# word = input().upper()
# cnt = Counter(word).most_common()
# if(cnt[0][1] == cnt[1][1]):
# 	print('?')
# else:
# 	print(cnt[0][0])

# 다른사람이 한것 짧게
# import sys
# from collections import Counter
# sCnt = Counter(sys.stdin.readline().rstrip('\n').upper())
# arr = [i for i in sCnt.keys() if sCnt[i] == max(sCnt.values())]
# print('?' if len(arr) > 1 else arr[0])

# 정석으로
word = input().upper()
uniq_word = list(set(word))
cnt_list = []
for i in uniq_word:
	cnt = word.count(i)
	cnt_list.append(cnt)
if cnt_list.count(max(cnt_list)) > 1:
	print("?")
else:
	max_index = cnt_list.index(max(cnt_list))
	print(uniq_word[max_index])