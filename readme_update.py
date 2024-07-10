import feedparser, datetime

# 로컬 테스트 시 ssl 인증서 문제 해결용
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# rss 추출
feed = feedparser.parse("https://kminu.tistory.com/rss")

# README 양식
markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=220&section=header&text=Minu%20Kim&fontSize=60&animation=fadeIn&fontAlignY=38&descAlignY=51&descAlign=62)

## 🎓 Profile
- Konkuk University Dept. of Smart Ict Convergence (2021~)

<br>

## 📕 Latest Blog Posts     

"""

# 최근 블로그 추가
for i in feed['entries'][:4]:

    # date formation
    date = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y.%m.%d")
    
    markdown_text += f"<a href =\"{i['link']}\"> [{date}] {i['title']} </a> <br>"
    # print(i['link'], i['title'])

# print(markdown_text)
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
