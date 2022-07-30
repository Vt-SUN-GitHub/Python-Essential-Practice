from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import numpy as np
from PIL import Image

f = open('D:\SUN\study\peacetime\个人\聊天记录词云图\(2625379461).txt', mode='r', encoding='utf-8', errors='ignore')

text=''

#处理脏数据部分，可根据运行效果进行更改
lines = f.readlines()
for line in lines:
    if line.isspace():
        continue
    elif((line.find('20',0,2) >= 0) or (line.find('图片') >= 0) or (line.find('表情') >=0) or
         (line.find('撤回了一条消息') >= 0) or (line.find('QQ体验新功能') >=0 ) or (line.find('新版手机QQ') >=0 )):
        continue
    else:
        text+=(" "+line)
        ...
    ...

font = r'C:\Windows\Fonts\SimHei.ttf'
wordCloud = WordCloud(scale=5, font_path=font, max_words=2000,max_font_size=15).generate(text)

plt.subplots(figsize=(12,8),dpi=600)
plt.imshow(wordCloud)
plt.axis("off")
plt.show()

