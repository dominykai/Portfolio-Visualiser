from typing import Optional

from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    api_key: str
    private_key: Optional[str] = None

class ApiKeyCreate(ApiKeyBase):
    pass

class ApiKeySchema(ApiKeyBase):
    pass