[![PyPI version](https://badge.fury.io/py/penelopa-dialog.svg)](https://badge.fury.io/py/penelopa-dialog)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/penelopadialog)](https://pepy.tech/project/penelopadialog)

# Penelopa Dialog

`Penelopa Dialog` is a Python module for creating interactive console applications. It simplifies the process of dialogues in the console, waiting for user inputs, and handling responses, making it easier to create interactive command-line tools.

## Installation

To install `Penelopa Dialog`, you can use pip:

```bash
pip install penelopa-dialog
```

## Usage

### As a Python Module

You can use `Penelopa Dialog` as a module in your Python scripts.

Example:

```python
from penelopa_dialog import PenelopaDialog

# Initialize the dialog with a prompt message
dialog = PenelopaDialog("Hello, please tell me your task.")

# Run the dialog and capture the user's input
user_response = dialog.run()

print("You responded with:", user_response)
```

This example demonstrates initializing the `Penelopa Dialog` with a specific message, running the dialogue to wait for the user's input, and then printing out the response.

### Customizing Your Dialogue

You can customize your dialogue by adjusting the prompt message or by extending the `PenelopaDialog` class to include more complex logic or additional interactive features.

## Output Example

When you run the `Penelopa Dialog`, it displays the prompt message and waits for the user's input. Here is an example interaction:

```
Hello, please tell me your task:
> Refactor the database schema.
You responded with: Refactor the database schema.
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/penelopa-dialog/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)
