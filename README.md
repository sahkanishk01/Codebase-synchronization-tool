# Multi-Language Codebase Synchronization Tool (MLCST)

The Multi-Language Codebase Synchronization Tool (MLCST) is designed to facilitate the synchronization of codebases written in different programming languages. This tool streamlines the development process for teams working on multi-language projects, ensuring that changes made in one language are automatically reflected in others.

## Features

- **Automatic Change Detection**: Monitors changes in the primary codebase using Git.
- **Real-Time Code Translation**: Translates code changes to other language versions using advanced algorithms.
- **Conflict Resolution**: Provides mechanisms for resolving conflicts arising from simultaneous edits.
- **Web-Based Dashboard**: Offers a user-friendly interface for monitoring synchronization status and notifications.
- **Customizable Language Profiles**: Allows users to define language-specific rules for translation.

## Technologies Used

- Python
- Flask (for the web interface)
- Git (for version control)
- Abstract Syntax Trees (AST) for code translation
- JavaScript (for frontend interactions)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/mlcst.git
   cd mlcst

Install Dependencies: 
Make sure you have Python and pip installed. Then, install the required packages:

Run : pip install -r requirements.txt
  
Set up the Git hooks to enable automatic change detection:

Run : chmod +x .git/hooks/post-commit

Usage
Run the Flask Application: Start the web application:

Run : python app.py
Access the Dashboard: Open your web browser and navigate to http://127.0.0.1:5000/ to access the synchronization dashboard.

Make Changes: Edit the main.py file to make changes. The tool will automatically detect changes and synchronize them across the specified language versions.

