import api from "./api";

export const getAgentMetrics =
  async () => {

    const response =
      await api.get(
        "/agents/metrics"
      );

    return response.data;
  };