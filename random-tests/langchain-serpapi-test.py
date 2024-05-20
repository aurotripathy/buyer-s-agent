"""
get keys from server.dev (and on other place)
"""
import os
import pprint

# os.environ["SERPER_API_KEY"] = "a2470c4bd9f80493bb2c3c2fc5bbd01873e0a429df4d4081ff1ec161fcb0ed1e"
os.environ["SERPER_API_KEY"] = "f82a9006ece734254185cccc35ba0bbacaaca8f1"

from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper()

print(search.run("Obama's first name?"))

