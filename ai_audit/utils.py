def chunk_data(data, size=4):
    for i in range(0, len(data), size):
        yield data[i:i+size]