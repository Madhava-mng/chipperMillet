from base64 import b64encode, b64decode
from hashlib import sha512
from binascii import Error as bError

edata = {
        101: "[required] base64 , set base64=False",
        102: "[required] bytes like, use 'str'.encode()",
        }

def check_order(ordering):
    if(ordering < 0):
        return check_order(200000 + ordering)
    if(ordering > 200000):
        return check_order(ordering - 200000)
    return ordering

def encrypt(bstring, passwd="", rotate=0, base64=True):
    """
    >>> encrypt(b"data hear", 'secret', 5000)
    """
    passwd = sha512((str(passwd)+"$?").encode()).hexdigest()
    mkvsp = 1
    mkpas_up = 1
    mkpas_down = 1
    ordering = 0
    padding = 0
    tmp = ""
    try:
        for i in range(1, 20):
            if(rotate%i == 0):
                mkvsp = i           # mkvsp

        # password initialization
        for i in passwd:
            if(i.isdigit()):
                mkpas_up += 1
            else:
                mkpas_down += 1    # mkpas_up ,  mkpas_down

        for i in bstring.decode():
            if(padding):
                ordering = ord(i) + (rotate + mkpas_up)
                padding = 0
            else:
                padding = 1
                ordering = ord(i) - (rotate + mkpas_down)

            ordering = check_order(ordering)

            tmp += chr(ordering)

        if(base64):
            return b64encode(tmp.encode())
        return tmp.encode()
    except AttributeError:
        error = 102
    if(error == 102):
        raise Exception(edata[102])

def decrypt(bstring, passwd="", rotate=0, base64=True):
    """
    >>> decrypt(b'base64enc', 'secret', 5000)
    """
    passwd = sha512((str(passwd)+"$?").encode()).hexdigest()
    mkvsp = 1
    mkpas_up = 1
    mkpas_down = 1
    ordering = 0
    padding = 0
    tmp = ""
    try:
        if(base64):
            bstring = b64decode(bstring)

        for i in range(1, 20):
            if(rotate%i == 0):
                mkvsp = i           # mkvsp

        # password initialization
        for i in passwd:
            if(i.isdigit()):
                mkpas_up += 1
            else:
                mkpas_down += 1    # mkpas_up ,  mkpas_down
        for i in bstring.decode():
            if(padding):
                ordering = ord(i) - (rotate + mkpas_up)
                padding = 0
            else:
                padding = 1
                ordering = ord(i) + (rotate + mkpas_down)

            ordering = check_order(ordering)

            tmp += chr(ordering)

        return tmp.encode()
    except bError:
        error = 101
    except AttributeError:
        error = 102

    if(error == 101):
        raise Exception(edata[101])
    elif(error == 102):
        raise Exception(edata[102])

