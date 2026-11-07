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

export const generateDocumentSummary =
  async (
    documentId: string
  ) => {

    const response =
      await api.get(
        `/summary/document/${documentId}`
      );

    return response.data;
  };