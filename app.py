import tkinter as tk
from tkinter import messagebox
import cv2
import os

def get_version():
    try:
        with open("version.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"

def check_for_updates(current_version):
    """
    Simulate checking for an update.
    In a real-world scenario, you might fetch the new version from a remote server.
    Here, we simulate that if the current version is not '2.0.0', then '2.0.0' is available.
    """
    new_version = "2.0.0"
    if current_version != new_version:
        return new_version
    return None

def main():
    current_version = get_version()
    root = tk.Tk()
    root.title(f"Simple App - v{current_version}")

    # Main label with app version
    label = tk.Label(root, text=f"Welcome to SimpleApp! Version: {current_version}", padx=20, pady=20)
    label.pack()

    # Display OpenCV version (dependency check)
    cv_version = cv2.__version__
    cv_label = tk.Label(root, text=f"OpenCV Version: {cv_version}")
    cv_label.pack()

    # Button to check for updates
    def update_check():
        new_version = check_for_updates(current_version)
        if new_version:
            if messagebox.askyesno("Update Available", f"A new version ({new_version}) is available. Update now?"):
                # Simulate an update:
                # Write the new version to version.txt and restart the app.
                with open("version.txt", "w") as f:
                    f.write(new_version)
                messagebox.showinfo("Update", "The app will now restart to update.")
                root.destroy()
                # In a real-world scenario, download and replace the .exe.
                # Here, we simulate by restarting the built executable.
                os.system("start SimpleAppTest.exe")
        else:
            messagebox.showinfo("Update", "You are using the latest version.")

    update_btn = tk.Button(root, text="Check for Updates", command=update_check)
    update_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
