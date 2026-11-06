import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import MainLayout from "./components/layout/MainLayout";

import Dashboard from "./pages/Dashboard";
import Assistant from "./pages/Assistant";
import Documents from "./pages/Documents";
import Comparison from "./pages/Comparison";
import Summary from "./pages/Summary";
import Evaluation from "./pages/Evaluation";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/assistant"
            element={<Assistant />}
          />

          <Route
            path="/documents"
            element={<Documents />}
          />

          <Route
            path="/comparison"
            element={<Comparison />}
          />

          <Route
            path="/summary"
            element={<Summary />}
          />

          <Route
            path="/evaluation"
            element={<Evaluation />}
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;