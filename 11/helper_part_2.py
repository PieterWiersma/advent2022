x = [3, 17, 11, 7, 5, 13, 19, 2]
#x = [23, 19, 13, 17]

for i in range(2,1000000000, 1):
     score = 0
     for j in x:
         if i % j == 0:
             score += 1

     if score == len(x):
         print(i)
         break
