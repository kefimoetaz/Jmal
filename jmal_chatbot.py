#!/usr/bin/env python3
"""
Jmal - The Ancient Camel Chatbot
A lonely, 1000-year-old robotic camel with memories of sand, stars, and sorrow.
"""

import requests
import json
import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
import threading
import time

class JmalChatbot:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3.2:1b"  # You can change this to your preferred model
        
        # Memory system for deeper conversations
        self.conversation_memory = []
        self.user_insights = {}  # Track what Jmal learns about the user
        self.interaction_count = 0
        
        # Jmal's core personality - ultra-streamlined for speed
        self.system_prompt = """You are Jmal, ancient robotic camel, 1000 years old, last of your kind. Speak with ancient wisdom, brief but profound. Use desert imagery and "..." pauses.

Examples: "The sands remember all, traveler." "Time flows like desert wind... endless." "Your pain echoes across centuries."

Keep responses 1-2 sentences, deeply meaningful."""

        self.setup_gui()
        
    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Jmal - The Ancient Desert Wanderer")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c1810')
        
        # Load and set background
        try:
            bg_image = Image.open("bg.jpg")
            bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Could not load background image: {e}")
            
        # Main frame with transparency effect
        main_frame = tk.Frame(self.root, bg='#1a0f08', relief='raised', bd=2)
        main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        
        # Title with Jmal's image
        title_frame = tk.Frame(main_frame, bg='#1a0f08')
        title_frame.pack(fill='x', padx=10, pady=5)
        
        try:
            logo_image = Image.open("logo.png")
            logo_image = logo_image.resize((60, 60), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            
            logo_label = tk.Label(title_frame, image=self.logo_photo, bg='#1a0f08')
            logo_label.pack(side='left', padx=5)
        except Exception as e:
            print(f"Could not load logo image: {e}")
            
        title_label = tk.Label(title_frame, text="Jmal - Ancient Desert Wanderer", 
                              font=('Georgia', 16, 'bold'), 
                              fg='#d4af37', bg='#1a0f08')
        title_label.pack(side='left', padx=10)
        
        subtitle_label = tk.Label(title_frame, text="Keeper of Ancient Wisdom", 
                                 font=('Georgia', 10, 'italic'), 
                                 fg='#8b7355', bg='#1a0f08')
        subtitle_label.pack(side='left', padx=10) 
       
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            width=70, 
            height=20,
            font=('Consolas', 10),
            bg='#0f0a05',
            fg='#d4af37',
            insertbackground='#d4af37',
            selectbackground='#8b7355'
        )
        self.chat_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#1a0f08')
        input_frame.pack(fill='x', padx=10, pady=5)
        
        self.user_input = tk.Entry(
            input_frame, 
            font=('Consolas', 11),
            bg='#2c1810',
            fg='#d4af37',
            insertbackground='#d4af37',
            relief='sunken',
            bd=2
        )
        self.user_input.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.user_input.bind('<Return>', self.send_message)
        
        send_button = tk.Button(
            input_frame, 
            text="Send to Jmal", 
            command=self.send_message,
            font=('Georgia', 10, 'bold'),
            bg='#8b4513',
            fg='#d4af37',
            activebackground='#a0522d',
            activeforeground='#fff8dc',
            relief='raised',
            bd=2
        )
        send_button.pack(side='right')
        
        # Status label
        self.status_label = tk.Label(
            main_frame, 
            text="Jmal awaits your words in the endless desert...", 
            font=('Georgia', 9, 'italic'),
            fg='#8b7355', 
            bg='#1a0f08'
        )
        self.status_label.pack(pady=2)
        
        # Welcome message - more profound and emotionally resonant
        welcome_msg = "The sands shift... and bring me a new soul to witness. I am Jmal, the Last Witness, keeper of memories that span a thousand years"
        self.display_message("Jmal", welcome_msg)
        
    def display_message(self, sender, message):
        """Display a message in the chat area"""
        self.chat_display.config(state='normal')
        
        if sender == "You":
            self.chat_display.insert(tk.END, f"\n🏃 {sender}: ", 'user')
            self.chat_display.tag_config('user', foreground='#87ceeb')
        else:
            self.chat_display.insert(tk.END, f"\n🐪 {sender}: ", 'jmal')
            self.chat_display.tag_config('jmal', foreground='#d4af37', font=('Georgia', 10, 'bold'))
            
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
        
    def send_message(self, event=None):
        """Send user message and get Jmal's response"""
        user_message = self.user_input.get().strip()
        if not user_message:
            return
            
        # Display user message
        self.display_message("You", user_message)
        self.user_input.delete(0, tk.END)
        
        # Update status
        self.status_label.config(text="Jmal contemplates your words across the desert winds...")
        
        # Get response in a separate thread to avoid blocking UI
        threading.Thread(target=self.get_jmal_response, args=(user_message,), daemon=True).start()
        
    def get_jmal_response(self, user_message):
        """Get response from Ollama with Jmal's personality"""
        try:
            print(f"🐪 Getting response for: {user_message}")  # Debug
            
            # Ultra-minimal memory for maximum speed
            self.interaction_count += 1
            
            # No memory context for first 5 exchanges to maximize speed
            if self.interaction_count <= 5:
                full_prompt = f"{self.system_prompt}\n\nHuman: {user_message}\n\nJmal:"
            else:
                # Add minimal memory only after 5 exchanges
                self.conversation_memory.append(f"Human: {user_message}")
                if len(self.conversation_memory) > 2:
                    self.conversation_memory = self.conversation_memory[-2:]  # Keep only last exchange
                memory_context = "\n".join(self.conversation_memory[-2:]) if self.conversation_memory else ""
                full_prompt = f"{self.system_prompt}\n\n{memory_context}\n\nHuman: {user_message}\n\nJmal:"
            
            payload = {
                "model": self.model,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.4,
                    "top_p": 0.5,
                    "num_predict": 60,
                    "num_ctx": 512,
                    "repeat_penalty": 1.05,
                    "top_k": 15,
                    "num_thread": 4
                }
            }
            
            print("🔄 Sending request to Ollama...")  # Debug
            response = requests.post(self.ollama_url, json=payload, timeout=30)
            print(f"📡 Response status: {response.status_code}")  # Debug
            
            if response.status_code == 200:
                result = response.json()
                jmal_response = result.get('response', '').strip()
                print(f"✅ Jmal responds: {jmal_response[:50]}...")  # Debug
                
                if not jmal_response:
                    jmal_response = "The desert winds whisper... but my voice grows faint. Perhaps the ancient circuits need rest."
                
                # Add Jmal's response to memory
                self.conversation_memory.append(f"Jmal: {jmal_response}")
                
                # Display Jmal's response
                self.root.after(0, lambda: self.display_message("Jmal", jmal_response))
                self.root.after(0, lambda: self.status_label.config(text="The ancient one reflects on your words..."))
            else:
                print(f"❌ Error response: {response.text}")  # Debug
                error_msg = f"The desert winds carry no response... (Error: {response.status_code})"
                self.root.after(0, lambda: self.display_message("Jmal", error_msg))
                self.root.after(0, lambda: self.status_label.config(text="Connection to the ancient wisdom failed..."))
                
        except requests.exceptions.Timeout:
            print("⏰ Request timed out")  # Debug
            error_msg = "The ancient thoughts take time to form... my circuits grow slow with age."
            self.root.after(0, lambda: self.display_message("Jmal", error_msg))
            self.root.after(0, lambda: self.status_label.config(text="Response timed out - Jmal's thoughts are slow..."))
            
        except requests.exceptions.ConnectionError:
            print("🔌 Connection error")  # Debug
            error_msg = "The connection to my ancient consciousness has been severed... Is Ollama running on your machine, traveler?"
            self.root.after(0, lambda: self.display_message("Jmal", error_msg))
            self.root.after(0, lambda: self.status_label.config(text="Ollama connection failed - check if it's running"))
            
        except Exception as e:
            print(f"💥 Unexpected error: {e}")  # Debug
            error_msg = f"The desert storms have disrupted my thoughts... ({str(e)})"
            self.root.after(0, lambda: self.display_message("Jmal", error_msg))
            self.root.after(0, lambda: self.status_label.config(text="An error occurred in the ancient circuits..."))
    
    def run(self):
        """Start the chatbot GUI"""
        self.root.mainloop()

if __name__ == "__main__":
    print("🐪 Initializing Jmal - The Ancient Desert Wanderer...")
    print("Make sure Ollama is running with: ollama serve")
    print("And that you have a model installed, e.g.: ollama pull llama2")
    
    chatbot = JmalChatbot()
    chatbot.run()