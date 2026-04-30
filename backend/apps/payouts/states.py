PROCESS = {
    "pending": ["Processing"],
    "processed": ["completed", "failed"],
}


def val_tx(old, new):
    if new not in PROCESS.get(old, []):
        raise Exception("Invalid Transaction")
