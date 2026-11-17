import { useState, type FormEvent } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Bell, Menu, Search, X } from "lucide-react";

type HeaderProps = {
  onMenuClick: () => void;
};

const pageTitles: Record<string, string> = {
  "/": "Dashboard",
  "/assistant": "Policy Assistant",
  "/agents": "Agent Center",
  "/documents": "Document Library",
  "/comparison": "Policy Comparison",
  "/summary": "Document Summaries",
  "/evaluation": "AI Evaluation",
};

export default function Header({ onMenuClick }: HeaderProps) {
  const [searchOpen, setSearchOpen] = useState(false);
  const [notificationsOpen, setNotificationsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const location = useLocation();
  const navigate = useNavigate();
  const pageTitle = pageTitles[location.pathname] ?? "Policy Intelligence";

  const handleSearch = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const query = searchTerm.trim();
    if (!query) return;
    navigate(`/documents?search=${encodeURIComponent(query)}`);
    setSearchOpen(false);
  };

  return (
    <header className="header">
      <div className="header-leading">
        <button
          type="button"
          className="icon-button mobile-menu-button"
          aria-label="Open navigation menu"
          onClick={onMenuClick}
        >
          <Menu size={20} />
        </button>
        <div>
          <span className="header-eyebrow">POLICYLENS AI WORKSPACE</span>
          <h2>{pageTitle}</h2>
        </div>
      </div>

      <div className="header-actions">
        {searchOpen && (
          <form className="global-search" onSubmit={handleSearch}>
            <Search size={17} />
            <input
              autoFocus
              aria-label="Search documents"
              placeholder="Search documents..."
              value={searchTerm}
              onChange={(event) => setSearchTerm(event.target.value)}
            />
            <button
              type="button"
              className="search-close"
              aria-label="Close search"
              onClick={() => {
                setSearchOpen(false);
                setSearchTerm("");
              }}
            >
              <X size={16} />
            </button>
          </form>
        )}
        <button
          type="button"
          className="icon-button"
          aria-label="Search documents"
          onClick={() => setSearchOpen((open) => !open)}
        >
          <Search size={19} />
        </button>
        <div className="notification-wrap">
          <button
            type="button"
            className="icon-button"
            aria-label="Notifications"
            aria-expanded={notificationsOpen}
            onClick={() => setNotificationsOpen((open) => !open)}
          >
            <Bell size={19} />
          </button>
          {notificationsOpen && (
            <div className="notification-popover">
              <strong>Notifications</strong>
              <p>You’re all caught up. New document and processing updates will appear here.</p>
            </div>
          )}
        </div>
        <div className="system-status">
          <span className="status-dot" />
          <span>System Online</span>
        </div>
      </div>
    </header>
  );
}
