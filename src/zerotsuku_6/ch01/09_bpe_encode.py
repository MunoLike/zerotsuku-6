from zerotsuku_6.codebot.tokenizer import BPETokenizer

import numpy as np

tokenizer = BPETokenizer.load_from("src/zerotsuku_6/codebot/merge_rules.pkl")

text = open("src/zerotsuku_6/codebot/tiny_codes.txt").read()
ids = tokenizer.encode(text, show_progress=True)

ids_array = np.array(ids, dtype=np.uint16)
ids_array.tofile("src/zerotsuku_6/codebot/tiny_codes.bin")

print(f"トークンID数: {len(ids_array)}")
print(f"最初の20個のトークン: {ids_array[:20]}")