import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

def check_soldout():
    url = "https://mujugipot.co.kr/shop/item.php?it_id=1395143923&NaPm=ct%3Dm02g30js%7Cci%3D4f245578cda3cb89704e9e546e4d92d1a865dd9d%7Ctr%3Dslsl%7Csn%3D857396%7Chk%3De43d859e6e878cf6f0c89264b99239694871c5aa"
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        soldout_option = soup.select_one("#it_option_1")

        if soldout_option:
            options = soldout_option.find_all("option")
            if len(options) > 1:
                option_state = options[1]
                if "품절" in option_state.text:
                    print("상품이 품절상태입니다.")
                    return "상품이 품절상태입니다."
                else:
                    print("상품의 재고가 있습니다.")
                    return "상품의 재고가 있습니다."
            else:
                print("옵션이 충분하지 않습니다.")
                return "옵션이 충분하지 않습니다."
        else:
            print("옵션을 찾을 수 없습니다.")
            return "옵션을 찾을 수 없습니다."
    except Exception as e:
        print("에러:", e)
        return f"에러 발생: {e}"


def send_email(subject, body, to_email):
    from_email = "from_email "
    password = "password"
    to_email = "to_email"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        
        with smtplib.SMTP("smtp.mail.nate.com", 587) as server:
            server.starttls() 
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            print("이메일이 성공적으로 발송되었습니다.")
    except Exception as e:
        print(f"이메일 발송 중 오류 발생: {e}")


send_email(
    subject="상품 입고상태",
    body=check_soldout(),
    to_email="to_email"
)