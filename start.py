import subprocess
import threading
import os



# Using 127.0.0.1 because localhost does not work properly in PRP
model = os.getenv('model_name')
def run_controller():
    subprocess.run(["python3", "-m", "fastchat.serve.controller", "--host", "127.0.0.1"])

def run_model_worker():
    model = os.environ.get('model_name')
    subprocess.run(["python3", "-m", "fastchat.serve.model_worker", "--host", "127.0.0.1",  "--model-path", model])

def run_api_server():
    subprocess.run(["python3", "-m", "fastchat.serve.openai_api_server", "--host", "127.0.0.1"])
def run_ui_server():
    subprocess.run(["python3", "-m", "fastchat.serve.gradio_web_server", "--host", "127.0.0.1"])





# Start controller thread

controller_thread = threading.Thread(target=run_controller)
controller_thread.start()
model_worker_thread = threading.Thread(target=run_model_worker)
model_worker_thread.start()
api_server_thread = threading.Thread(target=run_api_server)
api_server_thread.start()
ui_server_thread = threading.Thread(target=run_ui_server)
ui_server_thread.start()