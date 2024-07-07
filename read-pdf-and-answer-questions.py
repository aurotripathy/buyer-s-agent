
#code to read and Q&A a pdf
# %pip install pypdf
from pypdf import PdfReader

reader = PdfReader("./data/natural_hazard_disclosure_statement_NHD.pdf")
number_of_pages = len(reader.pages)
text_pages = []
for page in reader.pages:
    text_pages.append(page.extract_text())

full_text = ''.join(page.extract_text() for page in reader.pages)
# print(full_text[:2155])


# NOTE: local llm use: to find which model names you have, use cli tool:  `ollama list`
# ensure its being served
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
      model='llama3',
      base_url="http://localhost:11434/v1",
      api_key="NA"
)


import json
import requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "llama3"  # TODO: update this for whatever model you wish to use


def chat(messages):
    r = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={"model": model, "messages": messages, "stream": True},
	stream=True
    )
    r.raise_for_status()
    output = ""

    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            # the response streams one token at a time, print that as we receive it
            # print(content, end="", flush=True)

        if body.get("done", False):
            message["content"] = output
            return message


def main():
    for page_num in range(number_of_pages):
        print(f'Page Number:{page_num}')
        page_text = text_pages[page_num]
        final_prompt = f"""Here is a page from the natural hazards disclosure document: <document>{page_text}</document>.
- Check if the page mentions wildfires.
- If the page mentions wildfires, generate a json key value pair, "wildfire": "yes".
- Summarize the page as it relates to wildfires? Use key value pair "about_wildfire": "<your summary>".
- If the page does NOT mention wildfires, stay silent, do NOT output anything.

"""
        messages = []     
        messages.append({"role": "user", "content": final_prompt})
        response = chat(messages)
        print(response['content'])
    print("\n\n")

print(f'Page count:{number_of_pages}')


if __name__ == "__main__":
    main()