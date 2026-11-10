import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import { compareDocuments } from "../services/comparisonService";
import { getDocuments } from "../services/documentService";

export default function Comparison() {
  const [documentA, setDocumentA] =
    useState("");

  const [documentB, setDocumentB] =
    useState("");

  const [documents, setDocuments] =
    useState<any[]>([]);

  useEffect(() => {
    loadDocuments();
  }, []);

  const loadDocuments = async () => {
    try {
      const docs = await getDocuments();
      setDocuments(docs);
    } catch (error) {
      console.error(error);
    }
  };
  const [result, setResult] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const handleCompare =
    async () => {

      if (!documentA || !documentB) {
        alert(
          "Please select two documents."
        );
        return;
      }

      if (documentA === documentB) {
        alert(
          "Please select different documents."
        );
        return;
      }

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
        ⚖️ Regulatory Document Comparison
      </h1>
      <p>
        Compare policies, regulations,
        customs guidelines and legal
        documents stored in PolicyLenAI.
      </p>
      <select
        value={documentA}
        onChange={(e) =>
          setDocumentA(
            e.target.value
          )
        }
      >
        <option value="">
          Select First Document
        </option>

        {documents.map((doc) => (
          <option
            key={doc.document_id}
            value={doc.document_id}
          >
            {doc.title}
          </option>
        ))}
      </select>

      <br />
      <br />

      <select
        value={documentB}
        onChange={(e) =>
          setDocumentB(
            e.target.value
          )
        }
      >
        <option value="">
          Select Second Document
        </option>

        {documents.map((doc) => (
          <option
            key={doc.document_id}
            value={doc.document_id}
          >
            {doc.title}
          </option>
        ))}
      </select>

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
          🔍 Analyzing differences between documents...
        </p>
      )}

      {result && (
        <div className="summary-result">
          <h2>
            Comparison Result
          </h2>

          <ReactMarkdown>
            {result}
          </ReactMarkdown>
        </div>
      )}
    </div>
  );
}