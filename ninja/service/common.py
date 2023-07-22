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


def with_debug_log(**return_value):
    if DEBUG:
        print(return_value)
    return return_value
