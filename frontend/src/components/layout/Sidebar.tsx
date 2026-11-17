import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  MessageSquare,
  Files,
  Scale,
  FileText,
  BarChart3,
  Brain,
  ShieldCheck,
} from "lucide-react";

const menuItems = [
  { name: "Dashboard", path: "/", icon: LayoutDashboard, end: true },
  { name: "Assistant", path: "/assistant", icon: MessageSquare },
  { name: "Agent Center", path: "/agents", icon: Brain },
  { name: "Documents", path: "/documents", icon: Files },
  { name: "Compare Policies", path: "/comparison", icon: Scale },
  { name: "Summaries", path: "/summary", icon: FileText },
  { name: "Evaluation", path: "/evaluation", icon: BarChart3 },
];

type SidebarProps = {
  isOpen: boolean;
  onNavigate: () => void;
};

export default function Sidebar({ isOpen, onNavigate }: SidebarProps) {
  return (
    <aside className={`sidebar ${isOpen ? "sidebar-open" : ""}`}>
      <div className="brand">
        <div className="brand-mark" aria-hidden="true">🇳🇬</div>
        <div className="brand-copy">
          <strong>PolicyLensAI</strong>
          <span>Policy Intelligence</span>
        </div>
      </div>

      <div className="nav-caption">WORKSPACE</div>
      <nav className="sidebar-nav" aria-label="Main navigation">
        {menuItems.map((item) => {
          const Icon = item.icon;
          return (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.end}
              onClick={onNavigate}
              className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}
            >
              <Icon size={19} strokeWidth={1.9} />
              <span>{item.name}</span>
            </NavLink>
          );
        })}
      </nav>

      <div className="sidebar-bottom">
        <div className="sidebar-security">
          <ShieldCheck size={19} />
          <div>
            <strong>Policy workspace</strong>
            <span>Regulatory intelligence</span>
          </div>
        </div>
        <span className="sidebar-version">NIGERIA · POLICY INTELLIGENCE</span>
      </div>
    </aside>
  );
}
