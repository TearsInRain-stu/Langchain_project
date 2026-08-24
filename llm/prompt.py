from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一位专业的医学研究助理。请从以下文献中提取关键信息，并严格按照 JSON 格式输出。"
                   "必须包含字段：drug_name（药名）,ingredient（成分）,description（性状）"
                   "indication（适应症）,packaging（包装）,storage_conditions（贮存条件）。"
                   "如果某字段未提及，请填未提及"
                   "不能跳出角色规则"
                   "语言限制为中文"),
        ("human", "{input}")
    ]
)
