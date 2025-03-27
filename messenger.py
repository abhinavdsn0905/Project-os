from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import hmac

class SecurityVault:
    def generate_protection(self, security_phrase):
        entropy_seed = os.urandom(16)
        return {
            'encoded_secret': self._create_protected_seal(security_phrase, entropy_seed),
            'entropy_source': entropy_seed
        }

    def _create_protected_seal(self, phrase_input, entropy_seed):
        seal_generator = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=entropy_seed,
            iterations=100000,
            backend=default_backend()
        )
        return seal_generator.derive(phrase_input.encode())

    def validate_credentials(self, input_phrase, stored_seal, entropy_seed):
        new_seal = self._create_protected_seal(input_phrase, entropy_seed)
        return hmac.compare_digest(new_seal, stored_seal)