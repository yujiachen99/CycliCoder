import json
from utils import *
from check import *

file_path = 'data.jsonl'

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        generation = data['generation']
        if check_complete(generation):
            language = judge_language(generation)
            status, code = extract_code_block(generation)
            if status and language == "java":
                execute_res = execute_java(code,timeout=30)
            else:
                execute_res = "Language not supported"
            print(execute_res)
        else:
            print("Generation is not complete")
                
