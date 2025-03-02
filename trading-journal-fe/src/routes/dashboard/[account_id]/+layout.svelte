<script>
    import { page } from '$app/state';
    
    let accountId = page.params.account_id;
</script>
<nav>
    {#if accountId }
        <a href="/dashboard/{accountId}/settings">Settings</a>
    {/if}
</nav>
<slot />
