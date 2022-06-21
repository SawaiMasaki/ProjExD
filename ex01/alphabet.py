import random
import datetime
global ob_alpha, los_alpha
    
ob_alpha = 9   #対象文字数
los_alpha = 2  #欠損文字数
num_try = 5    #最大試行回数

def main():
    start = datetime.datetime.now()
    for i in range(num_try):
        seikai = quiz()
        if ans(seikai) == 0:
            print("完全正解！. おめでとう！")
            end = datetime.datetime.now()
            print(f"{(end - start).seconds}秒です")
            break

#出題する関数
def quiz():  
    alphabet = [chr(num+65) for num in range(26)]
    alphabets = random.sample(alphabet, ob_alpha)
    print("対象文字：")
    for i in alphabets:
        print(i, end=" ")

    #print("\n欠損文字：")
    los_alphabets = random.sample(alphabets, los_alpha)
    #for j in los_alphabets:
    #    print(j, end=" ")

    print("\n表示文字：")
    for k in los_alphabets:
        alphabets.remove(k)

    random.shuffle(alphabets)
    for l in alphabets:
        print(l, end=" ")

    return los_alphabets

#解答する関数
def ans(seikai):
    flag = 0
    num = int(input("\n欠損文字はいくつあるでしょうか？："))
    if num != los_alpha:
        print("不正解です.")

    else:
        print("正解です. それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(los_alpha):
            ans = input(f"{1+i}つ目の文字を入力してください：")
            if ans not in seikai:
                print("不正解です.またチャレンジしてください")
                flag = 1
                break
    return flag       

if __name__ == "__main__":
    main()