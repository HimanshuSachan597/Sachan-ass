// import { api } from "./client.js";

// export const usersApi = {
//   list: (params) => api.get("/users", { params }).then((r) => r.data.data.users),
//   get: (id) => api.get(`/users/${id}`).then((r) => r.data.data.user),
//   updateRole: (id, role) =>
//     api.patch(`/users/${id}/role`, { role }).then((r) => r.data.data.user),
//   setActive: (id, isActive) =>
//     api.patch(`/users/${id}/active`, { isActive }).then((r) => r.data.data.user),
//   remove: (id) => api.delete(`/users/${id}`).then((r) => r.data),
// };

import { api } from "./client.js";

export const usersApi = {
  list: (params) =>
    api
      .get("/auth/users/", { params })
      .then((r) => r.data),

  get: (id) =>
    api
      .get(`/auth/users/${id}/`)
      .then((r) => r.data),

  remove: (id) =>
    api
      .delete(`/auth/users/${id}/`)
      .then((r) => r.data),

  updateRole: (id, role) =>
    api
      .patch(`/auth/users/${id}/`, {
        role,
      })
      .then((r) => r.data),

  setActive: (id, isActive) =>
    api
      .patch(`/auth/users/${id}/`, {
        is_active: isActive,
      })
      .then((r) => r.data),
};