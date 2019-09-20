import smtplib as smtp
import time


def sendTheMessage(emails, passwords, subjects, email_texts, comboboxs,  deist_emails='gameway.com@yandex.ru'):
    if comboboxs == 'Yandex.ru':
        email = emails
        password = passwords
        deist_email = deist_emails

        subject = subjects
        email_text = email_texts

        message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, deist_email, subject, email_text)

        server = smtp.SMTP_SSL('smtp.yandex.ru')
        server.set_debuglevel(1)
        server.ehlo(email)
        server.login(email, password)
        server.auth_plain()
        server.sendmail(email, deist_email, message)

        time.sleep(5)
        server.quit()

    elif comboboxs == 'Mail.ru':
        email = emails
        password = passwords
        deist_email = deist_emails

        subject = subjects
        email_text = email_texts

        message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, deist_email, subject, email_text)

        server = smtp.SMTP_SSL('smtp.mail.ru')
        server.set_debuglevel(1)
        server.ehlo(email)
        server.login(email, password)
        server.auth_plain()
        server.sendmail(email, deist_email, message)
        time.sleep(5)
        server.quit()