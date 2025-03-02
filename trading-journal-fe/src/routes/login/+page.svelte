<script>
    import { loginUser } from '$lib/api';
    import { login } from '$lib/stores/auth';
    import { goto } from '$app/navigation';
    import { authStore } from '$lib/stores/auth';
    
    let username = '';
    let password = '';
    let message = '';

    async function handleLogin(e) {
        e.preventDefault();
        const data = { username, password };

        try {
            const result = await loginUser(data);
            if (result.access) {
                login({ username, token: result.access });
                goto('/dashboard'); // Redirect to dashboard after login
            } else {
                message = 'Invalid credentials';
            }
        } catch (error) {
            message = 'Login failed';
        }
    }

    authStore.subscribe(user => {
        if (user) {
            goto('/dashboard'); // Already logged in? Go to dashboard.
        }
    });
</script>

<form on:submit|preventDefault={handleLogin}>
    <input type="text" bind:value={username} placeholder="Username" required />
    <input type="password" bind:value={password} placeholder="Password" required />
    <button type="submit">Login</button>
</form>
<p>{message}</p>
