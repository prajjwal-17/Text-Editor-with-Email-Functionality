# Python Text Editor with Email Functionality

This is a simple Python-based text editor that allows users to create, edit, save, and open text files. Additionally, it includes an SMTP feature to send emails directly from the editor. The application supports both GUI (using Tkinter) and text-based modes, making it versatile for different user preferences.

---

## Features

- **Text Editing**: Create, edit, and save text files in a user-friendly environment.
- **File Management**: Open existing text files and save new edits seamlessly.
- **Email Sending**: Send text files as email attachments or directly email the file content using SMTP.
- **Dual Mode**: Run in GUI mode (Tkinter) or CLI (command line interface) mode.
- **Simple and Lightweight**: Built with simplicity in mind, ideal for lightweight tasks.

---

## Requirements

- Python 3.x
- Tkinter (usually included with Python on most platforms)
- SMTP email server credentials (e.g., Gmail, Outlook, etc.)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/python-text-editor.git
    cd python-text-editor
    ```

2. **Install dependencies**:
    Tkinter is usually included in Python, but if you need to install it:
    ```bash
    # For Debian/Ubuntu-based systems
    sudo apt-get install python3-tk
    ```

3. **Run the Text Editor**:
    - **GUI Mode**:
      ```bash
      python3 gui_editor.py
      ```

    - **Text Mode**:
      ```bash
      python3 text_editor.py
      ```

---

## Usage

### GUI Mode

In the GUI, you can:
- **Create**: Type text directly into the editor.
- **Save**: Click `Save` to save the current file.
- **Open**: Click `Open` to load an existing text file.
- **Send Email**: Use the `Send Email` button to send the file content as an email.

### Text Mode (CLI)

In text mode:
1. Start the editor.
2. Use commands to create, edit, save, and open files.
3. To send an email, run the following:
   ```bash
   python3 text_editor.py --email

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to open issues or submit pull requests for enhancements or bug fixes.


