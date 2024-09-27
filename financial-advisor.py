import boto3
import botocore.config

from langchain_aws import ChatBedrock
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase

def fintechbot(question:str):
    

   database_file_path = r"/Volumes/QDrive/Workspace/portfolio-projects/ai-financial-advisor/ai-financial-advisor.db"
   db = SQLDatabase.from_uri(f'sqlite:///{database_file_path}')

   bedrock_config = botocore.config.Config(read_timeout=900, connect_timeout=900, region_name="us-east-1")
   bedrock_client = boto3.client("bedrock-runtime", config=bedrock_config)

   llm = ChatBedrock(
    client=bedrock_client,
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs = {
        "temperature": 0.1,
        "top_p": 0.7,
        "top_k": 250,
    }
    )
   
   agent_executor = create_sql_agent(llm, db=db)
   # agent_executor = create_sql_agent(llm, db=db, verbose=True)

   response = agent_executor.invoke(
    {
        "input": question
    }
   )

   return response['output']

if __name__=="__main__":
    QUESTION = input("Ask a question: ")
    print(fintechbot(QUESTION))

# I have a high-risk tolerance. What investment options would you recommend?