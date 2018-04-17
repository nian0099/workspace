'''
邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
'''

import re
import smtplib
#邮件内容主体的扩展，从只支持纯文本格式扩展到HTML，同时支持附件、音频、图像等格式
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror,error
from src.utils.log import logger

class Email:
    def __init__(self,server,sender,password,receiver,title,message = None,path = None):
        """
        初始化Email类
        :param server:服务器
        :param sender:发件人
        :param password:密码
        :param receiver:收件人
        :param title:标题（非必填）
        :param message:信息（非必填）
        :param path:附件路径
        """
        self.title = title

        self.server = server

        self.sender = sender

        self.message = message

        self.password = password

        self.receiver = receiver

        self.files = path

        self.msg = MIMEMultipart('related')

    def _attach_file(self,att_file):
        '''
        将单个文件添加到附件列表中
        :param att_file:文件
        :return:
        '''
        att = MIMEText(open('%s' % att_file,'rb').read(),'plain','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]',att_file)
        att['Content-Disposition'] = 'attachment;filename = "%s"'%file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg["Subject"] = self.title
        self.msg["From"] = self.sender
        self.msg["To"] = self.receiver

        #邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files,list):
                for f in self.files:
                    self._attach_file(f)

            elif isinstance(self.files,str):
                self._attach_file(self.files)

        #连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  #连接server
        except(gaierror and error) as e:
            logger.exception("发送邮件失败，无法连接到SMTP服务器，检查SMTP服务器及网络.%s",e)
        else:
            try:
                smtp_server.login(self.sender,self.password)    #登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception("用户名及密码验证失败--%s",e)
            else:
                smtp_server.sendmail(self.sender,self.receiver.split(";"),self.msg.as_string())    #发送邮件
            finally:
                smtp_server.quit()   #断开连接
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))








