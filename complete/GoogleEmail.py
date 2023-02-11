import email
import imaplib
from email.header import decode_header, make_header


imap = imaplib.IMAP4_SSL('imap.gmail.com')
imap.login('홍길동@gmail.com', '16글자 전용 인증암호')

imap.select("INBOX")
# 사서함의 모든 메일의 uid 정보 가져오기
# 만약 특정 발신 메일만 선택하고 싶다면 'ALL' 대신에 '(FROM "xxxxx@naver.com")' 입력
status, messages = imap.uid('search', None, 'ALL')

messages = messages[0].split()

# 0이 가장 마지막 메일, -1이 가장 최신 메일
recent_email = messages[-1]

# fetch 명령어로 메일 가져오기
res, msg = imap.uid('fetch', recent_email, "(RFC822)")

# 사람이 읽을 수 있는 없는 상태의 이메일
raw = msg[0][1]

# 사람이 읽을 수 있는 형태로 변환
raw_readable = msg[0][1].decode('utf-8')

email_message = email.message_from_string(raw_readable)
fr = make_header(decode_header(email_message.get('From')))
print(fr)

# 메일 제목
subject = make_header(decode_header(email_message.get('Subject')))
print(subject)

# 메일 내용
if email_message.is_multipart():
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
else:
    body = email_message.get_payload(decode=True)
    




