# Cognitalk: Your Private AI Journal Assistant

## 🧠 Truly Personal AI, 100% Private.

**Submission for the OpenAI Open Model Hackathon - Best Local Agent Category.**

Cognitalk is an innovative command-line AI journal assistant that I built for ultimate privacy. In an age where using AI often means uploading your most sensitive data to third-party servers, Cognitalk stands apart. I believe you shouldn't have to trade your privacy for the power of AI, which is why your most personal thoughts and reflections **never leave your personal computer**.

---

## ▶️ How to Run This Project (Testing Instructions)

To test Cognitalk, you will need to run two scripts: the server in Google Colab and the client on your local machine.

### Step 1: Run the Server (on Google Colab)
1.  Open the `oss_server.py` script in a Google Colab notebook.
2.  Run the entire script in a single cell (`!oss_server.py`).
3.  The script will install all dependencies, start the AI model, and at the end, it will print a public `ngrok` URL.
4.  **Copy this public URL.**

### Step 2: Run the Client (on Your Local PC)
1.  Ensure you have Python installed on your computer.
2.  Install the required libraries by running: `pip install requests colorama`.
3.  Open the `oss.py` file in a text editor.
4.  Find the line `NGROK_URL = "..."` and paste the public URL you copied from Colab.
5.  Save the file.

### Step 3: Start Chatting!
1.  Open a terminal or command prompt on your PC.
2.  Navigate to the project directory.
3.  Run the command: `python oss.py`.
4.  The application will start, and you can begin adding entries or asking questions!

---

## ✨ Features

*   **🔒 Securely Add Entries:** Write and save journal entries to a local text file that is **never uploaded or shared**.
*   **🗣️ Ask Questions:** Chat with your own personal history in a natural, conversational manner.
*   **🔍 Analyze Themes:** Use the `analyze` command to have the AI act as a psychoanalyst, identifying recurring themes and emotional patterns in your writing.


Cognitalk is built on a secure, privacy-first client-server architecture.
Of course. Here is the exact Markdown code for the demo video section.

## 🎥 Demo Video

Watch the 3-minute video below to see Cognitalk in action and learn about its privacy-first architecture.

[![Cognitalk Demo Video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=kRIXcjK2HGE)

## 🚀 Architectural Deep Dive

![Architectural Diagram of Cognitalk](https://github.com/Jerryblessed/cognitalk/blob/main/architectural_diagram.png?raw=true)

*   **The Brain (Server):** A Python **Flask** server runs in a private Google Colab environment, using **Ollama** to serve the **`gpt-oss-20b`** model.
*   **The Bridge (Tunnel):** I employed **ngrok** to create a secure, temporary tunnel to the Flask server.
*   **The Interface (Client):** A local Python script runs on the user's PC, managing the journal file and presenting a polished UI enhanced with **Colorama**.

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

**To run locally, you would modify `oss.py` to call the local Ollama instance directly instead of the ngrok URL:**

```python
# --- Example of local-only modification ---
# import ollama # Instead of requests

# ... inside the send_prompt_to_server function ...
# response = ollama.chat(model='gpt-oss:20b', messages=[{'role': 'user', 'content': prompt}])
# print(Fore.CYAN + f"cognitalk: {response['message']['content']}\n")
