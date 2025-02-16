<script>
    import { API_URL, fetchWithAuth } from '$lib/api';  // Import API URL
    import { onMount } from 'svelte';
    
    let account = {};  // Store individual account details
    let errorMessage = '';  // Store error messages
  
    // Get the account ID from the URL parameter
    export let params;
    const accountId = params.accountid;
  
    // Fetch account details
    const fetchAccountDetails = async () => {
      try {
        const res = await fetchWithAuth(`${API_URL}/core/accounts/${accountId}/`, {
          method: 'GET'
        });
  
        if (res.ok) {
          account = await res.json();
        } else {
          const errorData = await res.json();
          errorMessage = errorData.detail || 'Failed to fetch account details';
        }
      } catch (error) {
        errorMessage = 'An error occurred';
      }
    };
  
    // Fetch account details when component is mounted
    onMount(fetchAccountDetails);
  </script>
  
  <style>
    /* Add any custom styles for the account details page */
    .account-details {
      padding: 20px;
    }
  
    .error-message {
      color: red;
    }
  </style>
  
  <div class="account-details">
    {#if errorMessage}
      <div class="error-message">{errorMessage}</div>
    {/if}
  
    {#if account}
      <h2>{account.name}</h2>
      <p>Balance: {account.balance} {account.currency}</p>
      <!-- Add more details here as needed -->
    {/if}
  </div>
  