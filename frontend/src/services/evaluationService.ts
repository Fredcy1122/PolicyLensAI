import api from "./api";

export const getEvaluation =
  async () => {
    const response =
      await api.get(
        "/evaluation"
      );

    return response.data;
  };