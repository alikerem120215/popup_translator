#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimalist macOS Pop-up Translator
Reads Turkish text from system clipboard (pbpaste), translates it to English,
and displays it in a clean, centered, frameless topmost window.
"""

import sys
import subprocess
import tkinter as tk

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("HATA: 'deep-translator' kütüphanesi yüklü değil.")
    print("Lütfen şu komutu çalıştırın: pip install deep-translator")
    sys.exit(1)


def get_clipboard_text() -> str:
    """Reads current text from macOS clipboard via pbpaste."""
    try:₺
        result = subprocess.run(['pbpaste'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Pano okuma hatası: {e}")
        return ""


def translate_text(text: str) -> tuple[str, str]:
    """
    Translates text from Turkish to English (or auto-detected).
    Returns (translated_text, target_lang_code)
    """
    if not text:
        return "Panoda okunacak metin bulunamadı.", "HATA"

    try:
        translator = GoogleTranslator(source='auto', target='en')
        translation = translator.translate(text)

        # Smart fallback: if copied text was already English, translate to Turkish
        if translation and translation.strip().lower() == text.strip().lower():
            translator_tr = GoogleTranslator(source='auto', target='tr')
            translation = translator_tr.translate(text)
            return translation, "TR"

        return translation, "EN"
    except Exception as e:
        return f"Çeviri hatası: {e}", "HATA"


class TranslatorPopup:
    def __init__(self, original_text: str, translated_text: str, target_lang: str):
        self.root = tk.Tk()
        self.original_text = original_text
        self.translated_text = translated_text
        self.target_lang = target_lang

        # Copy translated text back to clipboard for instant use
        self.copy_to_clipboard(translated_text)

        self.setup_window()
        self.create_widgets()
        self.adjust_dynamic_geometry()
        self.bind_events()

    def copy_to_clipboard(self, text: str):
        """Copies text to macOS clipboard using pbcopy."""
        try:
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, text=True)
            process.communicate(input=text)
        except Exception as e:
            print(f"Pano yazma hatası: {e}")

    def setup_window(self):
        # Frameless popup style
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        # Ultra-Minimalist Apple Dark Palette
        self.bg_color = "#1c1c1e"        # macOS System Dark Gray
        self.border_color = "#3a3a3c"    # Subtle Dark Border
        self.text_color = "#ffffff"      # High Contrast White
        self.orig_color = "#8e8e93"      # Secondary Muted Text
        self.badge_color = "#0a84ff"     # Apple System Blue
        self.footer_color = "#636366"    # Subtle Footer Text

        self.root.configure(bg=self.border_color)

        # Inner frame for 1px subtle border
        self.main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=16)
        self.main_frame.pack(fill="both", expand=True, padx=1, pady=1)

    def create_widgets(self):
        # Top bar: Minimal language indicator
        top_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        top_frame.pack(fill="x", anchor="w")

        lang_pair = "TR → EN" if self.target_lang == "EN" else "EN → TR"
        lang_label = tk.Label(
            top_frame,
            text=lang_pair,
            font=("SF Pro Text", 10, "bold"),
            fg=self.badge_color,
            bg=self.bg_color
        )
        lang_label.pack(side="left")

        copied_hint = tk.Label(
            top_frame,
            text="Panoya kopyalandı",
            font=("SF Pro Text", 9),
            fg=self.orig_color,
            bg=self.bg_color
        )
        copied_hint.pack(side="right")

        # Main Translated Text (Large & Crisp)
        trans_text = self.translated_text
        if len(trans_text) > 400:
            trans_text = trans_text[:397] + "..."

        trans_label = tk.Label(
            self.main_frame,
            text=trans_text,
            font=("SF Pro Display", 13, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
            anchor="w",
            justify="left",
            wraplength=395
        )
        trans_label.pack(fill="x", pady=(10, 6))

        # Original text preview (Small & subtle)
        orig_preview = self.original_text.replace('\n', ' ')
        if len(orig_preview) > 150:
            orig_preview = orig_preview[:147] + "..."

        orig_label = tk.Label(
            self.main_frame,
            text=orig_preview,
            font=("SF Pro Text", 10, "italic"),
            fg=self.orig_color,
            bg=self.bg_color,
            anchor="w",
            justify="left",
            wraplength=395
        )
        orig_label.pack(fill="x", pady=(0, 10))

        # Minimal Footer
        footer_label = tk.Label(
            self.main_frame,
            text="Kapatmak için ESC tuşuna basın veya tıklayın",
            font=("SF Pro Text", 8),
            fg=self.footer_color,
            bg=self.bg_color
        )
        footer_label.pack(side="bottom", anchor="w")

    def adjust_dynamic_geometry(self):
        """Calculates exact required height dynamically and centers on screen."""
        self.root.update_idletasks()

        # Fixed width, dynamic required height
        width = 440
        req_height = self.main_frame.winfo_reqheight() + 4

        # Min & max bounds for clean aesthetics
        height = max(130, min(req_height, 550))

        # Screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate exact centered position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2 - 30

        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def bind_events(self):
        # Close triggers
        self.root.bind("<Escape>", lambda e: self.close())
        self.root.bind("<Button-1>", lambda e: self.close())
        self.main_frame.bind("<Button-1>", lambda e: self.close())
        self.root.bind("<FocusOut>", lambda e: self.close())

        # Recursively bind clicks to all inner labels for seamless click-to-close
        for widget in self.main_frame.winfo_children():
            widget.bind("<Button-1>", lambda e: self.close())

    def close(self):
        self.root.destroy()

    def run(self):
        self.root.lift()
        self.root.focus_force()
        self.root.mainloop()


def main():
    clip_text = get_clipboard_text()
    if not clip_text:
        popup = TranslatorPopup("Pano Boş", "Lütfen çevirmek istediğiniz metni kopyalayın.", "HATA")
        popup.run()
        return

    translated, lang = translate_text(clip_text)
    popup = TranslatorPopup(clip_text, translated, lang)
    popup.run()


if __name__ == "__main__":
    main()
