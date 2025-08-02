# 设置OpenAI API密室
import os
os.environ["OPENAI_API_KEY"]='你的密室'
# 导入OpenAI库
from openai import OpenAI
# 创建client
client = OpenAI()
# 调用chat.completions.create()
response = client.chat.completions.create(
    model = "gpt-4-turbo-preview",
    response_format = {"type":"json-object"},
    message = [
        {"role":"system","content":"您是一个帮助用户了解鲜花信息的智能助手，并能够输出JSON格式的内容。"},
        {"role":"user","content":"生日礼物送什么花最好？"},
        {"role":"assistant","content":"玫瑰花是生日礼物的热门选择。"},
        {"role":"user","content":"送货需要多长时间？"}
    ]
)

print(response)

# 只打印响应中的消息内容
print('只打印响应中的消息内容\n')
print(response.choices[0].message.content)