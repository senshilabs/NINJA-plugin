import requests

from ninja.service.common import with_debug_log


def call_http(method, server_url, headers, body, params0, params1, params2, params3, params4, params5, params6,
              params7, params8, params9):
    params = {
        "$$0": params0,
        "$$1": params1,
        "$$2": params2,
        "$$3": params3,
        "$$4": params4,
        "$$5": params5,
        "$$6": params6,
        "$$7": params7,
        "$$8": params8,
        "$$9": params9,
    }

    for k, v in params:
        server_url = server_url.replace(k, v)
        body = body.replace(k, v)
        headers = headers.replace(k, v)

    if method == "GET":
        resp = requests.get(server_url, headers=headers)
    elif method == "POST":
        resp = requests.post(server_url, headers=headers, data=body)
    elif method == "PUT":
        resp = requests.put(server_url, headers=headers, data=body)
    elif method == "DELETE":
        resp = requests.delete(server_url, headers=headers)
    elif method == "PATCH":
        resp = requests.patch(server_url, headers=headers, data=body)
    elif method == "HEAD":
        resp = requests.head(server_url, headers=headers)
    else:
        raise Exception("Unknown method: {}".format(method))

    return with_debug_log(resp.text)
