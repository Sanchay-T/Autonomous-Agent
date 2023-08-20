import time
import uuid
import hashlib

SALT = "mysecretsaltvalue"

def generate_unique_key():
    timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
    random_value = str(uuid.uuid4())  # Random UUID
    unique_key = f"{timestamp}-{random_value}-{SALT}"
    hashed_key = hashlib.sha256(unique_key.encode()).hexdigest()
    return hashed_key





