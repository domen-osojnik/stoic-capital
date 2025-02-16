<script>
  import { fetchWithAuth } from '$lib/api.js';  // Adjust the path to your api.js

  let accounts = [];
  let errorMessage = '';

  import { onMount } from 'svelte';

  onMount(async () => {
    try {
      const res = await fetchWithAuth('/core/accounts/');  // Use fetchWithAuth instead of fetch
      if (res.ok) {
        accounts = await res.json();
      } else {
        errorMessage = 'Failed to fetch accounts';
      }
    } catch (error) {
      errorMessage = 'An error occurred while fetching accounts';
    }
  });
</script>

<style>
/* Account Container */
.account-container {
  padding: 20px;
  background-color: #ecf0f1;
  color: #34495e;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 50px auto;
}

/* Heading */
h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 20px;
}

/* Error Message */
.error-message {
  color: #e74c3c;
  text-align: center;
  margin-top: 10px;
  font-size: 14px;
  padding: 10px;
  border: 1px solid #e74c3c;
  border-radius: 4px;
  background-color: #f9ebea;
}

/* Account List Styles */
.account-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

/* Account Item Styles */
.account-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  padding: 15px;
  border-radius: 6px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.account-item:hover {
  transform: scale(1.02);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

.account-name {
  font-size: 18px;
  color: #2c3e50;
}

.account-item:active {
  transform: scale(1);
}

/* No Accounts Message */
.no-accounts {
  text-align: center;
  padding: 20px;
}

.no-accounts p {
  font-size: 16px;
  color: #7f8c8d;
}

/* Create Account Button */
.create-account {
  padding: 12px 20px;
  background-color: #16a085;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.create-account:hover {
  background-color: #1abc9c;
}

.create-account:focus {
  outline: none;
}

</style>

<div class="account-container">
  {#if errorMessage}
    <div class="error-message">{errorMessage}</div>
  {/if}

  {#if accounts.length > 0}
  <h1>Select account</h1>
    <div class="account-list">
      {#each accounts as account}
        <div class="account-item" on:click={() => window.location.href = `/account/${account.id}`}>
          <div class="account-name">{account.account_name} {account.balance} {account.currency}</div>
        </div>
      {/each}
      <button class="create-account" on:click={() => window.location.href = '/account/create'}>
        Create a New Account
      </button>
    </div>
  {:else}
    <div class="no-accounts">
      <p>You don't have any accounts yet.</p>
      <button class="create-account" on:click={() => window.location.href = '/account/create'}>
        Create a New Account
      </button>
    </div>
  {/if}
</div>

