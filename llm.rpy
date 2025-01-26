init python:
    import subprocess

    model = ""

    conv_hist = ""

    initial_context = "You are a helpful assistant."

    def ollama_run(query: str) -> str:
        global conv_hist

        full_context = initial_context + "\n" + conv_hist

        full_context += f"{query}\n"

        command = ['ollama', 'run', model, full full_context]

        result = subprocess.run(command, capture_output=True, text=True)

        response = result.stdout.strip()

        conv_hist += f"{response}\n"

        return response

label start:
