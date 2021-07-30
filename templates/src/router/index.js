import { createRouter, createWebHistory } from 'vue-router';
import authRoutes from './auth';
import Home from '../views/Home.vue';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	...authRoutes,
];

const router = createRouter({
	base: '/{{ spa_name }}/',
	history: createWebHistory(),
	routes,
});

export default router;
