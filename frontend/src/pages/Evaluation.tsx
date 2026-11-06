import { useEffect, useState } from "react";

import {
  getEvaluation,
} from "../services/evaluationService";

import type {
  EvaluationMetrics,
} from "../types/evaluation";

export default function Evaluation() {
  const [metrics, setMetrics] =
    useState<EvaluationMetrics | null>(
      null
    );

  useEffect(() => {
    loadMetrics();
  }, []);

  const loadMetrics =
    async () => {
      try {
        const data =
          await getEvaluation();

        setMetrics(data);
      } catch (error) {
        console.error(error);
      }
    };

  return (
    <div>
      <h1>
        📈 AI Evaluation
      </h1>

      <p>
        PolicyLenAI
        Performance Metrics
      </p>

      <br />

      <div className="metrics-grid">
        <div className="metric-card">
          <h3>
            Retrieval Accuracy
          </h3>

          <h2>
            {
              metrics?.retrieval_accuracy ??
              0
            }
            %
          </h2>
        </div>

        <div className="metric-card">
          <h3>
            Abstention Accuracy
          </h3>

          <h2>
            {
              metrics?.abstention_accuracy ??
              0
            }
            %
          </h2>
        </div>

        <div className="metric-card">
          <h3>
            Average Latency
          </h3>

          <h2>
            {
              metrics?.average_latency?.toFixed(
                2
              ) ?? "0"
            }
            s
          </h2>
        </div>

        <div className="metric-card">
          <h3>
            Questions Evaluated
          </h3>

          <h2>
            {
              metrics?.total_questions ??
              0
            }
          </h2>
        </div>
      </div>
    </div>
  );
}