# Environment
- Use uv as the package manager.
- Execute code with `uv run <file>`.
- Add dependencies with `uv add <package>`.
- Run tests with `uv run pytest`.
- Prefer running single tests during development for performance: `uv run pytest tests/<test_file>.py::test_<test_name>`.

# Linting and Formatting
- Use Ruff for formatting and linting.
- Check code with `uv run ruff check`.
- Format code with `uv run ruff format`.
- Let Ruff fix whitespace and line endings (`uv run ruff check --fix`).

# Code Style
- Prefix private class members with underscore (_).
- Use numpy-style docstrings for functions and classes.
- Mimic the style (formatting, naming), structure, framework choices, typing, and architectural patterns of existing code in the project.

# Comments
- When you add comments, focus on *why* something is done, especially for complex logic, rather than *what* is done.
- Do not edit comments that are separate from the code you are changing.
- NEVER talk to the user or describe your changes through comments
