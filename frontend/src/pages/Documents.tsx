import { useEffect, useMemo, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { FileText, Search, UploadCloud, X } from "lucide-react";
import { getDocuments, uploadDocument } from "../services/documentService";
import type { Document } from "../types/document";

export default function Documents() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [message, setMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);
  const [searchParams] = useSearchParams();
  const [searchTerm, setSearchTerm] = useState(searchParams.get("search") ?? "");
  const navigate = useNavigate();

  const loadDocuments = async () => {
    try {
      const data = await getDocuments();
      setDocuments(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error("Unable to load documents:", error);
      setMessage({ type: "error", text: "Could not load the document library. Please try again." });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDocuments();
  }, []);

  useEffect(() => {
    setSearchTerm(searchParams.get("search") ?? "");
  }, [searchParams]);

  const handleUpload = async () => {
    if (!selectedFile || uploading) return;
    if (!selectedFile.name.toLowerCase().endsWith(".pdf")) {
      setMessage({ type: "error", text: "Please select a PDF document." });
      return;
    }

    setUploading(true);
    setMessage(null);
    try {
      await uploadDocument(selectedFile);
      setSelectedFile(null);
      const input = document.getElementById("document-upload") as HTMLInputElement | null;
      if (input) input.value = "";
      setMessage({ type: "success", text: "Your document was uploaded successfully." });
      await loadDocuments();
    } catch (error) {
      console.error("Document upload failed:", error);
      setMessage({ type: "error", text: "Upload failed. Please try again. If the issue continues, check the backend upload logs." });
    } finally {
      setUploading(false);
    }
  };

  const filteredDocuments = useMemo(() => documents.filter((doc) => {
    const query = searchTerm.toLowerCase().trim();
    return !query || doc.title.toLowerCase().includes(query) || (doc.category ?? "").toLowerCase().includes(query);
  }), [documents, searchTerm]);

  return (
    <div className="page-stack">
      <section className="page-intro">
        <span className="section-kicker">KNOWLEDGE BASE</span>
        <h1>Document library</h1>
        <p>Manage the policies and regulations available to PolicyLensAI.</p>
      </section>

      <section className="upload-panel">
        <div className="upload-panel-copy">
          <div className="upload-panel-icon"><UploadCloud size={22} /></div>
          <div>
            <strong>Add a policy document</strong>
            <span>Upload a PDF to make it available for search, analysis and comparison.</span>
          </div>
        </div>
        <div className="upload-controls">
          <label className="file-picker" htmlFor="document-upload">
            <FileText size={17} />
            <span>{selectedFile ? selectedFile.name : "Choose PDF"}</span>
          </label>
          <input
            id="document-upload"
            className="visually-hidden"
            type="file"
            accept=".pdf,application/pdf"
            onChange={(event) => {
              setSelectedFile(event.target.files?.[0] ?? null);
              setMessage(null);
            }}
          />
          <button type="button" className="button-primary" onClick={handleUpload} disabled={!selectedFile || uploading}>
            {uploading ? "Uploading…" : "Upload document"}
          </button>
        </div>
      </section>

      {message && <div className={`inline-alert ${message.type}`} role="status">{message.text}</div>}

      <section className="section-block">
        <div className="section-heading">
          <div>
            <span className="section-kicker">YOUR COLLECTION</span>
            <h2>All documents <span className="count-label">{documents.length}</span></h2>
          </div>
        </div>
        <div className="document-toolbar">
          <Search size={17} />
          <input
            type="search"
            placeholder="Search by document name or category…"
            value={searchTerm}
            onChange={(event) => setSearchTerm(event.target.value)}
            aria-label="Search documents"
          />
          {searchTerm && <button type="button" aria-label="Clear search" onClick={() => setSearchTerm("")}><X size={16} /></button>}
        </div>

        {loading ? (
          <div className="content-card empty-state">Loading your documents…</div>
        ) : filteredDocuments.length ? (
          <div className="documents-grid">
            {filteredDocuments.map((doc) => (
              <article key={doc.document_id} className="document-card">
                <div className="document-card-top">
                  <div className="document-file-icon"><FileText size={20} /></div>
                  <span className={`status-badge ${doc.status === "READY" ? "success" : "pending"}`}>{doc.status || "Available"}</span>
                </div>
                <h3>{doc.title}</h3>
                <p className="document-category">{doc.category || "Uncategorised"}</p>
                <div className="document-id">ID: {doc.document_id}</div>
                <div className="document-actions">
                  <button type="button" onClick={() => navigate(`/summary/${doc.document_id}`)}>Summary</button>
                  <button type="button" onClick={() => navigate("/comparison")}>Compare</button>
                  <button type="button" onClick={() => navigate(`/analysis/${doc.document_id}`)}>Analyze</button>
                </div>
              </article>
            ))}
          </div>
        ) : (
          <div className="content-card empty-state">
            <FileText size={28} />
            <strong>{searchTerm ? "No matching documents" : "No documents yet"}</strong>
            <span>{searchTerm ? "Try another search term." : "Upload your first policy PDF to start using the knowledge base."}</span>
          </div>
        )}
      </section>
    </div>
  );
}
