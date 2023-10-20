#20221576 김시온
korean = ('정렬', '초보자', '내포', '사전')
english = ('sorting', 'novice', 'comprehension', 'dictionary')

matching = input('찾을 단어 입력 >> ')
if matching in korean:
    print(english[korean.index(matching)])
else:
    print("단어가 존재하지 않습니다.")




