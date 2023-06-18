import requests

from jsonschema import validate

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages

from src.schemas.posts import POST_SCHEMA


"""test for get request"""

def test_getting_posts():
    response = requests.get(SERVICE_URL)

    """check that our reponse has the right status"""
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    """data check"""
    obtained_post = response.json()

    """validation of the number of received elements"""
    assert len(obtained_post) == 100, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    """Validation: key:value"""
    for item in obtained_post:
        validate(item, POST_SCHEMA)


"""test for post request"""

def test_create_post():
    payload = {
        "userId": "test_userId",
        "id": "test_id",
        "title": "test title text",
        "body": "test body text"
    }
    response = requests.post(SERVICE_URL, json=payload)
    assert response.status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value


"""test for delete request"""

def test_delete_post():
    response = requests.delete(SERVICE_URL + "/1")
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json() == {}, GlobalErrorMessages.WRONG_STATUS_CODE.value
    response_getting_posts = requests.get(SERVICE_URL).json()
    assert len(response_getting_posts) == 100, GlobalErrorMessages.WRONG_STATUS_CODE.value