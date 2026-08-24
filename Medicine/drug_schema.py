from pydantic import BaseModel,Field
import uuid

class Medicine(BaseModel):
    drug_id: uuid.UUID
    drug_name: str
    ingredient: str  = Field(description='成分')
    description: str = Field(description='性状')
    indication: str  = Field(description='适应症')
    packaging: str   = Field(description='包装')
    storage_conditions:str = Field(description="存贮方式")

class UserQuery(BaseModel):
    text:str
