// import { api } from "./client.js";

// export const authApi = {
//   register: (payload) => api.post("/auth/register", payload).then((r) => r.data.data),
//   login: (payload) => api.post("/auth/login", payload).then((r) => r.data.data),
//   refresh: () => api.post("/auth/refresh").then((r) => r.data.data),
//   logout: () => api.post("/auth/logout").then((r) => r.data),
//   me: () => api.get("/auth/me").then((r) => r.data.data),
//   updateProfile: (payload) => api.patch("/auth/me", payload).then((r) => r.data.data),
//   changePassword: (payload) => api.post("/auth/change-password", payload).then((r) => r.data),
// };


// import { api, setAccessToken } from "./client.js";

// export const authApi = {

//   register: async (data) => {

//     const response = await api.post(
//       "/auth/register/",
//       {
//         username: data.name,
//         email: data.email,
//         password: data.password,
//       }
//     );

//     return response.data;
//   },

//   login: async (data) => {

//     const response = await api.post(
//       "/auth/login/",
//       {
//         username: data.username,
//         password: data.password,
//       }
//     );

//     if (response.data.access) {
//       setAccessToken(
//         response.data.access
//       );
//     }

//     return response.data;
//   },

//   refresh: async () => {

//     const response = await api.post(
//       "/auth/refresh/",
//       {}
//     );

//     if (response.data.access) {
//       setAccessToken(
//         response.data.access
//       );
//     }

//     return response.data;
//   },
// };

import {
  api,
  setAccessToken,
} from "./client.js";

export const authApi = {

  register: async (data) => {

    const response = await api.post(
      "/auth/register/",
      {
        username: data.name,
        email: data.email,
        password: data.password,
      }
    );

    return response.data;
  },

  login: async (data) => {

    const response = await api.post(
      "/auth/login/",
      {
        email: data.email,
        password: data.password,
      }
    );

    if (response.data.access) {

      setAccessToken(
        response.data.access
      );

      localStorage.setItem(
      "accessToken",
      response.data.access
    );
    }

    return response.data;
  },

  refresh: async () => {

    return null;
  },
};