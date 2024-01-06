# main_logic.py in the penelopa_dialog package

class PenelopaDialog:
    def __init__(self, prompt_message):
        self.prompt_message = prompt_message

    def run(self):
        # Print the prompt message with any formatting included
        print(self.prompt_message, end='')  # 'end' parameter controls what's printed after the message. Default is '\n'.

        # Wait for and return the user's input without any additional text
        return input()

# Additional methods and logic based on the requirements of your package
