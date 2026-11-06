export interface Citation {
  title: string;
  page: number;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  confidence?: string;
  citations?: Citation[];
}