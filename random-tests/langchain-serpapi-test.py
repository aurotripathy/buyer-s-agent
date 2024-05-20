"""
get keys from server.dev (and on other place)
"""
import os
import pprint
from dotenv import load_dotenv

load_dotenv()
print(f'serper api key: {os.environ["SERPER_API_KEY"]}')

from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper()

print(search.run("Obama's first name?"))

