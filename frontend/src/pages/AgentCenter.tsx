export default function AgentCenter() {
  return (
    <div>
      <h1>
        🧠 Agent Command Center
      </h1>

      <p>
        View agent routing and
        contributions.
      </p>

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
          <h3>Agent Architecture</h3>

          <pre>
Question
↓
Router Agent
↓
Legal Agent
Customs Agent
Trade Agent
Finance Agent
↓
Synthesis Agent
↓
Final Answer
          </pre>
        </div>
      </div>

      <div className="dashboard-card">
        <h3>Current Capabilities</h3>

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
            ✅ Synthesis Layer
          </li>
        </ul>
      </div>
    </div>
  );
}