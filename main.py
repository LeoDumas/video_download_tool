from typing import Optional, Tuple, Union
import customtkinter, os

# import Tools
from tools.youtube import download_youtube, getTitle
from tools.reddit import download_reddit, getTitle


class App(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title("Global Downloader")
        self.geometry("300x220")
        
        self.DEFAULT_SAVE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
        
        self.available_platform_label = customtkinter.CTkLabel(self, text="YouTube, Reddit, Twitter")
        self.available_platform_label.grid(row=0, column=0, padx=1, pady=10)
        
        self.link_entry = customtkinter.CTkEntry(self, height=30, width=250, placeholder_text="Video link ...")
        self.link_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        self.download_button = customtkinter.CTkButton(self, text="Dowload", command=self.downloadVideo)
        self.download_button.grid(row=2, column=0, padx=10, pady=10)
        
        
        
    def downloadVideo(self):
        value = self.link_entry.get()
        print(self.DEFAULT_SAVE_DIRECTORY)
        if value != "":
            
            if 'reddit.com' in value:
                download_reddit(value, self.DEFAULT_SAVE_DIRECTORY)
                
            elif 'twitter.com' in value:
                print("Downloading from twitter")
                
            elif 'youtube.com' in value:
                download_youtube(value, self.DEFAULT_SAVE_DIRECTORY)
                
            else:
                print("Unknown link")
            
        else:
            print("No link found")
        
app = App()
app.mainloop()