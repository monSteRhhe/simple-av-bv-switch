from urllib import request
import json

print("==简易AV号-BV号转换器==\n ==Current Version 0.2==")

def output(abv):
    if abv == 1:
        target = input("请输入av号(省略av)：")
        typ = 'a'
    else:
        target = input("请输入bv号(省略BV)：")
        typ = 'bv'
    html = request.urlopen(r'http://api.bilibili.com/x/web-interface/view?'+ typ +'id='+ target)
    getjson = json.loads(html.read())
    existcheck = getjson['code']
    if existcheck == 0:
        if abv == 1:
            print("对应的BV号是：", getjson['data']['bvid'])
        else:
            print("对应的AV号是：", getjson['data']['aid'])
    else:
        print("稿件不可见。")

ext = 0
while ext == 0:
    print("模式1：av → bv（输入1")
    print("模式2：bv → av（输入2")
    mode = int(input("请输入选择的模式："))
    if mode != 1 and mode != 2:
        print("请输入正确的数字。\n")
    elif mode == 1:
        output(1)
    else:
        output(2)
    print()
    end = int(input("输入1再次转换，按回车关闭程序："))
    if end != 1:
        print("\n请输入正确的数字。\n")
    else:
        ext = 0
