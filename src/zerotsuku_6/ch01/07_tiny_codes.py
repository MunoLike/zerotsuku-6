import os, sys
# os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
# sys.path.append(".")


import pickle
from zerotsuku_6.codebot.tokenizer import train_bpe 

vocab_size=1000
text = open("src/zerotsuku_6/codebot/tiny_codes.txt").read()
merge_rules=train_bpe(text, vocab_size)

with open("src/zerotsuku_6/codebot/merge_rules.pkl", "wb") as f:
    pickle.dump(merge_rules, f)
