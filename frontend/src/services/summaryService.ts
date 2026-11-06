import api from "./api";

export const generateSummary =
  async (
    title: string,
    content: string
  ) => {
    const response =
      await api.post(
        "/summary",
        {
          title,
          content,
        }
      );

    return response.data;
  };