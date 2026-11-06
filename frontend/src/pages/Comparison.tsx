import { useState } from "react";
import { compareDocuments } from "../services/comparisonService";

export default function Comparison() {
  const [documentA, setDocumentA] =
    useState("");

  const [documentB, setDocumentB] =
    useState("");

  const [result, setResult] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const handleCompare =
    async () => {
      try {
        setLoading(true);

        const response =
          await compareDocuments(
            documentA,
            documentB
          );

        setResult(
          response.comparison
        );
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

  return (
    <div>
      <h1>
        ⚖️ Policy Comparison
      </h1>

      <textarea
        rows={10}
        className="summary-textarea"
        placeholder="Paste first document..."
        value={documentA}
        onChange={(e) =>
          setDocumentA(
            e.target.value
          )
        }
      />

      <br />
      <br />

      <textarea
        rows={10}
        className="summary-textarea"
        placeholder="Paste second document..."
        value={documentB}
        onChange={(e) =>
          setDocumentB(
            e.target.value
          )
        }
      />

      <br />
      <br />

      <button
        className="summary-button"
        onClick={
          handleCompare
        }
      >
        Compare Documents
      </button>

      {loading && (
        <p>
          Comparing...
        </p>
      )}

      {result && (
        <div className="summary-result">
          <h2>
            Comparison Result
          </h2>

          <pre>
            {result}
          </pre>
        </div>
      )}
    </div>
  );
}