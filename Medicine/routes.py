from fastapi import APIRouter, HTTPException
from Langchain.medicine.medicine_schema import Medicine,UserQuery
from Langchain.llm.DASHSCOPE_AI import structed_whale_ai
drug_router = APIRouter()

@drug_router.post("/medicine",response_model=Medicine)
async def medicine(medicine_data: UserQuery):

    from Langchain.llm.prompt import chat_prompt_template

    chain = chat_prompt_template|structed_whale_ai


    try:
        result = await chain.ainvoke({"input":medicine_data.text})
        """
        return a object to your pydantic class
        """
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
