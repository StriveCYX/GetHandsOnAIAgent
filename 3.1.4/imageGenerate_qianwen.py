# 导入所需库
from dashscope import ImageSynthesis
import dashscope
from dotenv import load_dotenv
import os
import requests
from IPython.display import Image, display

# 加载环境变量
load_dotenv()

# 设置 DashScope API Key
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')
if not dashscope.api_key:
    raise ValueError("请在 .env 文件中设置 DASHSCOPE_API_KEY")

# 调用通义万相（WanX）生成图像
response = ImageSynthesis.call(
    model='wanx-v1',  # 通义万相文生图模型
    prompt="电商花语秘境的新春玫瑰花宣传海报，配上文案",
    n=1,              # 生成1张
    size='1024*1024', # 尺寸
    steps=50,         # 可选：生成步数，越高越精细
    cfg_scale=7,      # 可选：提示词相关性
)


# 检查响应是否成功
if response.status_code == 200:
    # 获取生成的图片 URL
    image_url = response.output.results[0].url
    print("图片生成成功！URL:", image_url)

    # 下载图片
    image_data = requests.get(image_url).content

    # 在 Jupyter 中显示图片
    display(Image(data=image_data))
else:
    print('生成失败:', response)

# 保存图片到本地
with open('generated_image.jpg', 'wb') as f:
    f.write(image_data)
    print("图片已保存为 generated_image.jpg")

# 在Jupyter Notebook中显示图片
Image(image_data)