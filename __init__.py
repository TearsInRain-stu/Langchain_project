from fastapi import FastAPI
from Langchain.medicine.routes import drug_router


version = "1.0"
app = FastAPI(
    title="Langchain API",
    version=version,
    description="Langchain API",
)


app.include_router(
    drug_router,
    prefix=f"/api/{version}"
)


