#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
from crew import CompAnalyst

__import__('pysqlite3') 
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
#load_dotenv()
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
inputs={"company_name":"company"}
def run(inputs):
    """
    Run the crew.
    """
    
    
    try:
         return CompAnalyst().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        
    }
    try:
        CompAnalyst().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CompAnalyst().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        
    }
    try:
        CompAnalyst().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
