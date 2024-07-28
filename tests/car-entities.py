"""
Taking guidance from...https://simmering.dev/blog/structured_output/
Of all the libraries, marvin appears to be the simplest and works with OpenAI;
The outlines library, another choice, doesn't work with OpenAI...yet
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



marvin.settings.openai.chat.completions.model = "gpt-3.5-turbo"


class CarEntity():
    def __init__(self) -> None:
        pass
 
    def get_car_entities(self, text):
        class Entity(BaseModel):
            name: str
            label: Literal["YEAR", "MODEL", "PRICE", "MILEAGE"]

        entities = marvin.extract(
            text,
            target=Entity,
            model_kwargs={"temperature": 0.0},
        )
        return entities
    

text = """
Title: KIA Optima 2014 
  Description: Elegant, reliable car for sale 4 cylinder, 2.4L, (31-32mpg average),with 65k miles, salvage title due to minor accident (front bumper was replaced and repainted). Tow hitch installed -great for bike racks). Smogged and Ready for a new owner. serious buyers welcome
  Price: 9600
"""

car_entity = CarEntity()
entities = car_entity.get_car_entities(text)
for entity in entities:
    print(f'label: {entity.label}, value: {entity.name}')