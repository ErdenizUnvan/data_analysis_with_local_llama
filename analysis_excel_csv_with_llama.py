from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
import os
import pandas as pd
import requests

# Disable Docker globally
os.environ["AUTOGEN_USE_DOCKER"] = "0"

#filename = 'heart.csv'
file_path = 'C:/Users/Dell/llama3_2/coding/heart.csv'

df = pd.read_csv(file_path)
data = df.to_string()

# Ensure the working directory exists
if not os.path.exists("coding"):
    os.makedirs("coding")

# Local executor is defined
executor = LocalCommandLineCodeExecutor(
    timeout=60,  # Maximum execution time is 60 seconds
    work_dir="coding"  # Directory where the code will run
)

# Initialize the ConversableAgent
agent = ConversableAgent(
    name="code_executor_agent",
    code_execution_config={"executor": executor},
    default_auto_reply="Code executed successfully.",
)

def generate_code_with_llama_execute_with_autogen(question, file_path, data):
    try:
        url = 'http://127.0.0.1:8000/ai/predict'
        query = f"The following dataset is stored at {file_path}:\nDataframe is {data}\nWrite a Python script for the task below:\nLoad the CSV and {question} for the file named: {file_path}\n"
        query_params = {'query': query}
        response = requests.get(url, params=query_params)

        # Validate response
        if response.status_code != 200:
            raise ValueError(f"API request failed with status code {response.status_code}")

        #outputs = response.json().get('response', {}).get('text', '')
        outputs=response.json()['response']['text']
        if not outputs:
            raise ValueError("No response text returned from the API.")

        # Extract Python code from the response
        if 'python' in outputs:
            number = outputs.index('python')
            number1 = outputs.index('```')
            number2 = outputs.find('```', number1 + 1)
            code = outputs[number + 6:number2]
        else:
            number1 = outputs.index('```')
            number2 = outputs.find('```', number1 + 1)
            code = outputs[number1 + 3:number2]

        print(code)

        print("\nExecuting the Generated Code with Executor...\n")
        response = agent.run_code(code)
        # Clean and display the result output
        if isinstance(response, tuple):
            _, raw_output, _ = response
            clean_output = raw_output.replace("\\n", "\n").strip()
            print("Clean Output:\n", clean_output)
        else:
            print("Result:", result)

    except Exception as e:
        print(f"Error generating or executing code: {str(e)}")

# Prompt the user for the task
question = input('question: ')
print(generate_code_with_llama_execute_with_autogen(question, file_path, data))
