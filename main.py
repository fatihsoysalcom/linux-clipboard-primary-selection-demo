import tkinter as tk

def copy_to_clipboard():
    """Copies the currently selected text in text_widget1 to the CLIPBOARD selection."""
    try:
        selected_text = text_widget1.get("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected_text)
        status_label.config(text=f"Copied '{selected_text}' to CLIPBOARD.")
    except tk.TclError:
        status_label.config(text="No text selected to copy to CLIPBOARD.")

def paste_from_clipboard():
    """Pastes content from the CLIPBOARD selection into text_widget2."""
    try:
        clipboard_content = root.clipboard_get()
        text_widget2.delete("1.0", tk.END)
        text_widget2.insert(tk.END, clipboard_content)
        status_label.config(text=f"Pasted '{clipboard_content}' from CLIPBOARD.")
    except tk.TclError:
        status_label.config(text="CLIPBOARD is empty or not accessible.")

def paste_from_primary():
    """Pastes content from the PRIMARY selection into text_widget2.
    In Linux (X11), highlighting text automatically puts it into PRIMARY.
    This simulates a middle-click paste action."""
    try:
        # 'selection_get()' with selection="PRIMARY" retrieves the PRIMARY selection.
        # This is the text highlighted by the mouse, distinct from CLIPBOARD.
        primary_content = root.selection_get(selection="PRIMARY")
        text_widget2.delete("1.0", tk.END)
        text_widget2.insert(tk.END, primary_content)
        status_label.config(text=f"Pasted '{primary_content}' from PRIMARY selection.")
    except tk.TclError:
        status_label.config(text="PRIMARY selection is empty or not accessible. Highlight text in Text 1 first.")

# Initialize the main window
root = tk.Tk()
root.title("Linux Clipboard (PRIMARY vs CLIPBOARD) Demo")

# --- Instructions ----
tk.Label(root, text="Type and select text in the top box. Observe how PRIMARY and CLIPBOARD selections work independently on Linux (X11).", wraplength=450).pack(pady=5)

# --- Text Widget 1 (Source) ---
tk.Label(root, text="Text 1 (Source - type and select text here):", anchor='w').pack(fill='x', padx=5)
text_widget1 = tk.Text(root, height=5, width=60, wrap=tk.WORD)
text_widget1.insert(tk.END, "Hello, this is some text to demonstrate Linux's multiple clipboards. Select me!")
text_widget1.pack(pady=5, padx=5)

# --- Buttons Frame ---
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Button for CLIPBOARD copy (explicit Ctrl+C equivalent)
btn_copy_clipboard = tk.Button(button_frame, text="Copy Selected to CLIPBOARD (Ctrl+C)", command=copy_to_clipboard)
btn_copy_clipboard.pack(side=tk.LEFT, padx=5)

# Button for CLIPBOARD paste (explicit Ctrl+V equivalent)
btn_paste_clipboard = tk.Button(button_frame, text="Paste from CLIPBOARD (Ctrl+V)", command=paste_from_clipboard)
btn_paste_clipboard.pack(side=tk.LEFT, padx=5)

# Button for PRIMARY paste (implicit middle-click equivalent)
btn_paste_primary = tk.Button(button_frame, text="Paste from PRIMARY (Middle Click)", command=paste_from_primary)
btn_paste_primary.pack(side=tk.LEFT, padx=5)

# --- Text Widget 2 (Destination) ---
tk.Label(root, text="Text 2 (Destination - paste results here):", anchor='w').pack(fill='x', padx=5)
text_widget2 = tk.Text(root, height=5, width=60, wrap=tk.WORD)
text_widget2.pack(pady=5, padx=5)

# --- Status Label ---
status_label = tk.Label(root, text="Ready.", fg="blue")
status_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
