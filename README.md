# Cognitalk: Your Private AI Journal Assistant

## 🧠 Truly Personal AI, 100% Private.

**Submission for the OpenAI Open Model Hackathon - Best Local Agent Category.**

Cognitalk is an innovative command-line AI journal assistant that I built for ultimate privacy. In an age where using AI often means uploading your most sensitive data to third-party servers, Cognitalk stands apart. I believe you shouldn't have to trade your privacy for the power of AI, which is why your most personal thoughts and reflections **never leave your personal computer**.

## ✨ Features

Cognitalk empowers you to gain deep insights from your journal entries in a secure, conversational way:

*   **🔒 Securely Add Entries:** Write and save journal entries to a local text file that is **never uploaded or shared**. Your data stays with you.
*   **🗣️ Ask Questions:** Chat with your own personal history in a natural, conversational manner. Easily recall memories, find specific information, or revisit past thoughts.
*   **🔍 Analyze Themes:** Go beyond simple Q&A. The `analyze` feature leverages `gpt-oss` to act as an AI psychoanalyst, identifying recurring themes, emotional patterns, and hidden insights within your writing. Get unparalleled self-reflection and personal growth, all while maintaining complete privacy.

## 🚀 Architectural Deep Dive

Cognitalk is built on a secure, privacy-first client-server architecture to ensure your sensitive data remains local while still harnessing the power of a sophisticated AI model.

![Architectural Diagram of Cognitalk](https://github.com/Jerryblessed/cognitalk/blob/main/architectural_diagram.png?raw=true)

*   **The Brain (Server):** A Python **Flask** server runs in a private Google Colab environment. It utilizes **Ollama** to serve the powerful, open-source **`gpt-oss-20b`** model, handling all the complex AI reasoning and analysis.
*   **The Bridge (Tunnel):** I employed **ngrok** to create a secure, temporary tunnel to the Flask server. This allows the local client to communicate with the AI model without exposing the server directly.
*   **The Interface (Client):** A local Python script runs directly on the user's PC. It manages the journal file, handles user input, and presents a clear, engaging command-line interface enhanced with **Colorama**.

This design meticulously guarantees that the AI model only ever sees the text of a single prompt and never has direct access to the user's personal files.

### Challenges I Ran Into

Building Cognitalk presented unique challenges, particularly around stability and data integrity:

1.  **Unicode Errors:** Early iterations crashed when encountering special characters in journal entries. I solved this by implementing **rigorous UTF-8 encoding** across all file I/O operations.
2.  **Ollama Initialization:** Ensuring the AI model was ready before the server began listening for requests was critical. I re-architected the server script into a robust, all-in-one process that ensures Ollama is downloaded, running, and has the model pulled *before* the public-facing server starts.

### Accomplishments I'm Proud Of

I am incredibly proud of building a fully functional, end-to-end AI application that is both useful and safe. My key accomplishments are:
*   **The Privacy-First Architecture:** Successfully creating a system where the user's private data is physically separated from the AI model.
*   **Agentic Reasoning:** The `analyze` feature is a testament to `gpt-oss`'s capability for complex synthesis and reasoning, providing deep psychoanalytic insights rather than just basic Q&A.
*   **A Polished User Experience:** Despite being a command-line tool, Cognitalk is intuitive, provides clear feedback, and uses color effectively for a visually engaging experience.

### What I Learned

This project was an intensive exploration into the power of local, open-weight language models:

1.  **The Viability of Local AI:** I proved that `gpt-oss` combined with Ollama is an incredibly powerful stack for building real-world applications without the necessity of cloud APIs.
2.  **The Art of Prompt Engineering:** The stark difference in capabilities between a simple Q&A prompt and the complex "psychoanalyst" prompt for the `analyze` feature highlighted the profound impact of well-crafted prompts.
3.  **The Importance of Secure Design:** Building this client-server architecture reinforced the critical importance of designing systems that are both powerful and inherently respectful of user privacy.

## 🔮 What's Next for Cognitalk

This is just the beginning. My vision for Cognitalk is to evolve it into a full, private OS assistant:

*   **Short-Term:** Package the client into a simple, downloadable application for Windows and macOS.
*   **Long-Term:** Extend the core architecture to handle more than just a journal. I envision a voice-controlled agent that can analyze local documents, securely browse the web, and automate tasks with tools like `pyautogui` – all while maintaining the same 100% privacy guarantee. Cognitalk is the foundation for a future where your AI agent truly works for you, and only you.

---

## For Advanced Users: Running 100% Locally

This project's architecture is designed for accessibility. However, for users with a powerful local GPU and Ollama already installed, the client can be easily adapted to run in a 100% local mode.

**Prerequisites:**
1.  [Ollama](https://ollama.com/download) is installed and running on your local machine.
2.  You have pulled the model: `ollama pull gpt-oss:20b`.

**To run locally, you would modify `client.py` to call the local Ollama instance directly instead of the ngrok URL:**

```python
# --- Example of local-only modification ---
# import ollama # Instead of requests

# ... inside the send_prompt_to_server function ...
# response = ollama.chat(model='gpt-oss:20b', messages=[{'role': 'user', 'content': prompt}])
# print(Fore.CYAN + f"cognitalk: {response['message']['content']}\n")
