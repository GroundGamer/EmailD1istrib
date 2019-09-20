import imaplib
import email


def tookEmail(emailsis, passwordsis, comboboxsis):
    emails = []

    if comboboxsis == 'Yandex.ru':
        mail = imaplib.IMAP4_SSL('imap.yandex.ru')

        mail.login(emailsis, passwordsis)

        mail.select('Inbox')

        type, data = mail.search(None, 'ALL')

        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))

                    email_from = msg['from']

                    email_from = email_from.replace('<', '').replace('>', '')

                    emails.append(email_from)

        # Отсекаем лишнее
        emails = [s.split(None, 1)[-1] for s in emails]
        emails = [s.split(None, 1)[-1] for s in emails]
        emails = [s.split(None, 1)[-1] for s in emails]

        print(emails)
        return emails

    elif comboboxsis == 'Mail.ru':
        mail = imaplib.IMAP4_SSL('imap.mail.ru')

        mail.login(emailsis, passwordsis)

        mail.select('Inbox')

        type, data = mail.search(None, 'ALL')

        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))

                    email_from = msg['from']

                    email_from = email_from.replace('<', '').replace('>', '')

                    emails.append(email_from)

        # Отсекаем лишнее
        emails = [s.split(None, 1)[-1] for s in emails]
        emails = [s.split(None, 1)[-1] for s in emails]
        emails = [s.split(None, 1)[-1] for s in emails]

        print(emails)
        return emails
