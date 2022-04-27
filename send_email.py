from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

content = MIMEMultipart()
content["subject"] = "topic" # 郵件標題
content["from"] = "besidefwr@gmail.com" # sender
content["to"] = "happyhaha@g.ncu.edu.tw" # reciver
content.attach(MIMEText("send_email_test"))
# 寄出時需要使用應用程式密碼(因為此類型屬於高風險型應用)
# 以下為需要傳送圖片
content.attach(MIMEText("Demo python send email"))  # 郵件純文字內容
content.attach(MIMEImage(Path("kapo.jpg").read_bytes()))  # 郵件圖片內容
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("besidefwr@gmail.com", "vxpyoxwgxdygouwo")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)
# 以上即可進行純文字信件傳送了
