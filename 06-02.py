company = {'삼성에스디에스': 242000, '삼성전자': 47000, '엔씨소프트': 52600, '핸디소프트': 5120, '골프존': 215000, '기아': 56300}
while True:
    choice = input('주식 이름 ? ')
    if choice in company:
        print('%s: %d' % (choice, company[choice]))
        print()
    else:
        print('주식 이름이 없습니다.')
        break