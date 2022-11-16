
# These are the location filters, also retrieved from Charles Proxy. Once copied, these don't need to be updated unless you want to update your filters
search_json_data = {
    "apiVersion": "V2",
    "filters": {
        "serviceAreaFilter": [
            "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx",
            "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx",
            "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx",
            "x",
            "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx",
            "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx",
        ],
        "timeFilter": {},
    },
    "serviceAreaIds": [
        "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx",
    ],
}


def accept_json_data(offerID):
    # This is the json data needed to accept a block, it takes an argument to extract the offer ID for the selected block
    return {
        "__type": "AcceptOfferInput:http://internal.amazon.com/coral/com.amazon.omwbuseyservice.offers/",
        "offerId": offerID,
    }
