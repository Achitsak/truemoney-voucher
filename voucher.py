from curl_cffi import requests

class angbpao:
    def __init__(self):

        self.session = requests.Session()

    def redeem(self, phnumber, voucher):
        try:    
            voucher_code = voucher.split("v=")[-1]
            
            if voucher_code:
                try:

                    headers = {
                        "accept": "application/json",
                        "accept-language": "th-TH,th;q=0.9,en;q=0.8",
                        "content-type": "application/json",
                    }

                    response = requests.post(f"https://gift.truemoney.com/campaign/vouchers/{voucher_code}/redeem",headers=headers, json = {"mobile": str(phnumber)}, impersonate="chrome")

                    if response:

                        result = response.json()

                        if "VOUCHER_NOT_FOUND" in result['status']['code']:
                            return {"succes": False,"msg":"INVAILD_VOUCHER"}
                        
                        if "SUCCESS" == result['status']['code'] :
                            return{'succes': True, 'amount': int(float(result['data']['my_ticket']['amount_baht'].replace(",",""))),'owner_full_name': result['data']['owner_profile']['full_name'],'code': voucher_code}

                        return {"succes": False,"msg":result['status']['code']}
                except Exception as e:
                    raise ValueError(f"error: {e}")
                
        except Exception as e:
            raise ValueError(f"error: {e}")
