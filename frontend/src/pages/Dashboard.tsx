import { useEffect, useState } from "react";
import { getDashboardStats } from "../services/dashboardService";
import type { DashboardStats } from "../types/dashboard";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const coverageData = [
  {
    name: "Customs",
    score: 92,
  },
  {
    name: "Trade",
    score: 80,
  },
  {
    name: "Import",
    score: 87,
  },
  {
    name: "Export",
    score: 75,
  },
  {
    name: "Compliance",
    score: 90,
  },
];

export default function Dashboard() {
  const [stats, setStats] =
    useState<DashboardStats | null>(null);
  const loadStats = async () => {
    try {
      const data =
        await getDashboardStats();
      console.log("Dashboard Stats:", data);
      setStats(data);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    loadStats();
  }, []);

  return (
    <div>
      <div
        style={{
          marginBottom: "30px",
        }}
      >
        <h1>
          🇳🇬 PolicyLenAI Command Center
        </h1>

       
        <p>
          Nigerian Policy Intelligence Platform
        </p>
      </div>

      <div className="metrics-grid">
        <div className="metric-card">
          <h3>Documents</h3>
          <h2>{stats?.documents ?? 0}</h2>
        </div>

        <div className="metric-card">
          <h3>Chunks</h3>
          <h2>{stats?.chunks ?? 0}</h2>
        </div>

        <div className="metric-card">
          <h3>Queries</h3>
          <h2>{stats?.queries ?? 0}</h2>
        </div>

        <div className="metric-card">
          <h3>Accuracy</h3>
          <h2>{stats?.accuracy ?? 0}%</h2>
        </div>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-card">
          <h3>Knowledge Coverage</h3>

          <ResponsiveContainer
            width="100%"
            height={300}
          >
            <BarChart data={coverageData}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />

              <Bar
                dataKey="score"
                fill="#008751"
              />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="dashboard-card">
          <h3>System Health</h3>

          <ul>
            <li>
              ✅ Backend Online
            </li>

            <li>
              ✅ Vector Store Active
            </li>

            <li>
              ✅ Retrieval Working
            </li>

            <li>
              ✅ Citation Engine Active
            </li>
          </ul>
        </div>
      </div>

      <div className="dashboard-card">
        <h3>Recent Queries</h3>

        <ul>
          <li>
            What are the penalties for false declaration?
          </li>

          <li>
            Explain Section 143 of NCSA 2023.
          </li>

          <li>
            Compare CEMA 2004 with NCSA 2023.
          </li>
        </ul>
      </div>
    </div>
  );
}