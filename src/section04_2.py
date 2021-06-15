# Section04-2
# 문자열, 문자열연산, 슬라이싱
# 문자열 함수 참조 : https://www.w3schools.com/python/python_ref_string.asp

# 문자열 길이
str1 = 'I am girl.'
str2 = "dailyco"
str3 = ''
str4 = str()
str5 = str('acb')

print(len(str1), len(str2), len(str3), len(str4), len(str5)) # 9 7 0 0 3

print()

# 이스케이프 문자 사용
escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'
escape_str5 = "Tab\tTab"

print(escape_str1) # Do you have a "big collection"?
print(escape_str2) # What's on TV?
print(escape_str3) # What's on TV?
print(escape_str4) # This is a "book".
print(escape_str5) # Tab Tab

print()

# Raw String
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

print(raw_s1) # C:\Programs\python3\"
print(raw_s2) # \\a\b\c\d
print(raw_s3) # \'"
print(raw_s4) # \"'

print()

# 멀티라인
multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """

print(multi_str1) 
"""

    문자열
    멀티라인
    테스트
    
"""

print()

# 문자열 연산
str_o1 = "dailyco"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1) # dailycodailycodailyco
print(str_o1 + str_o2) # dailycoOrange
print(dir(str_o1)) 
"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
print('x' in str_o1) # False
print('i' in str_o1) # True
print('e' not in str_o2) # False
print('O' not in str_o2) # False

# 문자열 형 변환
print(type(str(77)))  # <class 'str'>
print(str(10.4)) # 10.4
print(str(True)) # True
print(str(complex(12))) # (12+0j)

print()

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print(str_o1.capitalize()) # Dailyco (첫자 대문자)
print(str_o2.endswith("s")) # False (끝자 확인)
print(str_o1.join(["I'm ", "!"])) # I'm dailyco! (문자열 구분자와 합치기)
print(str_o1.replace('dai', 'week')) # weeklyco (문자열 대체)
print(str_o3.replace("is", "was", 3)) # thwas was string example....wow!!! thwas is really string (문자열 대체 수)
print(str_o4.split(' '))  # ['Kim', 'Lee', 'Park', 'Joo'] (문자열 분리)
print(sorted(str_o1))  # ['a', 'c', 'd', 'i', 'l', 'o', 'y'] (문자 정렬)
print(reversed(str_o2)) # <reversed object at 0x7f57941cd4c0>
print(list(reversed(str_o2))) # ['e', 'g', 'n', 'a', 'r', 'O'] (문자 거꾸로)

print()

# 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

print(str_sl[0:3]) # Nic (0~2 까지)
print(str_sl[:len(str_sl)]) # Niceboy (처음부터 끝까지)
print(str_sl[:len(str_sl) - 1]) # Nicebo (처음부터 하나 전까지)
print(str_sl[:]) # Niceboy (처음부터 끝까지)
print(str_sl[1:4:2]) # ie (1부터 3까지 2씩 뛰면서)
print(str_sl[-3:6]) # bo (뒤에서 세번째 부터 5까지)
print(str_sl[1:-2]) # iceb (1에서 뒤에서 세번째까지)
print(str_sl[::-1]) # yobeciN (처음부터 끝까지 뒤로 1씩 뛰면서)
print(str_sl[::2]) # Ncby (처음부터 끝까지 2씩 뛰면서)

print()

# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))
"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

# 출력
for i in im_str:
    print(i , end=' ')
# G o o d   B o y !

# im_str[0] = "T"  # 수정 불가(immutable) 
# TypeError: 'str' object does not support item assignment

# immutable 삭제
del str_sl

print()

# 아스키코드
a = 't'

print(ord(a)) # 116
print(chr(116)) # t