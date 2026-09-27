#!/bin/bash
echo "=== macOS Pop-up Translator Kurulumu ==="
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Step 1: Grant permissions
chmod +x "$SCRIPT_DIR/popup_translate.py"
chmod +x "$SCRIPT_DIR/run_translator.sh"

TARGET_DIR="$HOME/.popup_translator"
echo "1. Uygulama dosyaları $TARGET_DIR konumuna kopyalanıyor..."
mkdir -p "$TARGET_DIR"
cp "$SCRIPT_DIR/popup_translate.py" "$TARGET_DIR/"
cp "$SCRIPT_DIR/run_translator.sh" "$TARGET_DIR/"
chmod +x "$TARGET_DIR"/*.sh "$TARGET_DIR"/*.py

# Step 2: Install deep-translator in standalone venv
echo "2. Bağımlılıklar ($TARGET_DIR/venv) kuruluyor..."
if [ ! -d "$TARGET_DIR/venv" ]; then
    python3 -m venv "$TARGET_DIR/venv"
fi
"$TARGET_DIR/venv/bin/pip" install deep-translator --quiet

echo ""
echo "✅ Kurulum tamamlandı!"
echo "Kestirmeler (Shortcuts) betik yolu: $TARGET_DIR/run_translator.sh"
