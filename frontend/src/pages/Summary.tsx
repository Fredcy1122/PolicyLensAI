import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { FileText, Sparkles } from "lucide-react";
import ReactMarkdown from "react-markdown";
import { getDocuments } from "../services/documentService";
import { generateDocumentSummary } from "../services/summaryService";
import type { Document } from "../types/document";

export default function Summary() {
  const { documentId } = useParams();
  const [documents, setDocuments] = useState<Document[]>([]);
  const [selectedDocument, setSelectedDocument] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    if (documentId) {
      setSelectedDocument(documentId);
      generateSummary(documentId);
    } else {
      getDocuments()
        .then((data) => setDocuments(Array.isArray(data) ? data : []))
        .catch((err) => {
          console.error("Unable to load documents:", err);
          setError("Could not load your documents. Please try again.");
        });
    }
  }, [documentId]);

  const generateSummary = async (id: string) => {
    if (!id) return;
    setLoading(true);
    setError("");
    setSummary("");
    try {
      const result = await generateDocumentSummary(id);
      setSummary(result.summary ?? "");
    } catch (err) {
      console.error("Summary generation failed:", err);
      setError("The summary could not be generated. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleGenerate = () => {
    if (!selectedDocument) {
      setError("Select a document before generating its summary.");
      return;
    }
    if (selectedDocument !== documentId) {
      navigate(`/summary/${selectedDocument}`);
    } else {
      generateSummary(selectedDocument);
    }
  };

  const selected = documents.find((doc) => doc.document_id === selectedDocument);

  return (
    <div className="page-stack">
      <section className="page-intro">
        <span className="section-kicker">DOCUMENT INTELLIGENCE</span>
        <h1>Policy summaries</h1>
        <p>Generate a concise overview of a document in your policy library.</p>
      </section>

      {!documentId && (
        <section className="content-card summary-selector">
          <div className="summary-selector-icon"><Sparkles size={22} /></div>
          <div className="summary-selector-copy">
            <strong>Choose a document to summarise</strong>
            <span>Select a policy or regulation from your library.</span>
          </div>
          <select aria-label="Select document" value={selectedDocument} onChange={(event) => setSelectedDocument(event.target.value)}>
            <option value="">Select a document</option>
            {documents.map((doc) => <option key={doc.document_id} value={doc.document_id}>{doc.title}</option>)}
          </select>
          <button type="button" className="button-primary" onClick={handleGenerate} disabled={!selectedDocument}>
            Generate summary
          </button>
          {!documents.length && <span className="summary-hint">Upload a document first from the Documents page.</span>}
        </section>
      )}

      {documentId && (
        <section className="summary-document-heading">
          <div className="document-file-icon"><FileText size={20} /></div>
          <div>
            <span className="section-kicker">SELECTED DOCUMENT</span>
            <strong>{selected?.title ?? documentId}</strong>
          </div>
          <button type="button" className="button-secondary" onClick={() => navigate("/summary")}>Choose another</button>
        </section>
      )}

      {error && <div className="inline-alert error" role="alert">{error}</div>}
      {loading && <div className="content-card empty-state"><Sparkles size={25} /><strong>Generating your summary…</strong><span>This may take a little while depending on the document.</span></div>}
      {summary && (
        <section className="summary-result">
          <div className="section-heading"><div><span className="section-kicker">AI-GENERATED OVERVIEW</span><h2>Document summary</h2></div><span className="status-badge success">Complete</span></div>
          <ReactMarkdown>{summary}</ReactMarkdown>
        </section>
      )}
    </div>
  );
}
