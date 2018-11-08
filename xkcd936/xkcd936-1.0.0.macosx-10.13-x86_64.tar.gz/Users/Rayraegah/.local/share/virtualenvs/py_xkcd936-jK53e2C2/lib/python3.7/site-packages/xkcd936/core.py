import hashlib
import os.path
import sys

# Set unicode datatype
if sys.version_info.major == 3:
    unicode = str

# Set labels for word types (mapped to a text file in ./data)
WORD_TYPES = ("article", "adjective", "animal")

# Creates phrase templates using word types
TEMPLATES = (
    ("article", "adjective", "adjective", "animal"),
    ("adjective", "article", "adjective", "animal"),
)

WORDS_BY_TYPE = {}
_base_path = os.path.dirname(__file__)

for word_type in WORD_TYPES:
    with open(os.path.join(_base_path, "data/%s.txt" % word_type), "r") as f:
        WORDS_BY_TYPE[word_type] = [word.strip() for word in f.readlines()]


def bytes_to_int(b1, b2, b3, b4):
    return (b1 << 24) | (b2 << 16) | (b3 << 8) | b4


def get_slots(input_str):
    # Converts unicode into a byte string
    if isinstance(input_str, unicode):
        input_str = input_str.encode()

    md5 = hashlib.md5()
    md5.update(input_str)
    digest = [b for b in md5.digest()]

    return (
        bytes_to_int(*digest[0:4]),
        bytes_to_int(*digest[4:8]),
        bytes_to_int(*digest[8:12]),
        bytes_to_int(*digest[12:16]),
    )


def visualize(input_str):
    """
    Convert hashes and words into visualizations.
    """
    slots = get_slots(input_str)
    template = TEMPLATES[slots[3] % len(TEMPLATES)]

    words = []
    for idx, word_type in enumerate(template):
        options = WORDS_BY_TYPE[word_type]
        words.append(options[slots[idx] % len(options)])

    return " ".join(words)
