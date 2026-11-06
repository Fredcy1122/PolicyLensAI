import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  MessageSquare,
  Files,
  Scale,
  FileText,
  BarChart3,
  Brain,
} from "lucide-react";

const menuItems = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    name: "Assistant",
    path: "/assistant",
    icon: MessageSquare,
  },
  {
    name: "Agent Center",
    path: "/agents",
    icon: Brain,
  },
  {
    name: "Documents",
    path: "/documents",
    icon: Files,
  },
  {
    name: "Compare Policies",
    path: "/comparison",
    icon: Scale,
  },
  {
    name: "Summaries",
    path: "/summary",
    icon: FileText,
  },
  {
    name: "Evaluation",
    path: "/evaluation",
    icon: BarChart3,
  },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="logo-section">
        <h2>🇳🇬 PolicyLenAI</h2>
        <p>Policy Intelligence</p>
      </div>

      <nav>
        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                isActive
                  ? "nav-link active"
                  : "nav-link"
              }
            >
              <Icon size={18} />
              <span>{item.name}</span>
            </NavLink>
          );
        })}
      </nav>
    </aside>
  );
}