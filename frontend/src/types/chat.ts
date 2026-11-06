export interface Citation {
  title: string;
  page: number;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  citations?: Citation[];
  agents?: string[];
  confidence?: number;

  routing?: {
    matched_keywords: string[];
    selected_agents: string[];
  };
  collaboration?: boolean;
}