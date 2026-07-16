import data
import sender_stand_request


def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()['authToken']

def positive_asert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201


def negative_asert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 400

def test_1_kit_name_whith_one_letter():
    new_kit_body=get_kit_body("a")
    positive_asert(new_kit_body)


def test_2_kit_allowed_limit_of_511_characters():
    new_kit_body=get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_asert(new_kit_body)

def test_3_kit_the_number_of_characters_is_less_than_the_alloed_amount():
    new_kit_body=get_kit_body("0")
    negative_asert(new_kit_body)


def test_4_kit_the_number_of_characters_is_of_512():
    new_kit_body=get_kit_body("AbcdabababababacdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_asert(new_kit_body)

def test_5_kit_special_characters_are_allowed():
    new_kit_body=get_kit_body("№%@")
    positive_asert(new_kit_body)


def test_6_kit_spaces_are_allowed():
    new_kit_body=get_kit_body("A  Aaa")
    positive_asert(new_kit_body)


def test_7_kit_numbers_are_allowed():
    new_kit_body=get_kit_body("123")
    positive_asert(new_kit_body)

def test_8_kit_the_parameter_is_not_passed_in_the_request():
    new_kit_body=get_kit_body({})
    new_kit_body.pop("name", None)
    negative_asert(new_kit_body)


def test_9_kit_the_parameter_is_different():
    new_kit_body=get_kit_body({"name":123})
    negative_asert(new_kit_body)






