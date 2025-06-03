import customtkinter as ctk
import os
import shutil
import tempfile
import threading
import subprocess
from pathlib import Path
from tkinter import messagebox

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SystemCleanerApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("System Cleaner")
        self.window.geometry("400x350")
        self.window.resizable(False, False)
        
        # Set the window icon
        try:
            self.window.iconbitmap("open-folder.ico")
        except Exception:
            # If folder.png doesn't exist or can't be loaded, continue without icon
            print("Warning: Could not load open-folder.ico icon file")
        
        # Center the window
        self.center_window()
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self.window)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title label
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="System Cleaner", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=(20, 30))
        
        # Clear Temp Data button
        self.temp_button = ctk.CTkButton(
            self.main_frame,
            text="Clear Temp Data",
            font=ctk.CTkFont(size=16),
            height=50,
            width=200,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.clear_temp_data_thread
        )
        self.temp_button.pack(pady=10)
        
        # Clear Recycle Bin button
        self.recycle_button = ctk.CTkButton(
            self.main_frame,
            text="Clear Recycle Bin",
            font=ctk.CTkFont(size=16),
            height=50,
            width=200,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.clear_recycle_bin_thread
        )
        self.recycle_button.pack(pady=10)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Ready",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white"
        )
        self.status_label.pack(pady=(25, 15))
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=300)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        
    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
    
    def get_folder_size(self, folder_path):
        """Calculate folder size in GB"""
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                    except (OSError, FileNotFoundError):
                        continue
        except (OSError, FileNotFoundError):
            pass
        return total_size / (1024**3)  # Convert to GB
    
    def clear_temp_data_thread(self):
        """Run temp data clearing in a separate thread"""
        thread = threading.Thread(target=self.clear_temp_data, daemon=True)
        thread.start()
    
    def clear_temp_data(self):
        """Clear temporary files from %temp% folder"""
        try:
            # Disable button and show progress
            self.temp_button.configure(state="disabled")
            self.status_label.configure(text="Scanning temp folder...")
            self.progress_bar.set(0.1)
            
            temp_path = tempfile.gettempdir()
            
            # Calculate initial size
            initial_size = self.get_folder_size(temp_path)
            self.progress_bar.set(0.3)
            
            deleted_files = 0
            total_files = 0
            
            # Count total files first
            for root, dirs, files in os.walk(temp_path):
                total_files += len(files)
            
            self.status_label.configure(text=f"Deleting {total_files} temp files...")
            self.progress_bar.set(0.5)
            
            # Delete files
            for root, dirs, files in os.walk(temp_path, topdown=False):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        deleted_files += 1
                    except (OSError, PermissionError, FileNotFoundError):
                        continue
                
                # Try to remove empty directories
                for dir_name in dirs:
                    try:
                        dir_path = os.path.join(root, dir_name)
                        os.rmdir(dir_path)
                    except (OSError, PermissionError):
                        continue
            
            self.progress_bar.set(0.8)
            
            # Calculate final size
            final_size = self.get_folder_size(temp_path)
            freed_space = initial_size - final_size
            
            self.progress_bar.set(1.0)
            
            # Show success message
            message = f"Temp data cleared successfully!\n\n"
            message += f"Files deleted: {deleted_files}\n"
            message += f"Space freed: {freed_space:.2f} GB"
            
            messagebox.showinfo("Success", message)
            self.status_label.configure(text="Temp data cleared successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error clearing temp data: {str(e)}")
            self.status_label.configure(text="Error clearing temp data")
        
        finally:
            self.temp_button.configure(state="normal")
            self.progress_bar.set(0)
    
    def clear_recycle_bin_thread(self):
        """Run recycle bin clearing in a separate thread"""
        thread = threading.Thread(target=self.clear_recycle_bin, daemon=True)
        thread.start()
    
    def clear_recycle_bin(self):
        """Clear the recycle bin using PowerShell command"""
        try:
            # Disable button and show progress
            self.recycle_button.configure(state="disabled")
            self.status_label.configure(text="Emptying recycle bin...")
            self.progress_bar.set(0.5)
            
            # Use PowerShell command to empty recycle bin
            powershell_cmd = [
                "powershell.exe",
                "-Command",
                "Clear-RecycleBin -Force -Confirm:$false"
            ]
            
            # Run the PowerShell command
            result = subprocess.run(
                powershell_cmd,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            self.progress_bar.set(1.0)
            
            if result.returncode == 0:
                messagebox.showinfo("Success", "Recycle bin emptied successfully!")
                self.status_label.configure(text="Recycle bin emptied successfully")
            else:
                # Try alternative method using rd command
                try:
                    # Get all drive letters
                    drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
                    
                    for drive in drives:
                        recycle_path = os.path.join(drive, "$Recycle.Bin")
                        if os.path.exists(recycle_path):
                            # Use rd command to remove contents
                            subprocess.run([
                                "cmd", "/c", f"rd /s /q \"{recycle_path}\" 2>nul"
                            ], creationflags=subprocess.CREATE_NO_WINDOW)
                    
                    messagebox.showinfo("Success", "Recycle bin emptied using alternative method!")
                    self.status_label.configure(text="Recycle bin emptied successfully")
                    
                except Exception as alt_error:
                    messagebox.showwarning("Warning", 
                        f"Could not empty recycle bin completely.\n"
                        f"You might need to run as administrator.\n"
                        f"Error: {str(alt_error)}")
                    self.status_label.configure(text="Recycle bin operation incomplete")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error emptying recycle bin: {str(e)}")
            self.status_label.configure(text="Error emptying recycle bin")
        
        finally:
            self.recycle_button.configure(state="normal")
            self.progress_bar.set(0)
    
    def run(self):
        """Start the application"""
        self.window.mainloop()

if __name__ == "__main__":
    try:
        app = SystemCleanerApp()
        app.run()
    except ImportError as e:
        print("Required packages not found. Please install them using:")
        print("pip install customtkinter")
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")