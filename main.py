#!/usr/bin/env python
from langchain.chains import LLMChain
from langchain_aws.llms.bedrock import BedrockLLM
from langchain_community.chat_models import BedrockChat

from langchain_core.prompts import PromptTemplate

# from langchain_aws.llms.bedrock import BedrockLLM
# pydantic.v1.error_wrappers.ValidationError: 1 validation error for BedrockLLM
# Claude v3 models are not supported by this LLM


def main():

    ## Titan example
    _titan_llm = BedrockLLM(
        model_id="amazon.titan-text-lite-v1",
    )
    #  
    ## Claude v3 models are not working with BedrockLLM as of 8/9/2024
    ## When I try with:  from langchain_aws.llms.bedrock import BedrockLLM
    ## I recieved:      pydantic.v1.error_wrappers.ValidationError: 1 validation error for BedrockLLM
    ##                  Claude v3 models are not supported by this LLM 
   
    claude_llm = BedrockChat(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    )

    prompt_template = """
    You are an expert software engineer who is well versed in {language}.

    I will ask you to design a software system and you will answer in the format of:
    ## Specification of the system
    ## Summary of what and how this system will function
    ## Source code of the system
    
    Design a software system that {description}
    """

    prompt = PromptTemplate(
        input_variables=["country"], template=prompt_template
    )

    llm = LLMChain(llm=claude_llm, prompt=prompt)
    response = llm.invoke({"language": "Quarkus",
                           "description": "Create a REST API that returns the latest stock prick for a given ticker symbol"})
    print(response['text'])

if __name__ == "__main__":
    main()

