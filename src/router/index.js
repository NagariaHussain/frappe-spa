import { createRouter, createWebHistory } from "vue-router";
import authRoutes from "./auth";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  ...authRoutes,
];

// Add this to your hooks.py file
// website_route_rules = [
// {"from_route": "/dashboard/<path:app_path>", "to_route": "dashboard"},
// ]
const router = createRouter({
  base: "/dashboard/",
  history: createWebHistory(),
  routes,
});

export default router;
