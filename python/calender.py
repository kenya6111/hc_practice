

import sys
import datetime
from datetime import date, timedelta

class Color:
    BLACK          = '\033[30m'#(文字)黒
    RED            = '\033[31m'#(文字)赤
    GREEN          = '\033[32m'#(文字)緑
    YELLOW         = '\033[33m'#(文字)黄
    BLUE           = '\033[34m'#(文字)青
    MAGENTA        = '\033[35m'#(文字)マゼンタ
    CYAN           = '\033[36m'#(文字)シアン
    WHITE          = '\033[37m'#(文字)白
    COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
    BOLD           = '\033[1m'#太字
    UNDERLINE      = '\033[4m'#下線
    INVISIBLE      = '\033[08m'#不可視
    REVERCE        = '\033[07m'#文字色と背景色を反転
    BG_BLACK       = '\033[40m'#(背景)黒
    BG_RED         = '\033[41m'#(背景)赤
    BG_GREEN       = '\033[42m'#(背景)緑
    BG_YELLOW      = '\033[43m'#(背景)黄
    BG_BLUE        = '\033[44m'#(背景)青
    BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
    BG_CYAN        = '\033[46m'#(背景)シアン
    BG_WHITE       = '\033[47m'#(背景)白
    BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
    RESET          = '\033[0m'#全てリセット

week1=[]
week2=[]
week3=[]
week4=[]
week5=[]
week6=[]
week_list=["月","火","水","木","金","土","日"]

def count_by_week(first_day, end_day, d, now_day):
    """
    カレンダー情報を生成する。
    """
    day = 1
    for i in range(1,6*7):

        if i < first_day.weekday() + 1:
            week1.append("  ")
            continue
        elif i <= 7:
            week1.append(" " + str(day))
            day += 1
        elif i <= 14:
            if day < 10:
                week2.append(" " + str(day))
            else:
                week2.append(str(day))
            day += 1
        elif i <= 21:
            week3.append(str(day))
            day += 1
        elif i <= 28:
            week4.append(str(day))
            day += 1
        elif i <= 35:
            if day == end_day.day+1:
                break
            week5.append(str(day))
            day += 1
        elif i <= 42:
            if day == end_day.day+1:
                break
            week6.append(str(day))
            day += 1

    print("     {}月 {}".format(d.month,d.year))
    print(' '.join(week_list))
    print(' '.join(week1))
    print(' '.join(week2))
    print(' '.join(week3))
    print(' '.join(week4))
    print(' '.join(week5))
    print(' '.join(week6))

def create_calender():
    """
    現在月のカレンダーを表示する。
    """
    # 現在月の情報取得
    d = datetime.date.today()
    first_day = date(d.year, d.month, 1)
    end_day = date(d.year, d.month + 1, 1) - timedelta(days = 1)
    now_day = d.day
    count_by_week(first_day, end_day, d, now_day)


def create_calender_option():
    """
    指定月のカレンダーを表示する。
    """
    try:
        # 指定月の値取得
        month_index = sys.argv.index("-m") + 1
        month = int(sys.argv[month_index])
        if month < 0 or month > 12:
            raise ValueError

        # 指定月の初日と最終日取得
        d = datetime.date(2024, month, 10)
        first_day = date(d.year, d.month, 1)
        if d.month == 12:
            end_day = date(d.year + 1, 1, 1) - timedelta(days = 1)
        else:
            end_day = date(d.year, d.month + 1, 1) - timedelta(days = 1)

        count_by_week(first_day, end_day, d, None)
    except ValueError:
        print(f"{month} is neither a month number (1..12) nor a name")

def count_test (num):
    num=num+1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-m':
        if len(sys.argv) < 3:
            sys.exit("end program")
        create_calender_option()
    else:
        create_calender()
    print(f'{Color.BLACK}{Color.BG_WHITE}aaaa{Color.RESET}')
