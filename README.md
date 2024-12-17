Deploy an AI agent with via autogen and llama_index for making data analysis with your files.

In order to understand how this AI Agent locally works; you must first be familiar with how local llama systems works with ollama as I explained through my previous repository: https://github.com/ErdenizUnvan/ollama_local_llama_api

This project is one of the examples that I have made during my studies at Purdue University Applied Generative AI Specialization program.

Make a directory called coding at your path. Paste the heart.csv file to that folder. 

The python code of analysis_excel_csv_with_llama.py will not be at the folder named coding. Make sure that the python code is at parent directory. 

At python code replace the value of 'C:/Users/Dell/llama3_2/coding/heart.csv' with your files os full file path at your directory.

If you will run xlsx files, then make sure to change df = pd.read_csv(file_path) with df = pd.read_excel(file_path) at the python code.

 
