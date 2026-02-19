import { useState } from "react";
import { generateDocs } from "./api";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState("");

  const handleGenerate = async () => {
    const data = await generateDocs(prompt);
    setResult(data.documentation);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>📄 Documentation Generator Agent</h1>

      <textarea
        rows="8"
        style={{ width: "100%" }}
        placeholder="Enter code or description..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button onClick={handleGenerate} style={{ marginTop: 20 }}>
        Generate Documentation
      </button>

      <pre style={{ marginTop: 30, background: "#f4f4f4", padding: 20 }}>
        {result}
      </pre>
    </div>
  );
}
