import requests
import allure
from enums.global_enums import GlobalErrorMessages


class BasePage:
    response = None
    response_json = None

    """ CRUD METHODS """

    @allure.step("GET request")
    def get_response(self, url):
        self.response = requests.get(url=url)
        self.response_json = self.response.json()

    @allure.step("POST request")
    def post(self, url, payload):
        self.response = requests.post(url=url, json=payload)
        self.response_json = self.response.json()

    @allure.step("DELETE request")
    def delete(self, url):
        self.response = requests.delete(url=url)
        self.response_json = self.response.json()

    """ ASSERTIONS """

    @allure.step("Check count if obtained posts")
    def check_count_obtained_posts(self):
        assert len(self.response.json()) == 100, GlobalErrorMessages.WRONG_COUNT_OBTAINED_POSTS.value

    @allure.step("Check response json is empty")
    def check_response_json_is_empty(self):
        assert self.response.json() == {}, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value

    @allure.step("Check status code is 200")
    def check_status_is_200(self):
        assert self.response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step("Check status code is 201")
    def check_status_is_201(self):
        assert self.response.status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step("Check object item:userId")
    def check_user_id(self, userId):
        assert self.response.json()['userId'] == userId, GlobalErrorMessages.WRONG_ELEMENT_VALUE.value

    @allure.step("Check object item:title")
    def check_title(self, title):
        assert self.response.json()['title'] == title, GlobalErrorMessages.WRONG_ELEMENT_VALUE.value

    @allure.step("Check object item:body")
    def check_body(self, body):
        assert self.response.json()['body'] == body, GlobalErrorMessages.WRONG_ELEMENT_VALUE.value

