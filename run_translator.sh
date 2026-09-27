#!/bin/bash
# Wrapper script to execute popup_translate.py with appropriate environment
PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check virtualenv python first (local venv, parent venv, Kodus venv, fallback system)
if [ -f "$SCRIPT_DIR/venv/bin/python" ]; then
    PYTHON_BIN="$SCRIPT_DIR/venv/bin/python"
elif [ -f "$SCRIPT_DIR/../.venv/bin/python" ]; then
    PYTHON_BIN="$SCRIPT_DIR/../.venv/bin/python"
elif [ -f "/Users/alikeremguvenc/Documents/Kodus/.venv/bin/python" ]; then
    PYTHON_BIN="/Users/alikeremguvenc/Documents/Kodus/.venv/bin/python"
elif command -v python3 &>/dev/null; then
    PYTHON_BIN="$(command -v python3)"
else
    PYTHON_BIN="/opt/homebrew/bin/python3"
fi

"$PYTHON_BIN" "$SCRIPT_DIR/popup_translate.py"
