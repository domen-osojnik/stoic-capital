<script>
    import { fetchWithAuth } from '$lib/api.js';  // Adjust the path to your api.js
    
    let account_name = '';
    let currency = '';
    let balance = 0;
    let errorMessage = '';
  
    const handleCreateAccount = async () => {
      const res = await fetchWithAuth('/core/accounts/', {
        method: 'POST',
        body: JSON.stringify({ account_name, currency, balance }),
      });
  
      if (res.ok) {
        window.location.href = '/account';  // Redirect to the account list page after creation
      } else {
        const errorData = await res.json();
        errorMessage = errorData.detail || 'Account creation failed';
      }
    };
  </script>
  
  <style>
    .create-account-form {
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 700px;
    }
  
    .input {
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  
    .submit-btn {
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  </style>
  
  <div>
    <h1>Create a New Account</h1>
  
    {#if errorMessage}
      <div class="error-message">{errorMessage}</div>
    {/if}
  
    <form class="create-account-form" on:submit|preventDefault={handleCreateAccount}>
      <input class="input" type="text" placeholder="Account name" bind:value={account_name} required />

      <input class="input" type="text" placeholder="Starting balance" bind:value={balance} required />

      <input class="input" type="text" placeholder="Currency" bind:value={currency} required />
      <button class="submit-btn" type="submit">Create Account</button>
    </form>
  </div>
  