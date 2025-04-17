import requests


def get_id_and_digest(email: str):
    url = f"https://academia.srmist.edu.in/accounts/p/40-10002227248/signin/v2/lookup/{email}"

    headers = {
        "Cookie": "zalb_74c3a1eecc=d06cba4b90fbc9287c4162d01e13c516; cli_rgn=IN; _ga=GA1.3.1056011460.1744823504; _gid=GA1.3.635174888.1744823504; zalb_f0e8db9d3d=7ad3232c36fdd9cc324fb86c2c0a58ad; stk=a4ccd4b85bd37868861e8771c7f5d578; zccpn=1fb52cfe3f0a1881b673e64b5c7f31087c4a3d1707b1427270bbc74b33857d23071c4160307ab017746ec035b755f30f071e440f53a3df9e8a7218868be1e4ff; zalb_3309580ed5=5e41c4a69d62a20d11fee6ef8532db03; CT_CSRF_TOKEN=0ce8b2ac-a8ed-4dc0-a96b-61df62887b66; JSESSIONID=20E51295DC15FF49EB707D322D88EF5E; iamcsr=1fb52cfe3f0a1881b673e64b5c7f31087c4a3d1707b1427270bbc74b33857d23071c4160307ab017746ec035b755f30f071e440f53a3df9e8a7218868be1e4ff; _zcsr_tmp=1fb52cfe3f0a1881b673e64b5c7f31087c4a3d1707b1427270bbc74b33857d23071c4160307ab017746ec035b755f30f071e440f53a3df9e8a7218868be1e4ff; _gat=1; _ga_HQWPLLNMKY=GS1.3.1744833364.2.0.1744833364.0.0.0",
        "X-ZCSRF-TOKEN": "iamcsrcoo=1fb52cfe3f0a1881b673e64b5c7f31087c4a3d1707b1427270bbc74b33857d23071c4160307ab017746ec035b755f30f071e440f53a3df9e8a7218868be1e4ff",
        "content-type": "application/x-www-form-urlencoded",
    }

    data = {
        "serviceurl": "https://academia.srmist.edu.in/portal/academia-academic-services/redirectFromLogin"
    }

    response = requests.post(url, headers=headers, data=data)


    data = response.json()

    id = data['lookup']['identifier']
    digest = data['lookup']['digest']

    return ([id, digest])

