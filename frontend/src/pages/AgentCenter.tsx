import { useEffect, useState } from "react";

import { getAgentMetrics } from "../services/agentService";

import type { AgentMetrics } from "../types/agentMetrics";

export default function AgentCenter() {
  const [metrics, setMetrics] =
    useState<AgentMetrics | null>(
      null
    );

  useEffect(() => {
    loadMetrics();
  }, []);

  const loadMetrics =
    async () => {
      try {
        const data =
          await getAgentMetrics();

        setMetrics(data);
      } catch (error) {
        console.error(error);
      }
    };

  return (
    <div>
      <h1>
        🧠 Agent Command Center
      </h1>

      <p>
        View agent routing and
        contributions.
      </p>

      <div className="metrics-grid">

        <div className="metric-card">
          <h3>Total Questions</h3>

          <h2>
            {metrics?.total_questions ?? 0}
          </h2>
        </div>

        <div className="metric-card">
          <h3>Finance Agent</h3>

          <h2>
            {metrics?.finance ?? 0}
          </h2>
        </div>

        <div className="metric-card">
          <h3>Customs Agent</h3>

          <h2>
            {metrics?.customs ?? 0}
          </h2>
        </div>

        <div className="metric-card">
          <h3>Legal Agent</h3>

          <h2>
            {metrics?.legal ?? 0}
          </h2>
        </div>

      </div>

      <div className="dashboard-grid">

        <div className="dashboard-card">

          <h3>
            Agent Capabilities
          </h3>

          <ul>

            <li>
              ⚖️ Legal Agent
              (Acts, Sections,
              Penalties)
            </li>

            <li>
              🚢 Customs Agent
              (Imports, Exports,
              Clearance)
            </li>

            <li>
              🌍 Trade Agent
              (Trade Agreements,
              Policy Analysis)
            </li>

            <li>
              💰 Finance Agent
              (VAT, Tariffs,
              Duties)
            </li>

            <li>
              📘 Policy Agent
              (General Knowledge)
            </li>

          </ul>

        </div>

        <div className="dashboard-card">

          <h3>
            Agent Architecture
          </h3>

          <pre>
{`Question
↓
Router Agent
↓
Legal Agent
Customs Agent
Trade Agent
Finance Agent
↓
Reasoning Agent
↓
Final Answer`}
          </pre>

        </div>

      </div>

      <div className="dashboard-card">

        <h3>
          Current Capabilities
        </h3>

        <ul>

          <li>
            ✅ Multi-Agent Routing
          </li>

          <li>
            ✅ Agent Scoring
          </li>

          <li>
            ✅ Finance Agent
          </li>

          <li>
            ✅ Customs Agent
          </li>

          <li>
            ✅ Legal Agent
          </li>

          <li>
            ✅ Trade Agent
          </li>

          <li>
            ✅ Persistent Memory
          </li>

          <li>
            ✅ Reasoning Layer
          </li>

        </ul>

      </div>

    </div>
  );
}