
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

auth_json_data = {
        "requested_extensions": ["device_info", "customer_info"],
        "cookies": {"website_cookies": [], "domain": ".amazon.com"},
        "registration_data": {
            "domain": "Device",
            "app_version": "0.0",
            "device_type": "A3NWHXTQ4EBCZS",
            "os_version": "15.2",
            "device_serial": "0000000000000000",
            "device_model": "iPhone",
            "app_name": "Amazon Flex",
            "software_version": "1",
        },
        "auth_data": {
            "user_id_password": {
                "user_id": "SpamMe@FuhQ.com",
                "password": "DefinitelyMyRealPassword",
            }
        },
        "user_context_map": {"frc": ""},
        "requested_token_type": ["bearer", "mac_dms", "website_cookies"],
    }



def accept_json_data(offerID):
    # This is the json data needed to accept a block, it takes an argument to extract the offer ID for the selected block
    return {
        "__type": "AcceptOfferInput:http://internal.amazon.com/coral/com.amazon.omwbuseyservice.offers/",
        "offerId": offerID,
    }
