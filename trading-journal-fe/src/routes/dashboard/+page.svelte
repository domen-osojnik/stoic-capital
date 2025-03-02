<script>
    import { onMount } from 'svelte';
    import { fetchTradingAccounts } from '$lib/api';
    import { goto } from '$app/navigation';

    let accounts = [];
    let message = '';

    onMount(async () => {
        try {
            accounts = await fetchTradingAccounts();

            if (accounts.length === 0) {
                message = 'No trading accounts found. Please create one.';
            }
        } catch (error) {
            message = 'Error fetching accounts.';
        }
    });

    function goToCreateAccount() {
        goto('/dashboard/create');
    }
</script>

<h2>Select a Trading Account</h2>

{#if message}
    <p>{message}</p>
    <button on:click={goToCreateAccount}>Create Account</button>
{:else}
    <ul>
        {#each accounts as account}
            <li>
                <button on:click={() => goto(`/dashboard/${account.id}`)}>
                    {account.account_name} - ${account.account_size}
                </button>
            </li>
        {/each}
    </ul>

    <button on:click={goToCreateAccount}>Create New Account</button>
{/if}
