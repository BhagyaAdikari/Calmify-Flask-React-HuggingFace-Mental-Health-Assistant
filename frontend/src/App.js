import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);

  const analyzeText = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/analyze", {
        text: inputText,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error analyzing text:", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Mental Health Assistant</h1>
      <textarea
        rows="5"
        placeholder="How are you feeling today?"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={analyzeText}>Analyze</button>
      {result && (
        <div style={{ marginTop: "20px" }}>
          <p><strong>Emotion:</strong> {result.emotion}</p>
          <p><strong>Response:</strong> {result.response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
