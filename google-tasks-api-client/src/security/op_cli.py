import subprocess
from typing import Any


def run_op_command(command: Any) -> str:
    """ Run a 1Password CLI command and return the output """
    result: subprocess.CompletedProcess[str] = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"1Password CLI error: {result.stderr}")
    return result.stdout


def get_secure_note_field(vault_name, item_name, field_name) -> str:
    """ Get the content of a field from a 1Password Secure Note """
    command: Any = ["op", "read", f"op://{vault_name}/{item_name}/{field_name}"]
    field_content: str = run_op_command(command)
    return field_content

