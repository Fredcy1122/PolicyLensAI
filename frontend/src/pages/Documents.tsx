import { useEffect, useState } from "react";
import { getDocuments, uploadDocument } from "../services/documentService";
import type { Document } from "../types/document";

export default function Documents() {
  const [documents, setDocuments] =
    useState<Document[]>([]);

  const [loading, setLoading] =
    useState(true);
  const [selectedFile, setSelectedFile] =
    useState<File | null>(
      null
    );
  const [searchTerm, setSearchTerm] =
    useState("");
  const filteredDocuments =
    documents.filter((doc) =>
      doc.title
        .toLowerCase()
        .includes(
          searchTerm.toLowerCase()
        )
    );
  useEffect(() => {
    loadDocuments();
    const handleUpload =
      async () => {

        if (!selectedFile)
          return;

        try {

          await uploadDocument(
            selectedFile
          );

          loadDocuments();

          setSelectedFile(
            null
          );

        } catch (error) {

          console.error(error);

        }
      };
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
              setSelectedFile(
                file
              );
            }

          }}
        />

        <button
          onClick={
            handleUpload
          }
          className="summary-button"
          style={{
            marginLeft: "10px"
          }}
        >
          Upload Document
        </button>

      </div>

      <br />

      <input
        type="text"
        placeholder="Search documents..."
        value={searchTerm}
        onChange={(e) =>
          setSearchTerm(e.target.value)
        }
  className="search-input"
/>

      {loading ? (
        <p>Loading documents...</p>
      ) : (
        <div className="documents-grid">
          {filteredDocuments.map((doc) => (
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
                <span
                  className={`status-badge ${
                    doc.status === "READY"
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
            </div>
          ))}
        </div>
      )}
    </div>
  );
}