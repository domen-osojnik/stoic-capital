<script>
    import { createTradingAccount } from '$lib/api';
    import { goto } from '$app/navigation';
    
    let account_name = '';
    let account_size = '';
    let max_total_drawdown = '';
    let max_daily_drawdown = '';
    let is_default = false;
    let message = '';

    async function handleCreateAccount(e) {
        e.preventDefault();
        const accountData = {
            account_name,
            account_size: parseFloat(account_size),
            max_total_drawdown: parseFloat(max_total_drawdown),
            max_daily_drawdown: parseFloat(max_daily_drawdown),
            is_default,
        };

        try {
            const newAccount = await createTradingAccount(accountData);
            if (newAccount.id) {
                message = 'Account created successfully!';
                setTimeout(() => goto(`/dashboard/${newAccount.id}`), 1000);
            } else {
                message = 'Failed to create account.';
            }
        } catch (error) {
            message = 'An error occurred.';
        }
    }
</script>

<!-- 📌 Import the global form styles -->
<style>
    @import '$lib/styles/forms.css';
</style>

<h2>Create a New Trading Account</h2>

<form class="form-container" on:submit|preventDefault={handleCreateAccount}>
    <div class="form-column">
        <label>Account Name:</label>
        <input type="text" bind:value={account_name} required />

        <label>Account Size ($):</label>
        <input type="number" bind:value={account_size} required />
    </div>

    <div class="form-column">
        <label>Max Total Drawdown (%):</label>
        <input type="number" bind:value={max_total_drawdown} required />

        <label>Max Daily Drawdown (%):</label>
        <input type="number" bind:value={max_daily_drawdown} required />

        <label class="checkbox-label">
            <input type="checkbox" bind:checked={is_default} />
            Set as Default Account
        </label>
    </div>

    <div class="form-actions">
        <button type="submit" class="btn-primary">Create Account</button>
        <button type="button" class="btn-secondary" on:click={() => goto('/dashboard')}>Cancel</button>
    </div>
</form>

<p class="status-message">{message}</p>
