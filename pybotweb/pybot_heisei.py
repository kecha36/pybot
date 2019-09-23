# 与えられた西暦を平成に変換する
# param 平成 XXXX(西暦4桁)
def heisei_command(command):
    heisei, year_str = command.split();
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989 and year < 2020:
            heisei_year = year - 1988
            response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
        else:
            response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    else:
        response = '数値ヲ入力シテクダサイ'
    return response
