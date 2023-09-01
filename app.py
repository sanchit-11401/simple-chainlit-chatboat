import chainlit as cl
from textblob import TextBlob
import tracemalloc
from gpt4all import GPT4All

gpt = GPT4All(model_name = "llama-2-7b-chat.ggmlv3.q4_0.bin", model_path = "E:/GPT4ALL/")

tracemalloc.start()


@cl.on_message
async def main(message: str):
    result = message.title()
    
    if "sentiment" in message:
        file = None
        while file == None:
            file = await cl.AskFileMessage(content= "Please upload a text file to analyze ", accept = {'text/plain'}).send()
        

        file = file[0]
        for item in file.content.decode("utf-8"):
            text += str(item)
        blob = TextBlob(text)

        await cl.Message(content=f"Sure, here is a message: {text}.\n your result is {blob.sentiment}").send()

    else:
        result = gpt.generate(message, temp =0)
        response = result["choice"][0]["message"]["content"]

        await cl.Message(content=f"Sure, : {response}").send()

@cl.on_chat_start
async def start():
    content = "Hi, I am Sanchit AI"
    await cl.Message(content = content).send()