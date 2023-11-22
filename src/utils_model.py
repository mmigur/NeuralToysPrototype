import g4f

from src import config

def get_promt(promt_content: str) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt_content}],
        stream=config.STREAM,
    )
    
    return "".join(response)