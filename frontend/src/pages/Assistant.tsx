import { useState } from "react";
import { askQuestion } from "../services/chatService";
import type { ChatMessage } from "../types/chat";

export default function Assistant() {
  const [question, setQuestion] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [messages, setMessages] =
    useState<ChatMessage[]>([]);

  const handleAsk = async () => {
    if (!question.trim()) return;

    const userMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: question,
    };

    setMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    const currentQuestion = question;

    setQuestion("");

    try {
      setLoading(true);

      const result =
        await askQuestion(
          currentQuestion
        );

      const aiMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: result.answer,
        confidence:
          result.confidence,
        citations:
          result.citations || [],
      };

      setMessages((prev) => [
        ...prev,
        aiMessage,
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content:
            "Unable to reach PolicyLenAI backend.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div className="assistant-header">
        <h1>
          🇳🇬 PolicyLenAI Assistant
        </h1>

        <p>
          Ask questions about policies,
          regulations and customs
          legislation.
        </p>
      </div>

      <div className="chat-container">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`message ${msg.role}`}
          >
            <div className="message-content">
              {msg.content}
            </div>

            {msg.role ===
              "assistant" &&
              msg.confidence && (
                <div className="confidence-badge">
                  Confidence:
                  {" "}
                  {msg.confidence}
                </div>
              )}

            {msg.role ===
              "assistant" &&
              msg.citations &&
              msg.citations.length >
                0 && (
                <div className="citation-box">
                  <strong>
                    Sources:
                  </strong>

                  {msg.citations.map(
                    (citation, index) => (
                      <div
                        key={index}
                      >
                        ✅
                        {" "}
                        {
                          citation.title
                        }
                        {" "}
                        (Page{" "}
                        {
                          citation.page
                        }
                        )
                      </div>
                    )
                  )}
                </div>
              )}
          </div>
        ))}

        {loading && (
          <div className="thinking">
            PolicyLenAI is thinking...
          </div>
        )}
      </div>

      <div className="chat-input">
        <textarea
          rows={4}
          placeholder="Ask a policy question..."
          value={question}
          onChange={(e) =>
            setQuestion(
              e.target.value
            )
          }
        />

        <button
          onClick={handleAsk}
        >
          Ask
        </button>
      </div>
    </div>
  );
}