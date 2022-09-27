from codecs import utf_16_be_decode
import random, time

def shutudai():
    questions = ['サザエの旦那の名前は？','カツオの妹の名前は？','タラオはカツオから見てどんな関係？']
    answers = [['マスオ', 'ますお'],['ワカメ','わかめ'],['甥','おい', '甥っ子', 'おいっこ']]

    set = random.randint(0,2)

    print("問題：\n" + questions[set] + "\n")
    start = time.time()

    return answers[set], start

def kaito(hikisu1):

    judg = 0

    answer = input("回答：")
    finish = time.time() - hikisu1[1]

    for correct in hikisu1[0]:
        if answer == correct:
            judg = 1
        else:
            pass

    return judg, finish

def main():

    hantei = kaito(shutudai())

    if hantei[0] == 1:
        print("正解！")
    elif hantei[0] == 0:
        print("不正解")

    print("経過時間")
    print(round(hantei[1]))

main()