import allure
from base.base_page import BasePage
from base.post_model import CreatePost
from utils.urls import POSTS_URL

@allure.title('Get all posts')
def test_get_posts():
    get_posts = BasePage()
    get_posts.get_response(POSTS_URL)
    get_posts.check_status_is_200()
    get_posts.check_count_obtained_posts()

@allure.title('Create a new post')
def test_create_post():
    create_post = BasePage()
    payload = CreatePost().model_dump()
    create_post.post(POSTS_URL, payload=payload)
    create_post.check_status_is_201()
    create_post.check_user_id(payload['userId'])
    create_post.check_title(payload['title'])
    create_post.check_body(payload['body'])

@allure.title('Delete all posts')
def test_delete_posts():
    delete_post = BasePage()
    delete_post.delete(POSTS_URL + '/101')
    delete_post.check_status_is_200()
    delete_post.check_response_json_is_empty()
    delete_post.get_response(POSTS_URL)
    delete_post.check_count_obtained_posts()
