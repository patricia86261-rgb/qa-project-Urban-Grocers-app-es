import data
import sender_stand_request


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body =get_kit_body(name)
    response= sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(kit_body)
    print("imprimiendo kitbody ", kit_body)
    response = sender_stand_request.post_new_client_kit(kit_body)
    print(response.json())
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid symbol"


def test_create_kit_1_letter_in_name():
    positive_assert("a")

def test_create_kit_511_letter_in_name():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_0_letter_in_name():
    negative_assert_code_400("")


def test_create_kit_512_letter_in_name():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid symbol"


def test_create_kit_special_symbol_letter_in_name():
     positive_assert("\"№%@\",")


def test_create_kit_allow_spaces_letter_in_name():
   positive_assert(" A Aaa ")


def test_create_kit_allow_number_letter_in_name():
    positive_assert("123")


def test_create_kit_the_request_does_not():
    kit_body = get_kit_body({})
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400



def test_create_kit_that_a_different_parameter_is_passed():
    kit_body = get_kit_body(name=123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400











