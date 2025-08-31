# missy-chatbot
Missy is a smart, witty, and sarcastically helpful conversational AI assistant built using Hugging Face Transformers and Gradio. This project demonstrates how to build and deploy a character-driven chatbot locally, with no need for cloud-based inference. Missy is designed to maintain a casual, assistant-like tone while responding to users in a fun and engaging way.

The purpose of this project is to explore how open-source models can be customized to behave like unique personalities using prompt engineering. It’s also a technical demo of how conversational AI interfaces can be run completely on a local machine. This makes it suitable for developers learning about transformer-based chatbots, user interaction design, or local AI deployments.

Missy uses a pretrained model like DialoGPT-medium or BlenderBot-3B, and communicates with users through a Gradio-based web interface. While she does maintain short-term conversational memory, the design is intentionally lightweight and local, which means she doesn’t have persistent memory or long-form understanding. You can launch the chatbot by running app.py, which opens a Gradio interface in your browser at http://localhost:7860.

This project runs on CPU by default, though GPU acceleration is possible if available. Due to model size and architecture, response generation may take 60 to 90 seconds on CPU with larger models like BlenderBot. DialoGPT performs faster but produces less coherent multi-turn dialogue. The chatbot is modular, so models can easily be swapped with just a single line of code.

There are limitations. Missy is guided purely by prompt structure—not by fine-tuned training—so while her tone remains consistent, she can sometimes hallucinate answers, forget context, or repeat herself. Her short-term memory is limited to a few conversation turns. Larger models also introduce latency and can stall on weaker hardware. Despite these limitations, Missy is a strong foundation for experimenting with AI personality and local chatbot deployment.

To set up, install the required Python packages and run the script. Future improvements may include personality presets, persistent memory, newer instruct-tuned models like Mistral-7B, or hosting on platforms like Hugging Face Spaces.

This project is a fun way to demonstrate AI personality engineering and user interaction, and serves as a great addition to any data science or machine learning portfolio.
