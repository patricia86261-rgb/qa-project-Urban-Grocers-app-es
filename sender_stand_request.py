import data
import requests
import configuration

def post_new_user(user_body):
         return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                              json=user_body,
                       headers=data.headers)


def post_new_client_kit(kit_body,auth_token):
    curren_header = data.headers.copy()
    curren_header["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=curren_header)

post_new_client_kit(data.kit_body, auth_token="3d53e84a-2d09-4348-894a-d64c0887156a")














