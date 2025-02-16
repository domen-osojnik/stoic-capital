<script>
    import '../styles/forms.scss'; // Import the global styles
    import { goto } from '$app/navigation';
    import { fetchWithAuth } from '$lib/api';
    import { onMount } from 'svelte';
  
    let user = null; // Store authenticated user
    let loading = true;
  
    onMount(() => {
      const token = localStorage.getItem('access_token');
      
      if (!token) {
        goto('/login'); // Redirect if no token
        return;
      }
  
      fetchWithAuth('/auth/user/', {
        method: 'GET',
        headers: { Authorization: `Bearer ${token}` },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data?.username) {
            user = data; // Store user info
          } else {
            localStorage.removeItem('access_token');
            goto('/login'); // Redirect if invalid token
          }
        })
        .catch(() => goto('/login'))
        .finally(() => {
          loading = false;
        });
    });
  </script>    
  
<main>
      <slot /> <!-- Page content will be injected here -->
</main>