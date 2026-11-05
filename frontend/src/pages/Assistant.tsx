import { useState } from "react";
import { askQuestion } from "../services/chatService";

export default function Assistant() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [confidence, setConfidence] = useState("");
  const [citations, setCitations] = useState<any[]>([]);

  const handleAsk = async () => {
    if (!question) return;

    try {
      setLoading(true);

      const result = await askQuestion(
        question
      );

      setAnswer(result.answer);

      setConfidence(
        result.confidence || ""
      );

      setCitations(
        result.citations || []
      );
    } catch (error) {
      console.error(error);

      setAnswer(
        "Error communicating with PolicyLens backend."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        padding: "2rem",
        maxWidth: "1000px",
        margin: "0 auto",
      }}
    >
      <h1>PolicyLens AI</h1>

      <textarea
        rows={5}
        placeholder="Ask a policy or regulatory question..."
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
        style={{
          width: "100%",
          padding: "1rem",
        }}
      />

      <br />
      <br />

      <button onClick={handleAsk}>
        Ask Question
      </button>

      {loading && (
        <p>
          Thinking...
        </p>
      )}

      {answer && (
        <>
          <h2>Answer</h2>

          <p>{answer}</p>

          <h3>Confidence</h3>

          <p>{confidence}</p>

          <h3>Citations</h3>

          <ul>
            {citations.map(
              (citation, index) => (
                <li key={index}>
                  {citation.title}
                  {" "}
                  (
                  Page {citation.page}
                  )
                </li>
              )
            )}
          </ul>
        </>
      )}
    </div>
  );
}