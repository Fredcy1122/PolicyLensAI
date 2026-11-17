import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ArrowRight, Brain, FileText, Scale, Ship, Wallet, Globe2, BookOpen, Workflow } from "lucide-react";
import { getAgentMetrics } from "../services/agentService";
import type { AgentMetrics } from "../types/agentMetrics";

const agents = [
  { name: "Legal Agent", detail: "Legislation, sections, obligations and penalties", icon: Scale, tone: "purple" },
  { name: "Customs Agent", detail: "Imports, exports, customs procedures and clearance", icon: Ship, tone: "blue" },
  { name: "Trade Agent", detail: "Trade agreements, restrictions and policy analysis", icon: Globe2, tone: "green" },
  { name: "Finance Agent", detail: "VAT, tariffs, duties and financial regulations", icon: Wallet, tone: "amber" },
  { name: "Policy Agent", detail: "General policy knowledge and document context", icon: BookOpen, tone: "slate" },
];

export default function AgentCenter() {
  const [metrics, setMetrics] = useState<AgentMetrics | null>(null);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    getAgentMetrics()
      .then(setMetrics)
      .catch((err) => {
        console.error("Unable to load agent metrics:", err);
        setError("Agent metrics are currently unavailable.");
      });
  }, []);

  const metricItems = [
    ["Total questions", metrics?.total_questions ?? "—"],
    ["Finance Agent", metrics?.finance ?? "—"],
    ["Customs Agent", metrics?.customs ?? "—"],
    ["Legal Agent", metrics?.legal ?? "—"],
  ];

  return (
    <div className="page-stack">
      <section className="page-intro">
        <span className="section-kicker">MULTI-AGENT INTELLIGENCE</span>
        <h1>Agent command center</h1>
        <p>Understand how PolicyLensAI routes policy questions to specialist agents.</p>
      </section>

      {error && <div className="inline-alert" role="status">{error}</div>}

      <section className="agent-metrics-grid">
        {metricItems.map(([label, value]) => (
          <article className="agent-metric" key={label}>
            <span>{label}</span>
            <strong>{value}</strong>
          </article>
        ))}
      </section>

      <section className="section-block">
        <div className="section-heading"><div><span className="section-kicker">SPECIALIST WORKERS</span><h2>Agent capabilities</h2></div></div>
        <div className="agent-card-grid">
          {agents.map((agent) => {
            const Icon = agent.icon;
            return (
              <article className="agent-card" key={agent.name}>
                <div className={`agent-icon ${agent.tone}`}><Icon size={21} /></div>
                <strong>{agent.name}</strong>
                <p>{agent.detail}</p>
                <span className="agent-tag">Available in routing</span>
              </article>
            );
          })}
        </div>
      </section>

      <section className="section-block">
        <div className="section-heading"><div><span className="section-kicker">HOW IT WORKS</span><h2>Question routing flow</h2></div></div>
        <div className="content-card routing-flow">
          <div className="routing-step"><span>01</span><Brain size={20} /><strong>User question</strong><small>Policy query submitted</small></div>
          <ArrowRight className="routing-arrow" size={18} />
          <div className="routing-step"><span>02</span><Workflow size={20} /><strong>Router agent</strong><small>Identifies relevant expertise</small></div>
          <ArrowRight className="routing-arrow" size={18} />
          <div className="routing-step"><span>03</span><FileText size={20} /><strong>Specialist agents</strong><small>Retrieve and analyse context</small></div>
          <ArrowRight className="routing-arrow" size={18} />
          <div className="routing-step"><span>04</span><BookOpen size={20} /><strong>Final answer</strong><small>Reasoned response with sources</small></div>
        </div>
      </section>

      <section className="agent-cta">
        <div><strong>Ready to ask a policy question?</strong><span>Let the routing layer select the most relevant specialist agents.</span></div>
        <button type="button" className="button-primary" onClick={() => navigate("/assistant")}>Open assistant <ArrowRight size={16} /></button>
      </section>
    </div>
  );
}
