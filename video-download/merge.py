import shutil
import os

chunks = os.listdir('./josee')

with open('merged.ts', 'wb') as merged:
    for chunk in chunks:
        print(f"merging {chunk} ...")
        with open(os.path.join('./josee', chunk), 'rb') as chunkfile:
            shutil.copyfileobj(chunkfile, merged)