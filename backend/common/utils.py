import uuid


def gen_idempotency_key():
    return str(uuid.uuid4())
