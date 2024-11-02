import openai
bing.api_key = "3df2073b006c447dbc39a6ffbf6c972c"
openai.api_key = "ssk-proj-QoI1iJqn1QjuPtVzTsiX3okJDKahwTMc5M8ptrC13kjmXr2Uao_oVrXJsk-proj-joJpcgEvRE39TjcXeV0k6lrQRblyxlwMmtXxHvZkR45zDChgB7WOVzQNN0rDtDaH5aD_sMxgpOT3BlbkFJP78PVDmhTP03wx2iAT4y1gViATibTN0HwXdnBTFPRp0ZsEJ0Lvam8B5FPcjNxSO9OR5sTpY-0A"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, world!"}
        ],
        max_tokens=5
    )
    print(response)
except openai.error.OpenAIError as e:
    print(f"Error: {e}")
