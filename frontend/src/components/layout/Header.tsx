import {
  Bell,
  Search,
} from "lucide-react";

export default function Header() {
  return (
    <header className="header">
      <div>
        <h3>
          PolicyLenAI Command Center
        </h3>
      </div>

      <div className="header-actions">
        <Search size={18} />

        <Bell size={18} />

        <span className="status">
          ● System Online
        </span>
      </div>
    </header>
  );
}