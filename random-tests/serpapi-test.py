import serpapi
# search = serpapi.search({
#     "q": "coffee", 
#     "location": "Austin,Texas",
#     "api_key": "a2470c4bd9f80493bb2c3c2fc5bbd01873e0a429df4d4081ff1ec161fcb0ed1e"
# })
search = serpapi.search({
    "q": "Obama's first name", 
    "api_key": "a2470c4bd9f80493bb2c3c2fc5bbd01873e0a429df4d4081ff1ec161fcb0ed1e"
  })
result = search.as_dict()
print(search)