import os, sys

from zerotsuku_6.codebot.tokenizer import BPETokenizer

tokenizer = BPETokenizer.load_from("src/zerotsuku_6/codebot/merge_rules.pkl")
print("最初に学習された10個")
for token_id in range(256, 266):
    byte_seq = tokenizer.id_to_bytes[token_id]
    text = byte_seq.decode("utf-8")
    print(f"  ID {token_id}: '{text}'")

print("\n最後に学習された10個")
for token_id in range(990, 1000):
    byte_seq = tokenizer.id_to_bytes[token_id]
    text = byte_seq.decode("utf-8")
    print(f"  ID {token_id}: '{text}'")