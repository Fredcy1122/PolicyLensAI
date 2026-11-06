import { useState } from "react";
import { generateSummary } from "../services/summaryService";

export default function Summary() {
  const [title, setTitle] =
    useState("");

  const [content, setContent] =
    useState("");

  const [summary, setSummary] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const handleGenerate =
    async () => {
      try {
        setLoading(true);

        const result =
          await generateSummary(
            title,
            content
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
        📝 Policy Summary
      </h1>

      <input
        type="text"
        placeholder="Document Title"
        value={title}
        onChange={(e) =>
          setTitle(
            e.target.value
          )
        }
        className="search-input"
      />

      <textarea
        rows={10}
        placeholder="Paste document content..."
        value={content}
        onChange={(e) =>
          setContent(
            e.target.value
          )
        }
        className="summary-textarea"
      />

      <br />
      <br />

      <button
        onClick={
          handleGenerate
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
          <h2>Summary</h2>

          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}