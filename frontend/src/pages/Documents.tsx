import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getDocuments,
  uploadDocument,
} from "../services/documentService";

import type { Document } from "../types/document";

export default function Documents() {
  const [documents, setDocuments] =
    useState<Document[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [selectedFile, setSelectedFile] =
    useState<File | null>(null);

  const [searchTerm, setSearchTerm] =
    useState("");

  const navigate =
    useNavigate();

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

  const handleUpload =
    async () => {
      if (!selectedFile) {
        return;
      }

      try {
        await uploadDocument(
          selectedFile
        );

        await loadDocuments();

        setSelectedFile(
          null
        );
      } catch (error) {
        console.error(error);
      }
    };

  const filteredDocuments =
    documents.filter((doc) =>
      doc.title
        .toLowerCase()
        .includes(
          searchTerm.toLowerCase()
        )
    );

  return (
    <div>
      <h1>
        📚 Document Library
      </h1>

      <p>
        Browse ingested policies and regulations.
      </p>

      <div
        style={{
          marginTop: "20px",
          marginBottom: "20px",
        }}
      >
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => {
            const file =
              e.target.files?.[0];

            if (file) {
              setSelectedFile(file);
            }
          }}
        />

        <button
          onClick={handleUpload}
          className="summary-button"
          style={{
            marginLeft: "10px",
          }}
        >
          Upload Document
        </button>
      </div>

      <input
        type="text"
        placeholder="Search documents..."
        value={searchTerm}
        onChange={(e) =>
          setSearchTerm(
            e.target.value
          )
        }
        className="search-input"
      />

      <br />
      <br />

      {loading ? (
        <p>
          Loading documents...
        </p>
      ) : (
        <div className="documents-grid">
          {filteredDocuments.map(
            (doc) => (
              <div
                key={doc.document_id}
                className="document-card"
              >
                <h3>
                  {doc.title}
                </h3>

                <p>
                  Category: {doc.category}
                </p>

                <p>
                  Status{" "}
                  <span
                    className={`status-badge ${
                      doc.status ===
                      "READY"
                        ? "success"
                        : "pending"
                    }`}
                  >
                    {doc.status}
                  </span>
                </p>

                <small>
                  {doc.document_id}
                </small>

                <div
                  style={{
                    marginTop:
                      "10px",
                    display:
                      "flex",
                    gap: "10px",
                  }}
                >
                  <button
                    className="summary-button"
                    onClick={() =>
                      navigate(
                        `/summary/${doc.document_id}`
                      )
                    }
                  >
                    Summary
                  </button>

                  <button
                    className="summary-button"
                    onClick={() =>
                      navigate(
                        "/comparison"
                      )
                    }
                  >
                    Compare
                  </button>

                  <button
                    className="summary-button"
                    onClick={() =>
                      navigate(
                        `/analysis/${doc.document_id}`
                      )
                    }
                  >
                    Analyze
                  </button>
                </div>
              </div>
            )
          )}
        </div>
      )}
    </div>
  );
}