# # Solutions
# words = input("Enter Comma Seperated Sequence Of Words : ")
# listWords = words.split(',')
# listWords.sort()
# print(listWords)
# print(','.join(listWords))


transactions = [input() for i in range(5)]
deposit, withdraw = [], []
#print(transactions)
for t in transactions:
    if t.startswith('D'):
        deposit.append(int(t.split(" ")[1]))
    else:
        withdraw.append(int(t.split(" ")[1]))

print(f"Net Balance : {sum(deposit) - sum(withdraw)}")
