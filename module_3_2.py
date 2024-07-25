def send_email(message, recipient, sender="university.help@gmail.com"):
    if (('@' and (".com" or ".ru" or ".net")) not in (recipient or sender)
            or ('@' or (".com" or ".ru" or ".net")) not in (recipient or sender)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('message', 'vasyok1337@gmail.com')
send_email('message', 'urban.info@gmail.com', 'urban.fan@mail.ru')
send_email('message', 'urban.teacher@mail.uk', 'urban.student@mail.ru')
send_email('message', 'university.helpgmail.com')
send_email('message', 'university.help@gmail.r')
send_email('message', 'university.help@gmail.com')




