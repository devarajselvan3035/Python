import torch
from pypdf import PdfReader
import pprint


reader = PdfReader(
    "/home/devselvan/Downloads/NIPS-2017-attention-is-all-you-need-Paper.pdf"
)
page = reader.pages[0]
pprint.pprint(len(reader.pages))

# print(page.extract_text())
