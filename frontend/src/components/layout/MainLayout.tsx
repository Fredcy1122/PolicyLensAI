import { useState } from "react";
import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";
import Header from "./Header";

export default function MainLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="app-shell">
      <Sidebar
        isOpen={sidebarOpen}
        onNavigate={() => setSidebarOpen(false)}
      />
      {sidebarOpen && (
        <button
          type="button"
          className="sidebar-backdrop"
          aria-label="Close navigation menu"
          onClick={() => setSidebarOpen(false)}
        />
      )}
      <div className="main-area">
        <Header onMenuClick={() => setSidebarOpen((open) => !open)} />
        <main className="content">
          <Outlet />
        </main>
        <footer className="app-footer">
          <span>PolicyLensAI · Nigerian Policy Intelligence</span>
          <span>Built for informed regulatory decisions</span>
        </footer>
      </div>
    </div>
  );
}
