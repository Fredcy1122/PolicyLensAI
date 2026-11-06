import { useEffect, useState } from "react";
import { getDocuments } from "../services/documentService";
import type { Document } from "../types/document";

export default function Documents() {
  const [documents, setDocuments] =
    useState<Document[]>([]);

  const [loading, setLoading] =
    useState(true);
  const [searchTerm, setSearchTerm] =
    useState("");

  useEffect(() => {
    loadDocuments();
  }, []);

  const loadDocuments = async () => {
    try {
      const data =
        await getDocuments();

      setDocuments(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>📚 Document Library</h1>

      <p>
        Browse ingested policies and regulations.
      </p>

      <br />

      {loading ? (
        <p>Loading documents...</p>
      ) : (
        <div className="documents-grid">
          {documents.map((doc) => (
            <div
              key={doc.document_id}
              className="document-card"
            >
              <h3>{doc.title}</h3>

              <p>
                Category:
                {" "}
                {doc.category}
              </p>

              <p>
                Status:
                {" "}
                {doc.status}
              </p>

              <small>
                {doc.document_id}
              </small>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}