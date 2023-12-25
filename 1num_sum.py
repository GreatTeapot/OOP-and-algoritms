def sum(li:list, target:int):
    result_li=[]
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]+li[j]==target:
                result_li.append([li[i],li[j]])
    return result_li

meanli=[2,3,1,5,6,7,0,2]
targe=3 
print(sum(meanli,targe))
