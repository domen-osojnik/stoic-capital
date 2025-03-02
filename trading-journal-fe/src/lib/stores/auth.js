import { writable } from 'svelte/store';

// Check if running in the browser
const isBrowser = typeof window !== 'undefined';

// Load user from localStorage only if in the browser
const storedUser = isBrowser ? JSON.parse(localStorage.getItem('user')) || null : null;

export const authStore = writable(storedUser);

export function login(user) {
    if (isBrowser) {
        localStorage.setItem('user', JSON.stringify(user));
    }
    authStore.set(user);
}

export function logout() {
    if (isBrowser) {
        localStorage.removeItem('user');
    }
    authStore.set(null);
}