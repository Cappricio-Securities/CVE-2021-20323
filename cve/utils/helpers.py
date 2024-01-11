#!/usr/bin/env node

"""
 * CVE-2021-20323
 * CVE-2021-20323 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""
    
👋 Hey \033[96m{username}
   \033[92m                                                             v1.0
  ______   ______    ___  ___  ___ ___    ___  ___  ____ ___  ____
 / ___/ | / / __/___|_  |/ _ \|_  <  /___|_  |/ _ \|_  /|_  ||_  /
/ /__ | |/ / _//___/ __// // / __// /___/ __// // //_ </ __/_/_ < 
\___/ |___/___/   /____/\___/____/_/   /____/\___/____/____/____/     

                                   \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mCVE-2021-20323 : Bug scanner for WebPentesters and Bugbounty Hunters 

\x1b[31;1m$ \033[92mCVE-2021-20323\033[0m [option]

Usage: \033[92mCVE-2021-20323\033[0m [options]

Options:
  -u, --url     URL to scan                                CVE-2021-20323 -u https://target.com                
  -i, --input   <filename> Read input from txt             CVE-2021-20323 -i target.txt                         
  -o, --output  <filename> Write output in txt file        CVE-2021-20323 -i target.txt -o output.txt     
  -c, --chatid  Creating Telegram Notification             CVE-2021-20323 --chatid yourid    
  -b, --blog    To Read about CVE-2021-20323 Bug           CVE-2021-20323 -b   
  -h, --help    Help Menu                       
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
   \033[92m                                                             v1.0
  ______   ______    ___  ___  ___ ___    ___  ___  ____ ___  ____
 / ___/ | / / __/___|_  |/ _ \|_  <  /___|_  |/ _ \|_  /|_  ||_  /
/ /__ | |/ / _//___/ __// // / __// /___/ __// // //_ </ __/_/_ < 
\___/ |___/___/   /____/\___/____/_/   /____/\___/____/____/____/     

                                   \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mCVE-2021-20323 : Bug scanner for WebPentesters and Bugbounty Hunters 

\033[0m"""
    print(help_banner)
