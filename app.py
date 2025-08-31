import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"  # You can use other BlenderBot variants too
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Store conversation history
chat_history = []

# Max length for tokenized prompt
MAX_INPUT_TOKENS = 128
MAX_HISTORY = 6  # Keep last 3 exchanges (user + bot)

def respond(user_input):
    global chat_history

    # Add user's message to history
    chat_history.append(f"User: {user_input}")

    # Keep only the last few messages to prevent context overflow
    if len(chat_history) > MAX_HISTORY:
        chat_history = chat_history[-MAX_HISTORY:]

    # Join history into single prompt
    prompt = "\n".join(chat_history)

    # Tokenize with truncation
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=MAX_INPUT_TOKENS)

    # Generate response
    reply_ids = model.generate(**inputs, max_new_tokens=80)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Add bot response to history
    chat_history.append(f"Missy: {reply}")
    return reply

with gr.Blocks() as app:
    gr.Markdown("## 💬 Chat with Missy - Your Smart, Sassy AI Assistant")
    chatbot_ui = gr.Chatbot()
    user_input = gr.Textbox(label="Type your message")
    send_btn = gr.Button("Send")

    def chat(user_msg, history):
        reply = respond(user_msg)
        history = history + [(user_msg, reply)]
        return history, ""

    send_btn.click(chat, inputs=[user_input, chatbot_ui], outputs=[chatbot_ui, user_input])

# Launch
app.launch()
