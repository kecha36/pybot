# 与えられた文字列の長さを返す
# param 長さ 文字列
def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字列ノ長サハ {} 文字デス'.format(length)
    return response
