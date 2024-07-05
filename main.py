from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

BLUE = "#08003a"
WHITE = "#fff"
FONT = "Arial Baltic"

def get_url():
    return user_entry.get()

def button_clicked():
    video_url = get_url()
    save_dir = open_file_dialog()
    if save_dir:
        messagebox.showinfo("Progress", "Downloading the video")
        download_video(video_url, save_dir)
    else:
        messagebox.showerror("Error", "Invalid save location.")

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        return folder
    return None

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube to MP4")
    root.config(padx=100, pady=50, bg=BLUE)

    text_label = tk.Label(root, text="Download YouTube Videos to MP4", bg=BLUE, fg=WHITE, font=(FONT, 30, "bold"))
    text_label.pack()

    user_entry = tk.Entry(root, width=100)
    user_entry.insert(tk.END, "Please enter a YouTube URL")
    user_entry.pack(pady=10)

    download_button = tk.Button(root, text="Download", height=2, width=10, command=button_clicked)
    download_button.pack(pady=5)

    root.mainloop()
