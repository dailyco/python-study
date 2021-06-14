# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('Hello Python!') # Hello Python!
print("Hello Python!") # Hello Python!
print('''Hello Python!''') # Hello Python!
print("""Hello Python!""") # Hello Python!

print() # Enter

# Separator 옵션 사용
print('T', 'E', 'S', 'T') # T E S T (default: ' ')
print('T', 'E', 'S', 'T', sep='') # TEST
print('2021', '06', '14', sep='-') # 2021-06-14
print('dailyco', 'gmail.com', sep='@') # dailyco@gmail.com

# end 옵션 사용
print('Hello Python!') # Hello Python!\n (default: '\n' (줄바꿈))
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
# Welcome To the black parade piano notes\n

print() # Enter

# format 사용
print('{} and {}'.format('You', 'Me')) # You and Me
print('{0} and {1} and {0}'.format('You', 'Me')) # You and Me and You
print('{a} and {b}'.format(a='You', b='Me')) # You and Me

print("%s's favorite number is %d" % ('dailyco', 7)) # dailyco's favorite number is 7

# string format conversion
print('Test1: %5d, Price: %4.2f' % (776, 6534.123)) # Test1:   776, Price: 6534.12
print('Test1: {0: 5d}, Price: {1: 4.2f}'.format(776, 6534.123)) # Test1:   776, Price: 6534.12
print('Test1: {a: 5d}, Price: {b: 4.2f}'.format(a=776, b=6534.123)) # Test1:   776, Price: 6534.12

print() # Enter

# escape 코드
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...
"""

print("'you'") # 'you'
print('\'you\'') # 'you'
print('"you"') # "you"
print("""'you'""") # 'you'
print('\\you\\') # \you\
print('you\n\n') # you\n\n\n
print('\t\ttest') #         test