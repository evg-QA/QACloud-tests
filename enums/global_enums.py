from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected"
    WRONG_COUNT_OBTAINED_POSTS = "Number of elements is not equal to expected"
    WRONG_ELEMENT_VALUE = "Value of item is not equal to expected"
    WRONG_USER_ID = "userId less or equal zero"
