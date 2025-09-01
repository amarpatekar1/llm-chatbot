# Build AI Powered chat bot
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Backend: Python
def echo(message, history):
    response = client.responses.create(
    model="gpt-5",
    input=message
)

    return response.output_text




# Frontend: Gradio
test = gr.ChatInterface(fn=echo, type="messages", examples=[["Hello, how are you?"], ["What is the weather in Tokyo?"], ["What is the capital of France?"]])
test.launch()