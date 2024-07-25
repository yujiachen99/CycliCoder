import subprocess
import os
import tempfile
import re, json


def execute_java(code:str, timeout:float):

    def extract_class_name(code):
        match = re.search(r'public\s+class\s+(\w+)', code)
        if match:
            return match.group(1)  
        return None

    with tempfile.TemporaryDirectory() as tmpdirname:
        class_name = extract_class_name(code)
        if not class_name:
            return {"passed": False, "result": "compile_error: No public class name found in the provided Java code"} 
        
        code_path = os.path.join(tmpdirname, f"{class_name}.java")
        
        with open(code_path, "w") as file:
            file.write(code)
        
        # compile Java code
        compile_result = subprocess.run(["javac", code_path], capture_output=True, text=True)
        if compile_result.returncode != 0:
            
            return {"passed": False, "result": f"compile_error: {compile_result.stderr}"}
        
        # execute Java code
        try:
            exec_result = subprocess.run(["java", "-cp", tmpdirname, class_name], capture_output=True, text=True, timeout=timeout)
            if exec_result.returncode == 0:
                return {"passed": True, "result": exec_result.stdout}
            else:
                return {"passed": False, "result": exec_result.stderr}
            
        except subprocess.TimeoutExpired:
            return {"passed": False, "result": "timeout_error: Java code execution timed out"}



