from typing import Optional, Tuple, Union
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
import customtkinter, os 

# import Tools
from tools.youtube import download_youtube, get_title
from tools.reddit import download_reddit, get_title


class App(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title("Global Downloader")
        self.geometry("300x200")
        
        self.available_platform_label = customtkinter.CTkLabel(self, text="YouTube, Reddit, Twitter")
        self.available_platform_label.grid(row=0, column=0, padx=1, pady=10)
        
        self.link_entry = customtkinter.CTkEntry(self, height=30, width=250, placeholder_text="Video link ...")
        self.link_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        self.download_button = customtkinter.CTkButton(self, text="Dowload", command=self.downloadVideo)
        self.download_button.grid(row=2, column=0, padx=10, pady=10)
        
        
    def show_checkmark(self, folder_loc):
        res = CTkMessagebox(title="Download complete" message="The video has been downloaded successfully", icon="check", option_1="Close")
        if res =="Close":
            App.destroy()
            os.startfile(folder_loc)
        else:
            App.destroy()
    
    def show_error():
        CTkMessagebox(title="Download error", message="Failed to download the video", icon="cancel")
    
    def downloadVideo(self):
        value = self.link_entry.get()
        if value != "":
            
            self.save_path = filedialog.askdirectory()
            print(self.save_path)
            
            if 'reddit.com' in value:
                if download_reddit(value, self.save_path) == 1:
                    self.show_checkmark(self.save_path)
                else:
                    self.show_error()
                
            elif 'twitter.com' in value:
                print("Downloading from twitter")
                
            elif 'youtube.com' in value:
                if download_youtube(value, self.save_path) == 1:
                    self.show_checkmark(self.save_path)
                else:
                    self.show_error()
                
            else:
                print("Unknown link")
            
        else:
            print("No link found")
        
app = App()
app.mainloop()