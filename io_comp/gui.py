import tkinter as tk
import os
from tkinter import messagebox, ttk
from datetime import datetime
from .models import Event

class CalendarGUI:
    def __init__(self, root, repo, service):
        self.root = root
        self.repo = repo
        self.service = service
        self.root.title("Comp.io Calendar Search & Manage")

        # --- אזור בקרה ---
        input_frame = tk.LabelFrame(root, text="ניהול פגישות (הוספה/טעינה/מחיקה)", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(input_frame, text="שם:").grid(row=0, column=0)
        self.ent_name = tk.Entry(input_frame, width=10); self.ent_name.grid(row=0, column=1, padx=2)
        
        tk.Label(input_frame, text="התחלה:").grid(row=0, column=2)
        self.ent_start = tk.Entry(input_frame, width=6); self.ent_start.insert(0, "08:00"); self.ent_start.grid(row=0, column=3, padx=2)
        
        tk.Label(input_frame, text="סיום:").grid(row=0, column=4)
        self.ent_end = tk.Entry(input_frame, width=6); self.ent_end.insert(0, "09:00"); self.ent_end.grid(row=0, column=5, padx=2)

        tk.Button(input_frame, text="הוסף פגישה", command=self.add_manual).grid(row=0, column=6, padx=5)
        tk.Button(input_frame, text="📂 טען CSV", command=self.load_csv_from_resources, bg="#e3f2fd").grid(row=0, column=7, padx=5)
        tk.Button(input_frame, text="🗑️ מחק נבחר", command=self.delete_selected, bg="#ffcdd2").grid(row=0, column=8, padx=5)

        # --- טבלה ---
        self.tree = ttk.Treeview(root, columns=("Person", "Subject", "Start", "End"), show='headings')
        self.tree.heading("Person", text="משתתף"); self.tree.heading("Subject", text="נושא")
        self.tree.heading("Start", text="התחלה"); self.tree.heading("End", text="סיום")
        self.tree.pack(padx=10, pady=5, fill="both", expand=True)

        # --- אזור חישוב ---
        action_frame = tk.Frame(root, pady=10)
        action_frame.pack(fill="x", padx=10)
        
        tk.Label(action_frame, text="משך פגישה (דקות):").pack(side="left")
        self.ent_duration = tk.Entry(action_frame, width=5); self.ent_duration.insert(0, "60"); self.ent_duration.pack(side="left", padx=5)
        
        tk.Button(action_frame, text="🔍 מצא זמן פנוי לכולם", command=self.calculate, bg="#c8e6c9", height=2).pack(side="right", fill="x", expand=True)

    def delete_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("אזהרה", "יש לבחור פגישה מהטבלה כדי למחוק אותה")
            return
        index = self.tree.index(selected_item[0])
        if messagebox.askyesno("מחיקה", "האם להסיר פגישה זו מהחישוב?"):
            self.repo.remove_event(index)
            self.update_table()

    def load_csv_from_resources(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        csv_path = os.path.join(project_root, "resources", "calendar.csv")
        try:
            self.repo.load_from_csv(csv_path)
            self.update_table()
        except Exception as e: messagebox.showerror("שגיאה", str(e))

    def add_manual(self):
        try:
            ev = Event(self.ent_name.get().strip(), "Manual Entry",
                datetime.strptime(self.ent_start.get().strip(), "%H:%M").time(),
                datetime.strptime(self.ent_end.get().strip(), "%H:%M").time())
            self.repo.add_event(ev)
            self.update_table()
        except Exception as e: messagebox.showerror("שגיאה", "נתונים לא תקינים")

    def update_table(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for e in self.repo.get_events():
            self.tree.insert("", "end", values=(e.person, e.subject, e.start.strftime("%H:%M"), e.end.strftime("%H:%M")))

    def calculate(self):
        events = self.repo.get_events()
        if not events: return
        people = list(set(e.person for e in events))
        slots = self.service.find_available_slots(events, people, int(self.ent_duration.get()))
        res = "חלונות פנויים:\n" + "\n".join([f"✨ {s.strftime('%H:%M')} - {e.strftime('%H:%M')}" for s, e in slots])
        messagebox.showinfo("תוצאות", res if slots else "לא נמצא זמן פנוי")