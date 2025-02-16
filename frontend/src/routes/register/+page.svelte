<script>

import { registerUser } from '$lib/auth.api.js'; // Your API URL file

  let username = '';
  let password = '';
  let passwordConfirm = '';
  let errorMessage = '';

  const handleRegister = async (event) => {
    event.preventDefault(); // Prevent the form from reloading the page

    if (password !== passwordConfirm) {
      errorMessage = 'Passwords do not match';
      return;
    }

    const res = await registerUser(username, password, passwordConfirm);

    if (res.ok) {
      const data = await res.json();
      console.log('Registration successful:', data);
      // Redirect to the login page after successful registration
      window.location.href = '/login';
    } else {
      const errorData = await res.json();
      errorMessage = errorData.detail || 'Registration failed';
    }
  };
</script>

<div class="form-container">
  <h1>Register</h1>

    <input type="text" bind:value={username} placeholder="Username" class="form-input" />
    <input type="password" bind:value={password} placeholder="Password" class="form-input" />
    <input type="password" bind:value={passwordConfirm} placeholder="Confirm Password" class="form-input" />
    <button class="form-button" on:click={handleRegister}>Register</button>

  <p><a href="/login">Login here</a></p>
  {#if errorMessage}
    <div class="error-message">{errorMessage}</div>
  {/if}
</div>
