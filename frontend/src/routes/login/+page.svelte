<style>@import '../../styles/forms.scss'; /* Import the global form styles */
</style>
<script>
  import { loginUser } from '$lib/auth.api.js'; // Your API URL file

  let username = '';
  let password = '';
  let errorMessage = '';

  const handleLogin = async () => {
    const res = await loginUser(username, password);

    if (res.ok) {
      const data = await res.json();
      // Store the JWT tokens in localStorage or cookies
      localStorage.setItem('access_token', data.access);
      localStorage.setItem('refresh_token', data.refresh);

      // Redirect after successful login (e.g., to home page)
      window.location.href = '/account';
    } else {
      const errorData = await res.json();
      errorMessage = errorData.detail || 'Login failed';
    }
  };
</script>


<div class="form-container">
    <h1>Login</h1>
    <input class="form-input" type="text" bind:value={username} placeholder="Username" />
    <input class="form-input" type="password" bind:value={password} placeholder="Password" />
    <button class="form-button" on:click={handleLogin}>Login</button>
  
    {#if errorMessage}
      <div class="error-message">{errorMessage}</div>
    {/if}
  
    <div>
      <p>Don't have an account? <a href="/register">Register here</a></p>
    </div>
  </div>
  
