# ==============================================================================
# CLIENT SCRIPT (V4) - FINAL SUBMISSION VERSION
# All features and professional color design included.
# ==============================================================================
import requests
import json
from datetime import datetime
# Import the colorama library for a polished look
from colorama import init, Fore, Style

# Initialize colorama to automatically reset colors after each print
init(autoreset=True)

# Your ngrok URL is perfect, keep it.
NGROK_URL = "https://b45d840dc295.ngrok-free.app/process"

JOURNAL_FILE = "jo.txt"

def add_entry(text):
    """Appends a new entry to the local journal file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
            f.write(f"--- Entry Date: {timestamp} ---\n{text}\n\n")
        # Use green for success messages
        print(Fore.GREEN + "✅ Entry saved to your local journal.")
    except Exception as e:
        # Use red for errors
        print(Fore.RED + f"Error saving entry: {e}")

def load_journal():
    """Loads the entire local journal content into a string."""
    try:
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Your journal is currently empty."

def send_prompt_to_server(prompt):
    """Sends a prompt to the server and prints the response with colors."""
    # Use yellow for "thinking" status
    print(Fore.YELLOW + "\n🧠 Thinking...")
    try:
        response = requests.post(NGROK_URL, json={"prompt": prompt})
        if response.status_code == 200:
            result = response.json()
            # Use cyan for the AI's response to make it stand out
            print(Fore.CYAN + f"cognitalk: {result.get('response')}\n")
        else:
            print(Fore.RED + f"Error: Server returned status {response.status_code}. Details: {response.text}\n")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Connection Error: Could not connect to the server at {NGROK_URL}.")
        print(Fore.RED + "Please make sure the Colab server is running and the ngrok URL is correct.\n")


def main():
    """Main function to run the client application."""
    # Use bright magenta for the title to make it pop
    print(Style.BRIGHT + Fore.MAGENTA + "=================================================")
    print(Style.BRIGHT + Fore.MAGENTA + " cognitalk: Your Private AI Journal Assistant ")
    print(Style.BRIGHT + Fore.MAGENTA + "=================================================")
    
    print("Type 'add' to write a new journal entry.")
    print("Type 'analyze' to get an analysis of your journal.")
    print("Type 'exit' to quit.")
    print("Otherwise, just ask a question about your journal.\n")

    while True:
        # Use bright style for user input prompt
        user_input = input(Style.BRIGHT + "You: ")

        if user_input.lower() == 'exit':
            print(Fore.YELLOW + "Goodbye!")
            break

        if user_input.lower() == 'add':
            # Use cyan for the entry prompt
            entry_text = input(Fore.CYAN + "Write your journal entry: ")
            add_entry(entry_text)
            continue

        if user_input.lower() == 'analyze':
            journal_content = load_journal()
            analysis_prompt = f"""
            You are a thoughtful psychoanalyst. Read the following journal entries
            and provide a brief analysis. Identify 2-3 recurring themes (like 'anxiety about work',
            'excitement for a new project', 'reflections on family'), and for each theme,
            provide one piece of gentle, constructive insight.

            --- JOURNAL ENTRIES ---
            {journal_content}
            --- END OF JOURNAL ---
            """
            send_prompt_to_server(analysis_prompt)
            continue

        journal_content = load_journal()
        qa_prompt = f"""
        You are a helpful and insightful journal assistant. Based ONLY on the
        following journal entries, answer the user's question.

        --- JOURNAL ENTRIES ---
        {journal_content}
        --- END OF JOURNAL ---

        User's question: "{user_input}"
        """
        send_prompt_to_server(qa_prompt)

if __name__ == "__main__":
    main()