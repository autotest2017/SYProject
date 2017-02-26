#!/usr/bin/env python
# encoding:utf-8
"""
功能：发送HTML的邮件内容

演示：jupyter notebook 通过SMTP协议发送纯文本邮件
使用163邮箱作为测试：

用户名：zelin_test@163.com
密码：zelin123456
第三方授权码：Zelin123456
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))





def send_email(FROM_ADDR, FROM_PSWD, TO_ADDR, subject, file_path, mode="html"):
    SMTP_SERVER = u"smtp.163.com"
    html_data = ''

    if not file_path:
        return
    with open(file_path) as fp:
        html_data = fp.read()  # 把文本内容一次性读入内存
    msg = MIMEText(html_data, mode, 'utf-8')
    msg['From'] = _format_addr(u'自动化平台 <%s>' % FROM_ADDR)
    msg['To'] = _format_addr(u'开发人员 <%s>' % TO_ADDR)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP(SMTP_SERVER)
    server.login(FROM_ADDR, FROM_PSWD)
    server.sendmail(FROM_ADDR, [TO_ADDR], msg.as_string())
    server.quit()

if __name__ == "__main__":
    #send_email()
    pass