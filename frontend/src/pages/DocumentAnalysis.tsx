import {
  useEffect,
  useState,
} from "react";
import ReactMarkdown
from "react-markdown";
import {
  useParams,
} from "react-router-dom";

import {
  analyzeDocument,
} from "../services/documentService";

export default function
DocumentAnalysis() {

  const { documentId } =
    useParams();

  const [analysis,
  setAnalysis] =
    useState("");

  const [documentType,
  setDocumentType] =
    useState("");
  const [contributors,
  setContributors] =
    useState(0);

  const [agents,
  setAgents] =
    useState<string[]>([]);

  const [loading,
  setLoading] =
    useState(false);

  useEffect(() => {

    if (documentId) {
      loadAnalysis();
    }

  }, [documentId]);

  const loadAnalysis =
    async () => {

      try {

        setLoading(true);

        const result =
          await analyzeDocument(
            documentId!
          );

        setAnalysis(
          result.analysis
        );

        setContributors(
          result.contributors || 0
        );

        setDocumentType(
          result.document_type
        );

        setAgents(
          result.agents || []
        );

      } finally {

        setLoading(false);

      }
    };

  return (
    <div>

      <h1>
        📘 Document Analysis
      </h1>

      <p>
        Document:
        {" "}
        {documentId}
      </p>

      {loading &&
        <p>
          Generating analysis...
        </p>
      }

      {analysis && (

        <div
          className="summary-result"
        >
          {documentType && (
            <div className="citation-box">
              <strong>
                Document Type:
              </strong>
              {" "}
              {documentType}
            </div>
          )}
          {agents.length > 0 && (
            <div className="citation-box">
              <strong>
                Selected Agents:
              </strong>
              {" "}
              {agents.join(", ")}
            </div>
          )}

          {contributors > 0 && (
            <div className="citation-box">
              <strong>
                Contributing Agents:
              </strong>
              {" "}
              {contributors}
            </div>
          )}
          <ReactMarkdown>
            {analysis}
          </ReactMarkdown>

        </div>

      )}

    </div>
  );
}