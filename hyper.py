from httpx import post as httpxPOST

def hypeSquad(houses, tokens):
    houseLists = ["bravery", "brilliance", "balance"]
    for houseID, houseNAME in zip([1, 2, 3], houseLists):
        if (houses == houseNAME):
            payload = {'house_id': houseID}
        if (houses not in houseLists):
            return False

    requestsResponse = httpxPOST(
        'https://discordapp.com/api/v9/hypesquad/online', 
        headers={'Authorization': tokens,'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}, 
        json=payload
    ).text

    return requestsResponse

if (__name__ == "__main__"):
    tokens = input("YOUR TOKEN : ")
    houses = input("HOUSE [bravery, brilliance, balance] : ")

    hypeSquad(houses, tokens)
