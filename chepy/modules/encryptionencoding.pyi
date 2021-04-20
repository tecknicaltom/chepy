from ..core import ChepyCore
from typing import Any, TypeVar

jwt: Any
AES: Any
ARC4: Any
DES: Any
DES3: Any
Blowfish: Any
EncryptionEncodingT = TypeVar('EncryptionEncodingT', bound='EncryptionEncoding')

class EncryptionEncoding(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def rotate(self: EncryptionEncodingT, rotate_by: int) -> EncryptionEncodingT: ...
    def rotate_bruteforce(self: EncryptionEncodingT) -> EncryptionEncodingT: ...
    def rot_13(self: EncryptionEncodingT) -> EncryptionEncodingT: ...
    def rot_47(self: EncryptionEncodingT) -> EncryptionEncodingT: ...
    def xor(self: EncryptionEncodingT, key: str, key_type: str=..., ascii: bool=...) -> EncryptionEncodingT: ...
    def xor_bruteforce(self: EncryptionEncodingT, length: int=...) -> EncryptionEncodingT: ...
    def jwt_decode(self: EncryptionEncodingT) -> EncryptionEncodingT: ...
    def jwt_verify(self: EncryptionEncodingT, secret: str, algorithm: list=...) -> EncryptionEncodingT: ...
    def jwt_sign(self: EncryptionEncodingT, secret: str, algorithms: str=...) -> EncryptionEncodingT: ...
    def jwt_bruteforce(self: EncryptionEncodingT, wordlist: str, b64_encode: bool=..., algorithm: list=...) -> Any: ...
    def rc4_encrypt(self: EncryptionEncodingT, key: str, hex_key: bool=...) -> EncryptionEncodingT: ...
    def rc4_decrypt(self: EncryptionEncodingT, key: str, hex_key: bool=...) -> EncryptionEncodingT: ...
    def des_encrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def des_decrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def triple_des_encrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def triple_des_decrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def aes_encrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def aes_decrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def blowfish_encrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def blowfish_decrypt(self: EncryptionEncodingT, key: str, iv: str=..., mode: str=..., hex_key: bool=..., hex_iv: bool=...) -> Any: ...
    def vigenere_encode(self: EncryptionEncodingT, key: str) -> EncryptionEncodingT: ...
    def vigenere_decode(self: EncryptionEncodingT, key: str) -> EncryptionEncodingT: ...
    def affine_encode(self: EncryptionEncodingT, a: int=..., b: int=...) -> EncryptionEncodingT: ...
    def affine_decode(self: EncryptionEncodingT, a: int=..., b: int=...) -> EncryptionEncodingT: ...
    def atbash_encode(self: EncryptionEncodingT) -> EncryptionEncodingT: ...
    def atbash_decode(self: EncryptionEncodingT) -> EncryptionEncodingT: ...
    def to_morse_code(self: EncryptionEncodingT, dot: str=..., dash: str=..., letter_delim: str=..., word_delim: str=...) -> Any: ...
    def from_morse_code(self: EncryptionEncodingT, dot: str=..., dash: str=..., letter_delim: str=..., word_delim: str=...) -> Any: ...