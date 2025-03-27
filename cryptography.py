import sqlite3

class DigitalVault:
    def __init__(self, vault_file):
        self.vault_connection = sqlite3.connect(vault_file)
        self.vault_access = self.vault_connection.cursor()

    def establish_vault(self):
        self.vault_access.execute("""
            CREATE TABLE IF NOT EXISTS identity_registry (
                identity_tag TEXT PRIMARY KEY,
                protected_seal BLOB NOT NULL,
                entropy_seed BLOB NOT NULL,
                contact_reference TEXT
            )
        """)
        self.vault_connection.commit()

    def identity_exists(self, identity_tag):
        self.vault_access.execute(
            "SELECT identity_tag FROM identity_registry WHERE identity_tag = ?",
            (identity_tag,)
        )
        return self.vault_access.fetchone() is not None

    def store_identity(self, identity_tag, protected_seal, entropy_seed, contact_ref):
        self.vault_access.execute(
            "INSERT INTO identity_registry VALUES (?, ?, ?, ?)",
            (identity_tag, protected_seal, entropy_seed, contact_ref)
        )
        self.vault_connection.commit()

    def retrieve_protection(self, identity_tag):
        self.vault_access.execute(
            "SELECT protected_seal, entropy_seed, contact_reference FROM identity_registry WHERE identity_tag = ?",
            (identity_tag,)
        )
        result = self.vault_access.fetchone()
        if result:
            return {
                'encoded_secret': result[0],
                'entropy_source': result[1],
                'contact_node': result[2]
            }
        return None