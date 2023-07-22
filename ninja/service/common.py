class COMMON:
    FUNCTION = "execute"


MODEL = "MODEL"
VAE = "VAE"
CLIP = "CLIP"
CONDITIONING = "CONDITIONING"
LATENT = "LATENT"
IMAGE = "IMAGE"
MASK = "MASK"
INT = "INT"
STRING = "STRING"
FLOAT = "FLOAT"

CATEGORY = "NINJA"

# return 할때, Debug 모드이면 출력
DEBUG = True


def load_http_image(url):
    import requests
    import torch
    from PIL import Image
    from io import BytesIO
    import numpy as np
    content = requests.get(url).content
    i = Image.open(BytesIO(content))
    i = i.convert("RGB")
    image = np.array(i).astype(np.float32) / 255.0
    image = torch.from_numpy(image)[None,]
    return (image,)


def with_debug_log(*return_value):
    if DEBUG:
        print(return_value)
    return return_value
