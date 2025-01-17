import datetime
from typing import List

from pydantic import BaseModel, validator


class Content(BaseModel):
    title: str
    description: str
    link: str
    created: str
    tags: List[str]
    meta: dict

    @validator("link")
    def link_must_contain_http(cls, v):
        if "http" not in v:
            raise ValueError(f"must contain `http`. received: {v}")
        return v

    @validator("tags")
    def tags_may_not_be_empty(cls, v):
        if len(v) == 0:
            raise ValueError(f"tags cannot be empty. received: {v}")
        return v

    @validator("created")
    def created_string_must_be_date_parseable(cls, v):
        try:
            datetime.datetime.strptime(v, "%Y-%m-%d")
        except:
            raise ValueError(f"created date must be parse-able. received: {v}")
        return v
