import { Navigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext.jsx";

export default function RoleGate({
  children,
  roles = [],
  redirectTo = "/dashboard",
}) {
  const { user } = useAuth();

  const hasRole = (...allowedRoles) =>
    user && allowedRoles.includes(user.role);

  if (!hasRole(...roles)) {
    return <Navigate to={redirectTo} replace />;
  }

  return children;
}