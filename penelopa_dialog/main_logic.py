class PenelopaDialog:
    def __init__(self, prompt_message):
        self.prompt_message = prompt_message

    def run(self):
        print(self.prompt_message, end='')
        return input()