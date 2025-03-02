<script>
    import { authStore } from '$lib/stores/auth';
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    
    let user;
    // 🚀 Ensure the user is authenticated before accessing the dashboard
    onMount(() => {
        const unsubscribe = authStore.subscribe(value => {
            user = value;
            if (!user) {
                goto('/login');  // Redirect if not logged in
            }
        });

        return () => unsubscribe();  // ✅ Fix: Properly unsubscribe from store
    });

</script>
<nav>
    <a href="/dashboard/trade-instruments">Trade instruments</a>
</nav>
<slot />
