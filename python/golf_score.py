import sys

def regulation_strokes_check(list_regulation_strokes):
    if len(list_regulation_strokes) != 18:
        print("入力する数値の個数は18個です。")
        sys.exit(1)  # プログラムを終了する
    new_regulation_strokes_list = [ v for v in list_regulation_strokes if v >=3 and v <=5 ]
    if len(list_regulation_strokes) !=  len(new_regulation_strokes_list):
        print("入力できる値は3~5です。")
        sys.exit(1)  # プログラムを終了する

def actual_strokes_check(list_actual_strokes):
    if len(list_actual_strokes) != 18:
        print("入力する数値の個数は18個です。")
        sys.exit(1)  # プログラムを終了する
    new_actual_strokes_list = [ v for v in list_actual_strokes if v >= 1 ]
    if len(list_actual_strokes) !=  len(new_actual_strokes_list):
        print("入力できる値は1以上です。")
        sys.exit(1)  # プログラムを終了する

def score_judge(regulation_strokes, actual_strokes ,score_list):
    for v1,v2 in zip(regulation_strokes, actual_strokes):
        diff = v1-v2

        if diff == 0:
            score_list.append("パー")
        elif diff == 1:
            score_list.append("バーディ")
        elif diff == 2:
            if v1 == 3 or v2 == 1:
                score_list.append("ホールインワン")
            else:
                score_list.append("イーグル")
        elif diff == 3:
            if v1 == 4:
                score_list.append("ホールインワン")
            else:
                score_list.append("アルバトロス")
        elif diff == 4 and v1 == 5:
                score_list.append("コンドル")
        elif v2 == 1:
            score_list.append("ホールインワン")
        elif diff == -1:
            score_list.append("ボギー")
        else:
            score_list.append(f"{v2-v1}ボギー")


if __name__ == "__main__":
    regulation_strokes = list(map(int, input().split(',')))
    actual_strokes = list(map(int, input().split(',')))
    regulation_strokes_check(regulation_strokes)
    actual_strokes_check(actual_strokes)

    score_list=[]
    score_judge(regulation_strokes, actual_strokes ,score_list)

    print(score_list)

