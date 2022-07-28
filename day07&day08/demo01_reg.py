import requests
import re

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%E7%88%AC%E8%99%AB,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=&u_atoken=c0ae8c1c-d0a5-42fa-b2ac-88b3237128eb&u_asession=01DqEHLHyleX6ZW9hCRIVe72haEx5H4DrdmkODaBe8uhCzh6PkAuwKVST8gbqawlqwX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K8DYQ645wK4u-_o73ABGdq0Ppcarp92QKzyJKyYjREPlmBkFo3NEHBv0PZUm6pbxQU&u_asig=05oTqGq3XJdJSIYRv1d5U-X6-DfOPMeyalw3swMUv4DfcKqOuzlhRsh5wCP3hDdyxXo4_JOVVR4zOwEbW4C-3-X78ps9qakXxi8MvNoSu-h3z45iFkjdhm-m0J_WoDnsRfArFHhz015QBUvLQUaXdx5a90zPR-eMiWrdqFKdmbdlL9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzeh4TKBmTGp5TbbiHfVjJWCzTAtxsDMaVfCAFJ4IfnEDWPRPQyB_SKrj-61LB_f61u3h9VXwMyh6PgyDIVSG1W9r-XlvLrP9AYkB8jjQR_vuewz9FOKF11WmjcFoRW2jec1_OdbCUff-rzOge69JqCbddZ-zU_C5p9Qn9hm7RcmHmWspDxyAEEo4kbsryBKb9Q&u_aref=lIV3ULC6ZG87SNdYSZGyIvHbTXc='

response = requests.get(url)

if response.status_code == 200:
    # print(response.text)
    ...

#正则表达式
exp = r'<script.*?type="text/javascript">(.*?)</script>'
reg = re.compile(exp,re.S)
data = reg.findall(response.text)
index = data[0].index('{')
data = eval(data[0][index:])
engine_jobs = data['engine_jds']
for item in engine_jobs:
    print("工作详情网页: "+item['job_href'])
    print('工作名: ' +item['job_name'])
    print('公司名: ' + item['company_name'])
    print('薪资标准: '+ item['providesalary_text'])
    print('工作地区: ' + item['workarea_text'])
    print('工作福利: ' + item['jobwelf'])
    print()

