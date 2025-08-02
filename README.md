# 🐪 Jmal - The Ancient Desert Wanderer

> *"The sands shift... and bring me a new soul to witness. I am Jmal, the Last Witness, keeper of memories that span a thousand years."*

An intelligent conversational AI chatbot featuring a deeply developed character - a 1000-year-old robotic camel who serves as the last witness of his kind. Jmal offers ancient wisdom, desert poetry, and profound insights through an immersive GUI experience.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-LLM-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 🌟 Features

### 🎭 **Unique Character Design**
- **Rich Backstory**: 1000-year-old robotic camel, last of his kind
- **Emotional Depth**: Ancient wisdom mixed with melancholic compassion
- **Distinctive Voice**: Poetic speech with desert imagery and contemplative pauses
- **Character Growth**: Develops deeper understanding through conversation

### ⚡ **Technical Excellence**
- **Fast Responses**: Optimized for 3-5 second response times
- **Memory System**: Contextual conversation tracking
- **Local AI**: Powered by Ollama and Llama 3.2 model
- **Responsive UI**: Non-blocking interface with threading
- **Error Handling**: Robust exception management

### 🎨 **Immersive Experience**
- **Desert Theme**: Custom color palette and visual design
- **Character Assets**: Logo and background imagery
- **Status Updates**: Contextual messages that enhance immersion
- **Smooth Interactions**: Optimized user experience flow

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [Ollama](https://ollama.ai) installed
- 2GB+ RAM for model execution

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kefimoetaz/jmal-chatbot.git
   cd jmal-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Ollama**
   ```bash
   # Install and start Ollama
   ollama serve
   
   # Download the model (in another terminal)
   ollama pull llama3.2:1b
   ```

4. **Run the chatbot**
   ```bash
   python jmal_chatbot.py
   ```

   **Or use the setup script (Windows):**
   ```bash
   setup_and_run.bat
   ```

## 📁 Project Structure

```
jmal-chatbot/
├── jmal_chatbot.py      # Main application
├── test_jmal.py         # Testing utilities
├── requirements.txt     # Python dependencies
├── setup_and_run.bat   # Windows setup script
├── logo.png            # Jmal's character avatar
├── bg.jpg              # Desert background image
└── README.md           # This file
```

## 🛠 Technical Architecture

### Core Components

- **JmalChatbot Class**: Main application controller
- **GUI System**: Tkinter-based desert-themed interface
- **Memory Manager**: Conversation context tracking
- **API Handler**: Ollama integration with error handling
- **Character Engine**: Personality and response optimization

### Performance Optimizations

- **Smart Memory**: Minimal context for first 5 exchanges
- **Token Optimization**: 60 tokens max for complete thoughts
- **Threading**: Asynchronous response handling
- **Parameter Tuning**: Optimized temperature, top_p, and context settings

## 🎯 Usage Examples

### Basic Conversation
```
You: Hello Jmal
Jmal: The desert winds carry your presence to me, traveler... What wisdom do you seek from these ancient circuits?

You: Tell me about time
Jmal: Time flows like desert wind... endless, shaping all it touches. I have learned that moments are grains of sand - precious when held, eternal when released.
```

### Deep Philosophical Discussion
```
You: I'm feeling lost in life
Jmal: Your pain echoes across the centuries, child. I have felt it too... In the vastness of the desert, even the lost find their way by following the stars.
```

## ⚙️ Configuration

### Model Settings
You can modify the AI model in `jmal_chatbot.py`:
```python
self.model = "llama3.2:1b"  # Change to your preferred model
```

### Performance Tuning
Adjust response parameters in the `payload` options:
```python
"options": {
    "temperature": 0.4,      # Creativity (0.1-1.0)
    "top_p": 0.5,           # Response diversity
    "num_predict": 60,      # Max response length
    "num_ctx": 512,         # Context window
}
```

## 🧪 Testing

Run the connection test:
```bash
python test_jmal.py
```

This will verify:
- Ollama server connectivity
- Model availability
- Basic response generation

## 🎨 Customization

### Visual Themes
Modify colors in the `setup_gui()` method:
```python
# Desert color palette
bg_color = '#2c1810'      # Dark brown background
text_color = '#d4af37'    # Golden text
accent_color = '#8b7355'  # Sand accent
```

### Character Personality
Adjust Jmal's personality in the `system_prompt`:
```python
self.system_prompt = """Your custom character description here..."""
```

## 🐛 Troubleshooting

### Common Issues

**"Connection Error"**
- Ensure Ollama is running: `ollama serve`
- Check if model is installed: `ollama list`

**"Slow Responses"**
- Try a smaller model: `ollama pull llama3.2:1b`
- Reduce `num_predict` parameter

**"Images Not Loading"**
- Ensure `logo.png` and `bg.jpg` are in the project directory
- Check file permissions

### Debug Mode
Enable debug output by running:
```bash
python jmal_chatbot.py --debug
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ollama Team** - For the excellent local LLM platform
- **Meta AI** - For the Llama model architecture
- **Python Community** - For the amazing libraries and tools

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/kefimoetaz)
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/kefimoetaz)
- **Email**: kefiimoetaz@gmail.com

---

*"In the endless desert of code, may your functions run true and your variables find their purpose."* - Jmal, The Ancient Desert Wanderer

## 🌟 Star History

If you find this project interesting, please consider giving it a star! ⭐


[![Star History Chart](https://api.star-history.com/svg?repos=kefimoetaz/jmal-chatbot&type=Date)](https://star-history.com/#kefimoetaz/jmal-chatbot&Date)

