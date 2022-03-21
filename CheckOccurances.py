lis = [0,0,1,1,1,1,2,3,4,5,6,7,8,9,0,0]
print(len(lis))
n = len(lis)
ans = [i for i in list(dict.fromkeys(lis)) if (lis.count(i)/n)*100 == 25.0]
print(ans)