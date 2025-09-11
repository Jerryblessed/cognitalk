# ==============================================================================
# app.py - THE COMPLETE, ALL-IN-ONE SERVER SCRIPT
# This single file installs and runs the entire server-side application.
# It is designed to be run in a Linux environment like Google Colab.
# ==============================================================================

import subprocess
import os
import time
import sys

def run_command(command, shell=False, description=None):
    """Helper function to run a command and exit if it fails."""
    if description:
        print(description)
    try:
        # For the curl command with a pipe, we need shell=True
        if shell:
            subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.stderr.decode()}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Command not found: {command[0]}. Is it installed and in your PATH?")
        sys.exit(1)

def setup_and_run_server():
    """Main function to perform all setup steps and start the server."""

    # Step 1: Install Ollama
    run_command("curl -fsSL https://ollama.com/install.sh | sh", shell=True, description="--- Step 1/5: Installing Ollama... ---")
    print("✅ Ollama has been installed.")

    # Step 2: Start the Ollama server as a background process
    print("\n--- Step 2/5: Starting Ollama server in the background... ---")
    ollama_process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(10)  # Give the server a generous amount of time to start
    print("✅ Ollama server is running in the background.")

    # Step 3: Pull the gpt-oss model
    run_command(["ollama", "pull", "gpt-oss:20b"], description="\n--- Step 3/5: Pulling gpt-oss:20b model (this may take a while)... ---")
    print("✅ Model has been downloaded.")

    # Step 4: Install Python libraries
    run_command([sys.executable, "-m", "pip", "install", "Flask", "pyngrok", "ollama", "-q"], description="\n--- Step 4/5: Installing required Python libraries... ---")
    print("✅ Python libraries are installed.")

    # Step 5: Define and Run the Flask Server and ngrok Tunnel
    # We must import these libraries *after* they are installed.
    from flask import Flask, request, jsonify
    from pyngrok import ngrok
    import ollama

    print("\n--- Step 5/5: Configuring server and starting public tunnel... ---")

    # Your ngrok authtoken
    NGROK_AUTHTOKEN = "2ux38Y129Uxr0xjY3epOzwlsSjX_5b3ozQEaYKQTev6CmfCes"
    ngrok.set_auth_token(NGROK_AUTHTOKEN)

    app = Flask(__name__)

    @app.route('/process', methods=['POST'])
    def process_prompt():
        """Endpoint to process prompts with the locally running Ollama model."""
        data = request.json
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({"error": "No prompt was provided"}), 400
        try:
            response = ollama.chat(
                model='gpt-oss:20b',
                messages=[{'role': 'user', 'content': prompt}]
            )
            return jsonify({"response": response['message']['content']})
        except Exception as e:
            # Provide a more detailed error if Ollama is not reachable from the script
            error_message = str(e)
            if "Connection refused" in error_message:
                error_message = "Failed to connect to Ollama. The Ollama process may have stopped."
            return jsonify({"error": error_message}), 500

    # Start the public tunnel and then the server
    ngrok.kill()
    public_url = ngrok.connect(5000)
    print("\n" + "="*60)
    print("🚀 YOUR SERVER IS LIVE AND READY! 🚀")
    print(f"🔗 Public URL: {public_url}")
    print("COPY THIS NEW URL AND PASTE IT INTO YOUR client.py SCRIPT.")
    print("="*60 + "\n")

    # This is a blocking call that starts the web server.
    app.run(port=5000)

if __name__ == '__main__':
    setup_and_run_server()