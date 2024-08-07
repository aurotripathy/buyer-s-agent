"""
Taking guidance from...https://simmering.dev/blog/structured_output/
Of all the libraries, marvin appears to be the simplest to work with and works with OpenAI,
The outlines library doesn't...yet.
"""

from typing import Literal
from pydantic import BaseModel
import marvin
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
print(os.environ["OPENAI_API_KEY"])

import marvin
marvin.settings.openai.api_key = os.environ["OPENAI_API_KEY"]

text = """I'm looking for a three bedroom, two bath house in the 95035 zipcode, minimum sqaure footage of 2000sqft. and maximum 2500sqft"""

marvin.settings.openai.chat.completions.model = "gpt-3.5-turbo"


class Entity(BaseModel):
    name: str
    label: Literal["BEDROOM", "BATHROOM", "ZIPCODE", "HOME_SIZE"]


entities = marvin.extract(
    text,
    target=Entity,
    model_kwargs={"temperature": 0.0},
)

print(entities)

# output
# [Entity(name='3', label='BEDROOM'), Entity(name='2', label='BATHROOM'), Entity(name='95035', label='ZIPCODE'), Entity(name='2000-2500', label='HOME_SIZE')]
