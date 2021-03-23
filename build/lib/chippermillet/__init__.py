__doc__ = """Cryptography


import:
    >>> from chippermillet import encrypt
    >>> from chippermillet import decrypt


encrypt:

    >>> e = encrypt(b'data',  'secret', 60000)

decrypt:

    >>> decrypt(e, 'secret', 60000)
    'data'

Author: Madhava-mng
"""
from chippermillet.core import encrypt, decrypt
