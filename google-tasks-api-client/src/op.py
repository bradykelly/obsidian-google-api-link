import subprocess
import json


def run_op_command(command):
    """ Run a 1Password CLI command and return the output """
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"1Password CLI error: {result.stderr}")
    return result.stdout


def get_secure_note_field(vault_name, item_name, field_name):
    """ Get the content of a field from a 1Password Secure Note """
    command = ["op", "read", f"op://{vault_name}/{item_name}/{field_name}"]
    field_content = run_op_command(command)
    return field_content

