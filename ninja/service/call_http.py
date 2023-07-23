from .common import with_debug_log


def call_http(method, server_url, headers, body, params0, params1, params2, params3, params4, params5, params6,
              params7, params8, params9):
    import requests
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
    for k, v in params.items():
        server_url = server_url.replace(k, v)
        body = body.replace(k, v)
        headers = headers.replace(k, v)

    headers = dict([x.split(":") for x in headers.split(";") if x != ""])
    headers = {k.strip(): v.strip() for k, v in headers.items()}
    import json
    try:
        body = json.loads(body)
    except:
        body = json.loads("{" + body + "}")
    print(headers)
    print(body)

    if method == "GET":
        resp = requests.get(server_url, headers=headers)
    elif method == "POST":
        resp = requests.post(server_url, headers=headers, json=body)
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
