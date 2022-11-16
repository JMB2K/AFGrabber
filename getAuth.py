import requests
import header_data
import json_data


def getTwoStepVerificationChallengeUrl(challengeRequest):
    verificationChallengeCode = (
        challengeRequest.get("response")
        .get("challenge")
        .get("uri")
        .split("?")[1]
        .split("=")[1]
    )
    return (
        "https://www.amazon.com/ap/challenge?openid.return_to=https://www.amazon.com/ap/maplanding&openid.oa2.code_challenge_method=S256&openid.assoc_handle=amzn_device_ios_us&pageId=amzn_device_ios_light&accountStatusPolicy=P1&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.mode=checkid_setup&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.ns.oa2=http://www.amazon.com/ap/ext/oauth/2&openid.oa2.client_id=device:30324244334531423246314134354635394236443142424234413744443936452341334e5748585451344542435a53&language=en_US&openid.ns.pape=http://specs.openid.net/extensions/pape/1.0&openid.oa2.code_challenge=n76GtDRiGSvq-Bhrez9x0CypsZFB_7eLfEDy_qZtqFk&openid.oa2.scope=device_auth_access&openid.ns=http://specs.openid.net/auth/2.0&openid.pape.max_auth_age=0&openid.oa2.response_type=code"
        + f"&arb={verificationChallengeCode}"
    )


def getAuthToken():
    """
    Get authorization token for Flex Capacity requests
    Returns:
    An access token as a string
    """
    authUrl = "https://api.amazon.com/auth/register"
    
    try:
        response = requests.post(authUrl, headers=header_data.authHeaders, json=json_data.auth_json_data).json()
        return (
            response.get("response")
            .get("success")
            .get("tokens")
            .get("bearer")
            .get("access_token"),
            response.get("request_id")
        )


    except Exception as e:
        twoStepVerificationChallengeUrl = getTwoStepVerificationChallengeUrl(response)
        print("Unable to authenticate to Amazon Flex.")
        print(
            f"\nPlease try completing the two step verification challenge at \033[1m{twoStepVerificationChallengeUrl}\033[0m . Then try again."
        )
        print(
            "\nIf you already completed the two step verification, please check your Amazon Flex username and password in the config file and try again."
        )

