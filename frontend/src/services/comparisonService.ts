import api from "./api";

export const compareDocuments =
  async (
    documentA: string,
    documentB: string
  ) => {
    const response =
      await api.post(
        "/comparison",
        {
          document_a: documentA,
          document_b: documentB,
        }
      );

    return response.data;
  };