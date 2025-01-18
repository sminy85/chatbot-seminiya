from langchain_community.chat_models.bedrock import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def bedrock_chatbot():
    bedrock_llm = BedrockChat(
        credentials_profile_name='default',
        model_id='anthropic.claude-3-5-sonnet-20240620-v1:0',
        model_kwargs={
            "temperature": 0.5,  # 샘플링 온도
            "top_p": 1,          # 토큰 확률 분포
            "top_k": 250         # 고려할 상위 토큰 개수
        }
    )
    return bedrock_llm

def buff_memory():
    memory = ConversationBufferMemory(max_token_limit=200)  # LLM 제거
    return memory

def cnvs_chain(input_text, memory):
    bedrock_llm = bedrock_chatbot()
    cnvs_chain = ConversationChain(llm=bedrock_llm, memory=memory, verbose=True)

    chat_reply = cnvs_chain.predict(input=input_text)
    return chat_reply