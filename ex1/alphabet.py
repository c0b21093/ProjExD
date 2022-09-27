import random
import copy
import time

if __name__ == "__main__":
    a=0
    b=0
    trynum=2
    num = 5
    denum = 2
    alList=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while a==0 and trynum>b:
        ansList=list(random.sample(alList,num))
        quizList=list(random.sample(ansList,num-denum))
        disList=copy.copy(ansList)
        for i in quizList:
            if i in quizList:
                disList.remove(i)
        print("対象文字")
        print(ansList)
        print("表示文字")
        print(quizList)
        st = time.perf_counter()
        print("欠落文字")
        print(disList)
        totalans=input("欠損文字はいくつあるでしょうか？：")
        if totalans==str(denum):
            for i in range(denum):
                ans=input(str(i+1)+"つ目の文字を入力してください")
                if ans in ansList:
                    ansList.remove(ans)
            if len(ansList)==3:
                print("正解！")
                a=True
                ed = time.perf_counter()
            else:
                print("不正解です。またチャレンジしてください")
                ed = time.perf_counter()
            print(ed-st)
            b+=1
            print("aaaaa")

    

