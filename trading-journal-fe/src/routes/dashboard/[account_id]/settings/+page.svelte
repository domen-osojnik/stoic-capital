<script>
    import { onMount } from 'svelte';
    import { page } from '$app/state';
    import { fetchTradingAccount, updateTradingAccount } from '$lib/api';
    import { goto } from '$app/navigation';

    let account;
    let message = '';

    let accountId = page.params.account_id;
    let account_name = '';
    let is_default = false;

    onMount(async () => {
        try {
            account = await fetchTradingAccount(accountId);

            if (!account) {
                message = 'Account not found!';
                return;
            }

            // Pre-fill form with existing values
            account_name = account.account_name;
            is_default = account.is_default;
        } catch (error) {
            message = 'Error fetching account details.';
        }
    });

    async function updateAccount(e) {
        e.preventDefault();

        const updatedData = { account_name, is_default };

        try {
            const response = await updateTradingAccount(accountId, updatedData);

            if (response.id) {
                message = 'Account updated successfully!';
                setTimeout(() => goto(`/dashboard/${accountId}`), 1000);
            } else {
                message = 'Failed to update account.';
            }
        } catch (error) {
            message = 'An error occurred.';
        }
    }
</script>

<style>
    @import '$lib/styles/forms.css';
</style>

<h2>Edit Trading Account</h2>

{#if account}
    <form class="form-container" on:submit|preventDefault={updateAccount}>
        <div class="form-column">
            <label>Account Name:</label>
            <input type="text" bind:value={account_name} required />
        </div>

        <div class="form-column">
            <label class="checkbox-label">
                <input type="checkbox" bind:checked={is_default} />
                Set as Default Account
            </label>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-primary">Save Changes</button>
            <button type="button" class="btn-secondary" on:click={() => goto(`/dashboard/${accountId}`)}>Cancel</button>
        </div>
    </form>

    <p class="status-message">{message}</p>
{:else}
    <p>{message}</p>
{/if}
