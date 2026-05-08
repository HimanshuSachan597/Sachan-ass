import { api } from "./client.js";

export const dashboardApi = {

  stats: async () => {

    const response = await api.get(
      "/dashboard/stats"
    );

    return response.data;
  },
};