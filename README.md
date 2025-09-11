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
3.  Run the command: `python client.py`.
4.  The application will start, and you can begin adding entries or asking questions!

---

## ✨ Features

*   **🔒 Securely Add Entries:** Write and save journal entries to a local text file that is **never uploaded or shared**.
*   **🗣️ Ask Questions:** Chat with your own personal history in a natural, conversational manner.
*   **🔍 Analyze Themes:** Use the `analyze` command to have the AI act as a psychoanalyst, identifying recurring themes and emotional patterns in your writing.

## 🚀 Architectural Deep Dive

Cognitalk is built on a secure, privacy-first client-server architecture.

![Architectural Diagram of Cognitalk](https://github.com/Jerryblessed/cognitalk/blob/main/architectural_diagram.png?raw=true)

*   **The Brain (Server):** A Python **Flask** server runs in a private Google Colab environment, using **Ollama** to serve the **`gpt-oss-20b`** model.
*   **The Bridge (Tunnel):** I employed **ngrok** to create a secure, temporary tunnel to the Flask server.
*   **The Interface (Client):** A local Python script runs on the user's PC, managing the journal file and presenting a polished UI enhanced with **Colorama**.

This design guarantees that the AI model only ever sees the text of a single prompt and never has direct access to the user's personal files.

*(...The rest of your README - "Challenges," "Accomplishments," "What I Learned," and "What's Next" - is perfect as it is and should follow here.)*```
