import json
import sys
from pathlib import Path


def pycharm_to_vscode_config(
    pycharm_filename: str,
    vscode_key: str,
) -> bool:
    """
    Convert PyCharm configuration files to VSCode settings.

    Args:
        pycharm_filename (str): The name of the PyCharm configuration file.
        vscode_key (str): The key in VSCode settings where the content should be placed.

    Returns:
        bool: True if the file was updated, False otherwise.
    """
    input_path = Path(__file__).parent / "pycharm" / pycharm_filename
    output_path = Path(__file__).parent / "vscode" / (vscode_key + ".json")

    #  Read instructuions from the PyCharm file
    instructions: list[str] = []
    for line in input_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            continue
        if line.strip() == "":
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        instructions.append(line)

    # Check if the output file already exists and if the content is the same
    if output_path.exists():
        existing_data = json.loads(output_path.read_text(encoding="utf-8"))
        existing_instructions = [
            item["text"] for item in existing_data.get(vscode_key, [])
        ]
        if existing_instructions == instructions:
            return False

    # Write the instructions to the VSCode settings file
    with open(output_path, "w", encoding="utf-8") as f:
        print(f"Updating {output_path}.")
        json.dump(
            {vscode_key: [{"text": instr} for instr in instructions]}, f, indent=4
        )
    return True


if __name__ == "__main__":
    ret1 = pycharm_to_vscode_config(
        pycharm_filename="global-copilot-instructions.md",
        vscode_key="github.copilot.chat.codeGeneration.instructions",
    )
    ret2 = pycharm_to_vscode_config(
        pycharm_filename="global-git-commit-instructions.md",
        vscode_key="github.copilot.chat.commitMessageGeneration.instructions",
    )
    if ret1 or ret2:
        print("PyCharm configuration files updated.")
        sys.exit(1)  # pre-commit hook will fail
    sys.exit(0)  # pre-commit hook will pass
