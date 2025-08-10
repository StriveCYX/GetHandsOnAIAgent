from dotenv import load_dotenv
import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"  # 禁用 LangSmith 警告
load_dotenv()

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

# 初始化本地模型 Gemma 3
llm = Ollama(model="gemma3")  # 确保已运行 `ollama pull gemma3`

# 创建带对话历史的提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个帮助用户了解鲜花信息的智能助手，请用纯JSON格式回答，包含一个'answer'字段"),
    ("human", "生日礼物送什么花最好？"),
    ("ai", "玫瑰花是生日礼物的热门选择。"),
    ("human", "送货需要多长时间？")
])

# 创建处理链
chain = prompt | llm | StrOutputParser()

# 执行查询
response = chain.invoke({})

print("完整响应:")
print(response)

# 尝试解析JSON（模型可能返回非标准JSON，需要处理）
try:
    # 提取可能的JSON部分（Gemma 3有时会在JSON外添加额外文本）
    json_start = response.find('{')
    json_end = response.rfind('}') + 1
    json_str = response[json_start:json_end]
    
    parsed = json.loads(json_str)
    print("\n解析后的JSON内容:")
    print(parsed['answer'])
except Exception as e:
    print(f"\nJSON解析失败，返回原始响应: {e}")
    print(response)