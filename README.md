# Github Copilot Custom Instructions
Custom Github Copilot instructions for **VS Code** (`settings.json`) and **Pycharm**.

These are based on potentially useful prompts I encountered on the internet. 

The VS Code JSON settings are partially synced from the Pycharm Markdown files  file via a pre-commit hook. Install the pre commit hook with `uv run pre-commit install`.

## 📂 Location of the Pycharm files:
- `%LOCALAPPDATA%\github-copilot\intellij\global-git-commit-instructions.md`
- `%LOCALAPPDATA%\github-copilot\intellij\global-copilot-instructions.md`

## ⚙️ Settings in VS Code:
- [github.copilot.chat.codeGeneration.instructions](vscode://settings/github.copilot.chat.codeGeneration.instructions)
- [github.copilot.chat.commitMessageGeneration.instructions](vscode://settings/github.copilot.chat.commitMessageGeneration.instructions)
- [github.copilot.chat.testGeneration.instructions](vscode://settings/github.copilot.chat.testGeneration.instructions)

Or via the `settings.json` file at `%APPDATA%\Code\User\settings.json`


## See also
- [Customize AI responses in VS Code](https://code.visualstudio.com/docs/copilot/copilot-customization#_specify-custom-instructions-in-settings)
- [Writing effective repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot#writing-effective-repository-custom-instructions)
- [Gemini CLI system prompt](https://gist.github.com/simonw/9e5f13665b3112cea00035df7da696c6)
- [Example CLAUDE.md file](https://github.com/mitsuhiko/sloppy-xml-py/blob/main/CLAUDE.md)
