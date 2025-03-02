<script>
    import { authStore, logout } from '$lib/stores/auth';

    let user;
    authStore.subscribe(value => user = value);
</script>

<nav>
    <a href="/">Home</a>
    {#if user}
        <a href="/dashboard">Dashboard</a>
        <button on:click={logout}>Logout</button>
    {:else}
        <a href="/login">Login</a>
        <a href="/register">Register</a>
    {/if}
</nav>

<slot />
