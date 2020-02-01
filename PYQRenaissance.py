import itchat
import random, json
import time

with open('corpus.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    
firstImpression = json_data['第一印象']
adj_FI = json_data['第一印象形容']
compliment  = json_data['夸赞句子']
truth = json_data['真心话']
secret = json_data['秘密']
answer = json_data['答案']
pic = json_data['年轻照片']
chat = json_data['瞎聊']
#itchat.auto_login()

@itchat.msg_register('Text')
def text_reply(msg):
    #message:取出msg里面的文本消息
    message = msg['Text']
    
    # 延时5-12秒，假装在打字，以及防止号被限制
    wait = random.randint(3, 8)
    time.sleep(wait)
    
    reply = ''
    if  '1' in message: # 第一印象
        reply = random.choice(firstImpression)
        reply = reply.replace('adj', random.choice(adj_FI))
    elif '2' in message: # 夸赞
        reply = random.choice(compliment)
    elif '3' in message:  # 真心话
        reply = random.choice(secret)
    elif '4' in message: # 秘密
        reply = random.choice(secret)
    elif '5' in message: # 高中照片
        reply += "好吧，看来要拿出我QQ空间珍藏的高中照片了\n"
        # 0-刘皓然 1-彭鱼晏 2-吴三石 3-吴彦祖 4-金乘五 5-木村拓
        #reply += pic[0]
        reply += random.choice(pic)
    elif '6' in message: # 问题
        reply = random.choice(answer)

    # 如果后续被diss
    elif '傻' in message:
        reply = '怎么可能傻得过你'
    elif '自动' in message:
        reply = '?? 我这么真诚，都是掏心窝子的话'
    elif '笑' in message:
        reply = '你开心就好'
    elif '。。' in message:
        reply = '给你一个大大的围笑'    
    elif '拜' in message:
        reply = '886'
    else:
        reply = random.choice(chat)
    
    return reply

if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    itchat.send('I am ready', toUserName='filehelper')
    itchat.run()