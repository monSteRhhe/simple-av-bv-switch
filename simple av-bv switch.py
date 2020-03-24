import urllib.request
import json

print("模式1：av → bv（输入1")
print("模式2：bv → av（输入2")
check = input("输入选择的模式：")
mode = int(check)

if mode == 1:
    target = input("请输入av号(省略av)：")
    html = urllib.request.urlopen(r'http://api.bilibili.com/x/web-interface/view?aid='+target)
    hjson = json.loads(html.read())
    print("对应的BV号是：", hjson['data']['bvid'])
else:
    target = input("请输入bv号(省略BV)：")
    html = urllib.request.urlopen(r'http://api.bilibili.com/x/web-interface/view?bvid='+target)
    hjson = json.loads(html.read())
    print("对应的AV号是：", hjson['data']['aid'])

input()
