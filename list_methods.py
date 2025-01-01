fruits = ['banana','apple','guava']
flowers = ['lily','rose']
games = ['kho-kho','kancha']
fruits.extend(['grapes','raw_grapes'])
fruits.pop(0)
fruits.remove('apple')
fruits.extend(flowers)
fruits.append(games)

two_d_list = [
        [1,'ath'],[2,'aw'],[3,'waku'],
        [4,'kuku'],[5,'aw2'],[6,'ranchi']
]
for i in (two_d_list):
    for j in i:
        if j=='aw2':
            print(i)

    #insert(index, x)
print(games)
games.insert(1,'cricket')
print(games)