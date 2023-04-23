import openai
#https://platform.openai.com/docs/guides/chat/introduction
#질문 유의사항
#당신의 지시를 더 명확하게 만드십시오
# 답변을 원하는 형식을 지정하십시오.
# 답을 결정하기 전에 모델에게 단계별로 생각하거나 장단점에 대해 토론하도록 요청하십시오.
openai.api_key="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"
completion = openai.ChatCompletion.create(
    model ="gpt-3.5-turbo", 
    #현재 사용가능한 model https://platform.openai.com/docs/models/gpt-3
    #GPT-4
    #GPT-3.5
    #GPT-3
    #CODEX : 코드 생성 모델
    #DAL-E : 자연어 이미지
    #파인튜닝 모델이나, 오디오 모델도 있으니 확인해보자
    messages=[
    #role은 총 3가지가 있음
        #system : 모델에 직접적으로 명령하는 것, 파라미터 초기화나 assistant가 기억시켜놓은 것에 대한 초기화? 혹은 gpt에 역할을 부여할 수있음 (예를 들어 선생님이 가르치듯이)
        #user : 사용자가 직접 묻는 것
        #assistant : 사전지식을 학습케함, 예시는 아래와 같음
    {        
        "role" : "system", 
        "content": "Who owns Tesla?",
    },
    {
        "role" : "assistant",
        "content" : "Elon Musk owns Tesla",        
    },
    {
        "role" : "user",
        "content" : "How much did he pay for it?",        
    }
],
)
print(completion)



#답변
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Elon Musk did not initially buy Tesla. He led a $7.5 million financing round in February 2004 and joined the board of directors. In 2008, he became the CEO of Tesla after investing additional funds in the company.",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1679322882,
#   "id": "chatcmpl-6wAssggwnnmxkZhIILrzt1q5s4rCo",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 51,
#     "prompt_tokens": 34,
#     "total_tokens": 85
#   }
# }