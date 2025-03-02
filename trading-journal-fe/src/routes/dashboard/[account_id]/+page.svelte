<script>
    import { onMount } from 'svelte';
    import { page } from '$app/state';
    import { fetchTradingAccounts } from '$lib/api';

    let account;
    let message = '';

    onMount(async () => {

        let accountId = page.params.account_id;

        try {
            const accounts = await fetchTradingAccounts();
            account = accounts.find(acc => acc.id == accountId);

            if (!account) {
                message = 'Account not found!';
            }
        } catch (error) {
            message = 'Error fetching account data.';
        }
    });
</script>

{#if account}
    <h2>{account.account_name}</h2>
    <p>Account Size: ${account.account_size}</p>
    <p>Max Drawdown: {account.max_total_drawdown}%</p>
    <p>Daily Drawdown: {account.max_daily_drawdown}%</p>
{:else}
    <p>{message}</p>
{/if}
