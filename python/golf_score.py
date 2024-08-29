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
    SCORE_MAPPING = {
        4: "コンドル",
        3: "アルバトロス",
        2: "イーグル",
        1: "バーディ",
        0: "パー",
        -1: "ボギー"
    }
    for v1,v2 in zip(regulation_strokes, actual_strokes):
        diff = v1-v2
        if v2 == 1 and v1 != 5:
            score_list.append("ホールインワン")
        elif diff in SCORE_MAPPING:
            score_list.append(SCORE_MAPPING.get(diff))
        else:
            score_list.append(f"{-diff}ボギー")


if __name__ == "__main__":
    regulation_strokes = list(map(int, input().split(',')))
    actual_strokes = list(map(int, input().split(',')))
    regulation_strokes_check(regulation_strokes)
    actual_strokes_check(actual_strokes)

    score_list=[]
    score_judge(regulation_strokes, actual_strokes ,score_list)

    print(score_list)

