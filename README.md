Cryptography


## Installation

```bash
$ python3 -m pip install chippermillet
```

##import:

```python
    >>> from chippermillet import encrypt
    >>> from chippermillet import decrypt
```

##encrypt:


```python
    >>> e = encrypt(b'data',  'secret', 60000)
```

##decrypt:


```python
    >>> decrypt(e, 'secret', 60000)
    'data'
```

