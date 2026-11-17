import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  ArrowRight,
  BarChart3,
  FileText,
  Files,
  MessageSquare,
  Scale,
  Sparkles,
  UploadCloud,
} from "lucide-react";
import { getDashboardStats } from "../services/dashboardService";
import { getDocuments } from "../services/documentService";
import type { DashboardStats } from "../types/dashboard";
import type { Document } from "../types/document";

export default function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    let active = true;
    const loadDashboard = async () => {
      try {
        const [statsResult, documentsResult] = await Promise.all([
          getDashboardStats(),
          getDocuments(),
        ]);
        if (active) {
          setStats(statsResult);
          setDocuments(Array.isArray(documentsResult) ? documentsResult : []);
          setLoadError("");
        }
      } catch (error) {
        console.error("Unable to load dashboard data:", error);
        if (active) setLoadError("Some dashboard information could not be loaded. Please refresh to try again.");
      } finally {
        if (active) setLoading(false);
      }
    };
    loadDashboard();
    return () => { active = false; };
  }, []);

  const metrics = [
    { label: "Documents", value: stats?.documents ?? "—", icon: Files, tone: "green", note: "In your library" },
    { label: "Indexed chunks", value: stats?.chunks ?? "—", icon: FileText, tone: "blue", note: "Available for retrieval" },
    { label: "Questions", value: stats?.queries ?? "—", icon: MessageSquare, tone: "purple", note: "Questions processed" },
    { label: "Accuracy", value: stats ? `${stats.accuracy}%` : "—", icon: BarChart3, tone: "amber", note: "Reported system metric" },
  ];

  const actions = [
    { title: "Upload a document", description: "Add a policy or regulation to your library", icon: UploadCloud, action: () => navigate("/documents"), primary: true },
    { title: "Ask a question", description: "Get answers grounded in your documents", icon: MessageSquare, action: () => navigate("/assistant") },
    { title: "Compare policies", description: "Identify differences between two documents", icon: Scale, action: () => navigate("/comparison") },
    { title: "Generate a summary", description: "Review an existing document in brief", icon: Sparkles, action: () => navigate("/summary") },
  ];

  return (
    <div className="page-stack">
      <section className="welcome-panel">
        <div>
          <span className="section-kicker">YOUR POLICY WORKSPACE</span>
          <h1>Good to have you back.</h1>
          <p>Explore Nigerian legislation, understand regulatory changes and get answers from your policy documents.</p>
        </div>
        <div className="welcome-emblem" aria-hidden="true">🇳🇬</div>
      </section>

      {loadError && <div className="inline-alert" role="status">{loadError}</div>}

      <section className="metrics-grid" aria-label="Workspace metrics">
        {metrics.map((metric) => {
          const Icon = metric.icon;
          return (
            <article className="metric-card" key={metric.label}>
              <div className={`metric-icon ${metric.tone}`}><Icon size={20} /></div>
              <div className="metric-copy">
                <span>{metric.label}</span>
                <strong>{loading ? "…" : metric.value}</strong>
                <small>{metric.note}</small>
              </div>
            </article>
          );
        })}
      </section>

      <section className="section-block">
        <div className="section-heading">
          <div>
            <span className="section-kicker">GET THINGS DONE</span>
            <h2>Quick actions</h2>
          </div>
        </div>
        <div className="action-grid">
          {actions.map((item) => {
            const Icon = item.icon;
            return (
              <button
                type="button"
                key={item.title}
                className={`action-card ${item.primary ? "action-card-primary" : ""}`}
                onClick={item.action}
              >
                <span className="action-icon"><Icon size={21} /></span>
                <span className="action-text">
                  <strong>{item.title}</strong>
                  <small>{item.description}</small>
                </span>
                <ArrowRight className="action-arrow" size={18} />
              </button>
            );
          })}
        </div>
      </section>

      <section className="section-block">
        <div className="section-heading">
          <div>
            <span className="section-kicker">YOUR LIBRARY</span>
            <h2>Recently available documents</h2>
          </div>
          <button type="button" className="text-action" onClick={() => navigate("/documents")}>
            View all documents <ArrowRight size={16} />
          </button>
        </div>
        <div className="content-card">
          {loading ? (
            <div className="empty-state">Loading your documents…</div>
          ) : documents.length ? (
            <div className="recent-document-list">
              {documents.slice(0, 5).map((document) => (
                <div className="recent-document" key={document.document_id}>
                  <div className="document-file-icon"><FileText size={19} /></div>
                  <div className="recent-document-copy">
                    <strong>{document.title}</strong>
                    <span>{document.category || "Uncategorised policy"}</span>
                  </div>
                  <span className={`status-badge ${document.status === "READY" ? "success" : "pending"}`}>
                    {document.status || "Available"}
                  </span>
                  <button
                    type="button"
                    className="row-action"
                    aria-label={`Open analysis for ${document.title}`}
                    onClick={() => navigate(`/analysis/${document.document_id}`)}
                  >
                    <ArrowRight size={17} />
                  </button>
                </div>
              ))}
            </div>
          ) : (
            <div className="empty-state">
              <Files size={28} />
              <strong>Your document library is ready</strong>
              <span>Upload a policy document to start building your searchable knowledge base.</span>
              <button type="button" className="button-primary" onClick={() => navigate("/documents")}>Upload first document</button>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
