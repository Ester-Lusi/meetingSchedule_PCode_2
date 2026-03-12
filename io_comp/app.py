import tkinter as tk
from .repository import MemoryRepository
from .service import CalendarService
from .gui import CalendarGUI

def main():
    root = tk.Tk()
    root.geometry("850x500")
    
    # אתחול הרכיבים
    repo = MemoryRepository()
    service = CalendarService()
    
    # יצירת ה-GUI והזרקת התלויות
    app = CalendarGUI(root, repo, service)
    
    root.mainloop()

if __name__ == "__main__":
    main()