import { authStore } from '$lib/stores/auth';
import { goto } from '$app/navigation';
import { onMount } from 'svelte';

/**
 * Protect a route by checking if the user is authenticated.
 * Redirects to /login if not authenticated.
 */
export function protectPage() {
    onMount(() => {
        authStore.subscribe(user => {
            if (!user) {
                goto('/login'); // Redirect to login page
            }
        });
    });
}