import os
from pathlib import Path
from dotenv import load_dotenv

def find_secret_word_in_venv(key_word:str)->str|None:
    env_link= Path(__file__).resolve().parent[2] / '.venv' / '.env'
    print(env_link)
    load_dotenv(dotenv_path=env_link)
    key_find=os.getenv(key_word)
    if key_find is not None:
        return key_find
    return None

print(find_secret_word_in_venv('DATABASE_URL'))
