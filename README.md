# 🌟 Calmify: Mental Health Assistant

Calmify is a modern mental health assistant leveraging the power of Flask, React, and Hugging Face's models. This application uses state-of-the-art AI technologies like GPT-4 and sentiment analysis models to provide personalized emotional support and guidance. 💡

---

## 🛠️ Features

- **Emotion Detection**: Analyzes user text to understand emotions using the `j-hartmann/emotion-english-distilroberta-base` model. 😊😢😠

- **User-Friendly Interface**: A seamless front-end powered by React. 💻
- **Scalable Backend**: Flask API for efficient communication between the front-end and AI models. ⚙️
- **Personalized Suggestions**: Provides tips and resources for emotional well-being. 🌱

---

## 🚀 Tech Stack

### Frontend:
- React ⚛️
- CSS 🎨
- JavaScript 📜

### Backend:
- Flask 🐍
- Python 🐍



---

## ⚙️ Installation Guide

### Prerequisites:
- Python 3.8 or higher 🐍
- Node.js and npm 📦
- Virtual Environment (venv) 🛡️

### Steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Calmify-Flask-React-HuggingFace-GPT4-Mental-Health-Assistant.git
   cd Calmify-Flask-React-HuggingFace-GPT4-Mental-Health-Assistant
   ```

2. **Setup Backend**:
   ```bash
   cd Backend
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For Mac/Linux
   pip install -r requirements.txt
   ```

3. **Setup Frontend**:
   ```bash
   cd ../Frontend
   npm install
   ```

4. **Run the Application**:
   - Backend:
     ```bash
     cd Backend
     python app.py
     ```
   - Frontend:
     ```bash
     cd Frontend
     npm start
     ```

5. **Access the Application**:
   Open your browser and navigate to: `http://localhost:3000`. 🌐

---

## 🌈 How It Works

1. **User Interaction**:
   - Users input their thoughts or feelings via the React-based interface.

2. **Emotion Analysis**:
   - The input is sent to the Flask backend, which processes it using Hugging Face's sentiment analysis model. 🤔

3. **Response Generation**:
   - GPT-4 generates a personalized response based on the detected emotion and user input. 📝

4. **Display Output**:
   - The response is displayed on the front-end for the user to see and engage with. 💬

---

## 📚 Dependencies

- **Backend**:
  - Flask
  - Transformers (Hugging Face)
  - PyTorch

- **Frontend**:
  - React
  - Axios

---

## 🛡️ Security Considerations

- Ensure sensitive API keys (e.g., OpenAI) are stored in `.env` files and not committed to version control.
- Use HTTPS for secure communication in production.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). 📄

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or create pull requests. Check out our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. 💪

---

## 📞 Support

If you encounter any issues, feel free to contact us at `support@calmify.com` or open an issue on GitHub. 🛠️

---

### 🌟 Thank You for Using Calmify! 🌟

Your mental health matters. Together, let’s create a space where everyone feels supported. 💕

