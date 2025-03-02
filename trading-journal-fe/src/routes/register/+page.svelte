<script>
    import { registerUser } from '$lib/api';
    import { goto } from '$app/navigation';

    let username = '';
    let email = '';
    let password = '';
    let password2 = '';
    let message = '';

    async function handleRegister(e) {
        e.preventDefault();
        const data = { username, email, password, password2 };

        try {
            const result = await registerUser(data);
            if (result.id) {
                message = 'Registration successful! Redirecting to login...';
                setTimeout(() => goto('/login'), 2000);
            } else {
                message = result.detail || 'Registration failed';
            }
        } catch (error) {
            message = 'An error occurred.';
        }
    }
</script>

<h2>Register</h2>
<form on:submit|preventDefault={handleRegister}>
    <input type="text" bind:value={username} placeholder="Username" required />
    <input type="email" bind:value={email} placeholder="Email" required />
    <input type="password" bind:value={password} placeholder="Password" required />
    <input type="password" bind:value={password2} placeholder="Confirm Password" required />
    <button type="submit">Register</button>
</form>
<p>{message}</p>
<p>Already have an account? <a href="/login">Login here</a></p>
