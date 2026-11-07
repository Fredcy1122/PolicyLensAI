import { useEffect, useState } from "react";

import { useParams } from "react-router-dom";
import ReactMarkdown
from "react-markdown";
import {
  generateDocumentSummary,
} from "../services/summaryService";

export default function Summary() {

  const { documentId } =
    useParams();

  const [summary, setSummary] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  useEffect(() => {

    if (documentId) {
      generateSummary();
    }

  }, [documentId]);

  const generateSummary =
    async () => {

      if (!documentId) {
        return;
      }

      try {

        setLoading(true);

        const result =
          await generateDocumentSummary(
            documentId
          );

        setSummary(
          result.summary
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
        📝 Document Summary
      </h1>

      <p>
        Document ID:
        {" "}
        {documentId}
      </p>

      <br />

      <button
        onClick={
          generateSummary
        }
        className="summary-button"
      >
        Generate Summary
      </button>

      {loading && (
        <p>
          Generating summary...
        </p>
      )}

      {summary && (
        <div className="summary-result">

          <h2>
            Summary
          </h2>

          <ReactMarkdown>
            {summary}
          </ReactMarkdown>

        </div>
      )}

    </div>
  );
}