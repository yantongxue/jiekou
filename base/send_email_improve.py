# coding=utf-8
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class SendMail:

    def __init__(self):
        self.msg=MIMEMultipart()# 引入这个就是为了发送附件，也就是实例化这个，可以发送很多MIMEText

    def send_mail(self, user_list, subject, content,html=None,file_path=None,image_path=None):
        send_user = "931038157@qq.com"
        password = "cvdjlxsjfdxabeee"
        email_host = "smtp.qq.com"
        user = "转角" + "<" + send_user + ">"

        message = MIMEText(content, _subtype="plain",_charset="utf-8")  # 此处的_subtype="plain",代表就是邮件类型，就是普通text邮件类型,如果是html就是html类型
        self.msg.attach(message)
        if html!=None:
            file_html = MIMEText(html, _subtype="html",_charset="utf-8")  # 此处的_subtype="plain",代表就是邮件类型，就是普通text邮件类型,如果是html就是html类型
            self.msg.attach(file_html)


        if file_path!=None:
            att1 = MIMEText(open(file_path, 'rb').read(), 'base64','gb2312')  # 这里的read()读取全部内容，open里面的"rb'意思就是以制度的形式打开文件，但是还没有读打开的文件
        # base64一般用于在HTTP协议下传输二进制数据，由于HTTP协议是文本协议，所以在HTTP协议下传输二进制数据需要将二进制数据转换为字符数据
            att1["Content-Type"] = 'application/octet-stream'  # application/octet-stream ： 二进制流数据（如常见的文件下载）
            att1["Content-Disposition"] = 'attachment; filename="fujian"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字，需要实现一个强制在浏览器中的下载功能（即强制让浏览器弹出下载对话框），并且文件名必须保持和用户之前上传时相同（可能包含非 ASCII 字符）。 前一个需求很容易实现：使用 HTTP Header 的 Content-Disposition: attachment 即可，还可以配合 Content-Type: application/octet-stream 来确保万无一失。
            self.msg.attach(att1)


        if image_path!=None:

            image = MIMEImage(open(image_path,"rb").read())
            image.add_header('Content-ID', '<image1>')
            self.msg.attach(image)






        #msg to from  subject是为了构造收到的邮件的头部信息
        self.msg["To"] = user_list
        self.msg["from"] =user
        self.msg["subject"] = subject
        server = smtplib.SMTP_SSL()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, self.msg.as_string())
        server.close()


if __name__ == "__main__":
    #mail_msg = """
        #<p>Python 邮件发送测试...</p>
        #<p><a href="http://www.runoob.com">这是一个链接</a></p>
        #"""
    send = SendMail()

    send.send_mail("yanlizhi@myhexin.com", "接口测试分析","测试哈哈哈哈哈哈",image_path='C:/Users/viruser.v-desktop/Desktop/picture/1.jpg')

