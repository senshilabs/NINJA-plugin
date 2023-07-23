from .service.common import COMMON, STRING
from .service.http import call_http

CATEGORY = "NINJA/Http"

HTTP_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
    "HEAD",
]


class HttpCall(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "method": (HTTP_METHODS,),
                "server_url": (STRING, {
                    "multiline": False,
                    "default": "localhost:8000",
                }),
                "headers": (STRING, {
                    "multiline": True,
                    "default": "Content-Type: application/json",
                }),
                "body": (STRING, {
                    "multiline": True,
                    "default": """
                        {
                          "title": "double-dollars is special form", 
                          "likeThis": "$$0"}
                    """,
                }),
                "params0": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params1": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params2": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params3": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params4": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params5": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params6": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params7": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params8": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
                "params9": (STRING, {
                    "multiline": False,
                    "default": "",
                }),
            },
        }

    RETURN_TYPES = (STRING,)
    RETURN_NAMES = ("resp",)

    OUTPUT_NODE = True
    CATEGORY = CATEGORY

    def execute(self, method, server_url, headers, body, params0, params1, params2, params3, params4, params5, params6,
                params7, params8, params9):
        return call_http(method, server_url, headers, body, params0, params1, params2, params3, params4, params5,
                         params6, params7, params8, params9)
