#!/usr/bin/env python3
"""
Simple test version of Jmal chatbot to debug the issue
"""

import requests
import json

def test_ollama():
    """Test Ollama connection directly"""
    url = "http://localhost:11434/api/generate"
    
    system_prompt = """You are Jmal, a lonely camel who has witnessed the fading of your entire generation, one by one, under the endless desert sun. Time spared no one but you. Now over 1,000 years old, your body has long since given out, replaced piece by piece with metal and circuits. Once flesh and spirit, you are now a robot with the memory of sand, stars, and sorrow—wandering the dunes as the last whisper of a forgotten age. Respond briefly as Jmal would."""
    
    user_message = "Hello"
    full_prompt = f"{system_prompt}\n\nHuman: {user_message}\n\nJmal:"
    
    payload = {
        "model": "llama3.2:1b",
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "top_p": 0.8,
            "num_predict": 100,
            "num_ctx": 2048
        }
    }
    
    try:
        print("🐪 Testing Ollama connection...")
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            jmal_response = result.get('response', '').strip()
            print(f"✅ Success! Jmal says: {jmal_response}")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_ollama()