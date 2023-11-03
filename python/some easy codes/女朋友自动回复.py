import time  
  
def respond_to_message(message):  
    # 定义自动回复的消息列表  
    responses = {  
        "我想你了": "宝贝，我也很想你！",  
        "你在干嘛呢": "我正在想你呢，你呢？",  
        "我爱你": "我也爱你，宝贝！",  
        "晚安": "晚安，宝贝，做个好梦！",  
        "早安": "早安，宝贝！"  
    }  
  
    # 检查消息是否在自动回复列表中  
    if message in responses:  
        return responses[message]  
    else:  
        return "对不起，宝贝，我没有听懂你的话，你可以再说一次吗？"  
  
# 无限循环，等待女朋友的消息并自动回复  
while True:  
    message = input("女朋友发来一条消息：")  
    response = respond_to_message(message)  
    print("回复：", response)  
    time.sleep(1)  # 等待1秒钟再继续循环
