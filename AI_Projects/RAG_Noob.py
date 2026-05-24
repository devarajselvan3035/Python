from langchain_community.document_loaders import PyPDFLoader
from pprint import pprint

path = "/home/devselvan/Downloads/Build a Large Language Model (From Scratch) MEAP V08 - Unknown(1).pdf"

loader = PyPDFLoader(path)
pages = loader.load()
pprint(pages[0].metadata)
