import re
from typing import List, Tuple, Dict, Optional, Callable

def extract_code_block(content: str) -> Tuple[bool, str]:
    pattern = re.escape("```Java") + r"(.*?)" + re.escape("```")
    match = re.findall(pattern, content, re.DOTALL|re.IGNORECASE)
    if match:
        return True, match[0].strip()
    
    return False, ""

def check_complete(content: str) -> bool:
    
    start = content.find("```")
    if start != -1:
        end = content.find("```", start+4)
        if end != -1:
            return True
        else:
            return False    
    else:
        return False
    

def judge_language(content: str) -> str:
    pattern = re.escape("```Java") + r"(.*?)"
    match = re.findall(pattern, content, re.DOTALL|re.IGNORECASE)
    
    if pattern:
        return "java"
    else:
        return "unknown"