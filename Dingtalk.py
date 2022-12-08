from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings
import time
import datetime

# WebHook地址
WEBHOOK = getattr(settings, "WEBHOOK", None)
SECRET = getattr(settings, "SECRET", None)
webhook = f"https://oapi.dingtalk.com/robot/send?access_token={WEBHOOK}"
secret = SECRET  # 可选：创建机器人勾选“加签”选项时使用
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

# 今天星期几
Week2 = int(time.strftime("%w"))
print(Week2)
Week = str((Week2)+1)
classlist1 = "星期一\n数学\n语文\n历史\n政治\n\n数学\n英语\n化学\n物理\n\n英语\n数学"
classlist2 = "星期二\n历史\n英语\n物理\n数学\n\n政治\n英语\n语文\n语文\n\n历史\n化学"
classlist3 = "星期三\n数学\n语文\n历史\n政治\n\n数学\n英语\n物理\n化学\n\n政治\n物理"
classlist4 = "星期四\n历史\n英语\n物理\n数学\n\n政治\n英语\n语文\n语文\n\n化学\n语文"
classlist5 = "星期五\n化学\n语文\n物理\n历史\n\n语文\n英语\n数学\n数学\n\n物理\n数学"
classlist6 = "星期六\n数学\n化学\n英语\n英语\n\n语文\n数学\n物理\n政治\n\n英语\n语文"
classlist7 = "0"

if Week == '1':
    xiaoding.send_text(msg=classlist1, is_at_all=False)
elif Week == '2':
    xiaoding.send_text(msg=classlist2, is_at_all=False)
elif Week == '3':
    xiaoding.send_text(msg=classlist3, is_at_all=False)
elif Week == '4':
    xiaoding.send_text(msg=classlist4, is_at_all=False)
elif Week == '5':
    xiaoding.send_text(msg=classlist5, is_at_all=False)
elif Week == '6':
    xiaoding.send_text(msg=classlist6, is_at_all=False)
elif Week == '7':
    print("nothing")
