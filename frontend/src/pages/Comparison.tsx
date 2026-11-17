import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import { ArrowLeftRight, Scale } from "lucide-react";
import { compareDocuments } from "../services/comparisonService";
import { getDocuments } from "../services/documentService";
import type { Document } from "../types/document";

export default function Comparison() {
  const [documentA, setDocumentA] = useState("");
  const [documentB, setDocumentB] = useState("");
  const [documents, setDocuments] = useState<Document[]>([]);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    getDocuments()
      .then((docs) => setDocuments(Array.isArray(docs) ? docs : []))
      .catch((err) => {
        console.error("Unable to load documents for comparison:", err);
        setError("Could not load the document list. Please refresh and try again.");
      });
  }, []);

  const handleCompare = async () => {
    if (!documentA || !documentB) {
      setError("Please select both documents before comparing.");
      return;
    }
    if (documentA === documentB) {
      setError("Choose two different documents to compare.");
      return;
    }

    setLoading(true);
    setError("");
    setResult("");
    try {
      const response = await compareDocuments(documentA, documentB);
      setResult(response.comparison ?? "No comparison text was returned.");
    } catch (err) {
      console.error("Document comparison failed:", err);
      setError("The comparison could not be completed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-stack">
      <section className="page-intro">
        <span className="section-kicker">REGULATORY ANALYSIS</span>
        <h1>Compare policies</h1>
        <p>Review two documents side by side to understand differences in requirements, provisions and obligations.</p>
      </section>

      <section className="content-card comparison-panel">
        <div className="comparison-title"><div className="comparison-icon"><Scale size={22} /></div><div><strong>Select documents</strong><span>Choose two different documents from your library.</span></div></div>
        <div className="comparison-selectors">
          <label>FIRST DOCUMENT
            <select value={documentA} onChange={(event) => setDocumentA(event.target.value)}>
              <option value="">Select first document</option>
              {documents.map((doc) => <option key={doc.document_id} value={doc.document_id}>{doc.title}</option>)}
            </select>
          </label>
          <div className="comparison-vs"><ArrowLeftRight size={18} /></div>
          <label>SECOND DOCUMENT
            <select value={documentB} onChange={(event) => setDocumentB(event.target.value)}>
              <option value="">Select second document</option>
              {documents.map((doc) => <option key={doc.document_id} value={doc.document_id}>{doc.title}</option>)}
            </select>
          </label>
        </div>
        <button type="button" className="button-primary comparison-submit" onClick={handleCompare} disabled={loading || documents.length < 2}>
          {loading ? "Comparing documents…" : "Compare selected documents"}
        </button>
        {documents.length < 2 && <p className="form-hint">Add at least two documents to start a comparison.</p>}
      </section>

      {error && <div className="inline-alert error" role="alert">{error}</div>}
      {loading && <div className="content-card empty-state">Reviewing both documents and identifying key differences…</div>}
      {result && <section className="summary-result"><span className="section-kicker">COMPARISON OUTPUT</span><h2>Analysis of differences</h2><ReactMarkdown>{result}</ReactMarkdown></section>}
    </div>
  );
}
