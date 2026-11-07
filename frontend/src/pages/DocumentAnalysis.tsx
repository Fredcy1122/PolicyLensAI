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

          <ReactMarkdown>
            {analysis}
          </ReactMarkdown>

        </div>

      )}

    </div>
  );
}