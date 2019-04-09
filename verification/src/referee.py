from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "morse_encoder"
    FUNCTION_NAMES = {
        "python_3": "morse_encoder",
        "js_node": "morseEncoder"
    }
    ENV_COVERCODE = {
        
    }