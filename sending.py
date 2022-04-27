from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
# info代表基本資料, which代表要傳送的是圖片或是純文字檔案
# xian20020824@gmail.com
# "vxpyoxwgxdygouwo"
def send_mail(info, which, content, app_pass):
    contents = MIMEMultipart()
    contents["subject"] = info[0]
    contents["from"] = info[1]
    contents["to"] = info[2]
    if which == "pic":
        contents.attach(MIMEText(content))
    elif which == "text":
        contents.attach(MIMEText(content))
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(info[1], app_pass)  # 登入寄件者gmail
            smtp.send_message(contents)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
# 以上即可進行純文字信件傳送了