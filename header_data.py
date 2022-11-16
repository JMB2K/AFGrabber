
# Get this info by using Charles Proxy or something similar, headers will need to be updated every time you run the script
headers = {
    'x-amz-access-token': 'ACCESS TOKEN',
    'X-Amzn-RequestId': 'REQUEST ID',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/S3B1.220318.003) RabbitAndroid/3.72.1.25.0',
    'X-Flex-Client-Time': '1650322099698',
    'x-flex-instance-id': 'INSTANCE ID',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Authorization': 'RABBIT3-HMAC-SHA256 SignedHeaders=host;x-amz-access-token;x-amz-date;x-amzn-requestid,Signature=SIGNATURE',
    'Host': 'flex-capacity-na.amazon.com',
    'X-Amz-Date': '20220418T174820Z',
}

# Leave these here to delete the unneeded headers that will cause problems running the script
del headers["X-Flex-Client-Time"]
del headers["X-Amz-Date"]
