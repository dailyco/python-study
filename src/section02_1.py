# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

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