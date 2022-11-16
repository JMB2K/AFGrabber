import requests
import json
import time
import json_data
import header_data
import getAuth
import logging
import random
from appJar import gui

logging.basicConfig(format="%(asctime)s \n\t%(message)s", level=logging.INFO)

session = requests.Session()


def get_offer_list():
    # Requesting list of available blocks and returning either a filtered list of blocks or an error message
    global session
    response = session.post(
        "https://flex-capacity-na.amazon.com/GetOffersForProviderPost",
        headers=header_data.headers,
        json=json_data.search_json_data,
    )

    j = json.loads(response.text)

    try:
        return [accept_block(block) for block in j["offerList"] if filter_blocks(block)]
    except KeyError:
        return j["message"]
    except:
        header_data.headers['x-amz-access-token'], header_data.headers['X-Amzn-RequestId'] = getAuth.getAuthToken()


def filter_blocks(block):
    # Filtering out blocks that you don't want.
    # Comment out individual filters that you don't want applied
    block_length = (block["endTime"] - block["startTime"]) / 3600
    return (
        not block["hidden"]
        and block["rateInfo"]["priceAmount"] / block_length > 29
        and block["rateInfo"]["priceAmount"] > 100
        and block["startTime"] - int(time.time()) >= 1500
        and block_length < 4
    )


def accept_block(block):
    # Accepting a block, returns status code. 200 is a successful attempt and 400 (I think, could be 404 or something else) is a failed attempt
    global session
    accept = session.post(
        "https://flex-capacity-na.amazon.com/AcceptOffer",
        headers=header_data.headers,
        json=json_data.accept_json_data(block["offerId"]),
    )

    if accept.status_code == 200:
        logging.info(f"Caught The Block For {block['rateInfo']['priceAmount']}")
    else:
        logging.info(f"Missed The Block For {block['rateInfo']['priceAmount']}")

    return accept.status_code

def press(button):
    if button == "Cancel":
        app.stop()
        return None
    else:
        json_data.auth_json_data["auth_data"]["user_id_password"]["user_id"] = app.getEntry("Email:")
        json_data.auth_json_data["auth_data"]["user_id_password"]["password"] = app.getEntry("Password:")

    keepItUp = True
    while keepItUp:
        lst = get_offer_list()
        if lst == "Rate exceeded":
            logging.info("Rate Exceeded, Waiting")
            time.sleep(90)
            logging.info("Back At It")
        elif 200 in lst:
            keepItUp = False
            break

        time.sleep(random.random())



if __name__ == "__main__":

    #header_data.headers['x-amz-access-token'], header_data.headers['X-Amzn-RequestId'] = getAuth.getAuthToken()

    app = gui()
    app.addLabelEntry("Email:")
    app.addLabelSecretEntry("Password:")
    app.addLabelOptionBox("Max Block Length:", ["3", "3.5", "4", "4.5", "5"])
    app.addLabelEntry("Min Per Hour:")
    app.button('Accessibility', app.showAccess, icon='ACCESS')
    app.go()




