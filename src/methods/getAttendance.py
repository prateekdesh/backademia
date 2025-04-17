import requests


def getAttendance(cookies):

    url = "https://academia.srmist.edu.in/srm_university/academia-academic-services/page/My_Attendance"

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-GB,en;q=0.9",
        "Connection": "keep-alive",
        "DNT": "1",
        "Referer": "https://academia.srmist.edu.in/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="135", "Not-A.Brand";v="8"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    response = requests.get(url, headers=headers, cookies=cookies)
    return response



