from auth.login_init import get_id_and_digest
import requests

def getCookies(email, password):
    auth = list(get_id_and_digest(email))

    url = f"https://academia.srmist.edu.in/accounts/p/40-10002227248/signin/v2/primary/{auth[0]}/password?digest={auth[1]}&cli_time=1744860675322&servicename=ZohoCreator&service_language=en&serviceurl=https%3A%2F%2Facademia.srmist.edu.in%2Fportal%2Facademia-academic-services%2FredirectFromLogin"

    data = {"passwordauth": {"password": password}}

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-GB,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "zalb_74c3a1eecc=d06cba4b90fbc9287c4162d01e13c516; _ga=GA1.3.1056011460.1744823504; _gid=GA1.3.635174888.1744823504; zalb_f0e8db9d3d=7ad3232c36fdd9cc324fb86c2c0a58ad; stk=a4ccd4b85bd37868861e8771c7f5d578; zalb_3309580ed5=5e41c4a69d62a20d11fee6ef8532db03; CT_CSRF_TOKEN=0ce8b2ac-a8ed-4dc0-a96b-61df62887b66; JSESSIONID=0576A060D80E11468562067564B79352; cli_rgn=IN; zccpn=a750e015622d2033f4705482d3295f3a17c1953fbfa94f0a1d5b2f4dc1022deb7164f43c2987c2e94670aa9c2c8f387c36087231da118722ed04ed168f0732c6; _zcsr_tmp=a750e015622d2033f4705482d3295f3a17c1953fbfa94f0a1d5b2f4dc1022deb7164f43c2987c2e94670aa9c2c8f387c36087231da118722ed04ed168f0732c6; iamcsr=a750e015622d2033f4705482d3295f3a17c1953fbfa94f0a1d5b2f4dc1022deb7164f43c2987c2e94670aa9c2c8f387c36087231da118722ed04ed168f0732c6; _gat=1; _ga_HQWPLLNMKY=GS1.3.1744860674.4.0.1744860674.0.0.0",
        "DNT": "1",
        "Origin": "https://academia.srmist.edu.in",
        "Referer": "https://academia.srmist.edu.in/accounts/p/10002227248/signin?hide_fp=true&servicename=ZohoCreator&service_language=en&css_url=/49910842/academia-academic-services/downloadPortalCustomCss/login&dcc=true&serviceurl=https%3A%2F%2Facademia.srmist.edu.in%2Fportal%2Facademia-academic-services%2FredirectFromLogin",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-ZCSRF-TOKEN": "iamcsrcoo=a750e015622d2033f4705482d3295f3a17c1953fbfa94f0a1d5b2f4dc1022deb7164f43c2987c2e94670aa9c2c8f387c36087231da118722ed04ed168f0732c6",
        "sec-ch-ua": '"Chromium";v="135", "Not-A.Brand";v="8"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    response = requests.post(url, headers=headers, json=data)

    cookies = response.cookies

    authy = {}
    for cookie in cookies:
        authy[cookie.name] = cookie.value

    return authy





