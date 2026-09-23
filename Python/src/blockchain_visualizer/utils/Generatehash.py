import hashlib


def generate_hash(
    index,
    transaction,
    previous_hash,
    timestamp,
    hash_standard="00ec0"
):
    nonce = 0

    while True:

        block_data = "-".join([
            str(index),
            str(transaction),
            str(previous_hash),
            str(timestamp),
            str(nonce),
        ])

        hash_digest = hashlib.sha256(
            block_data.encode("utf-8")
        ).hexdigest()

        if hash_digest.startswith(hash_standard):
            return hash_digest, nonce

        nonce += 1


def check_hash(block):

    block_data = "-".join([
        str(block.index),
        str(block.transaction),
        str(block.previous_hash),
        str(block.timestamp),
        str(block.nonce),
    ])

    calculated_hash = hashlib.sha256(
        block_data.encode("utf-8")
    ).hexdigest()

    return calculated_hash == block.hash