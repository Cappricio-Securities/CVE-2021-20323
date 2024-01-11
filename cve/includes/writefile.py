#!/usr/bin/env node

"""
 * CVE-2021-20323
 * CVE-2021-20323 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
def writedata(output,data):
    with open(output,'a') as file:
        file.write(data)