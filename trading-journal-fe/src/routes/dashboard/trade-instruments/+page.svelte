<script>
    import { onMount } from 'svelte';
    import { fetchTradeInstruments, createTradeInstrument, deleteTradeInstrument } from '$lib/api';

    let instruments = [];
    let message = '';

    let symbol = '';
    let name = '';
    let type = 'futures';  // Default type
    let tick_size = '';
    let tick_value = '';
    let contract_size = '';
    let currency = 'USD';
    let exchange = '';

    const instrumentTypes = [
        { value: 'futures', label: 'Futures' },
        { value: 'stock', label: 'Stock' },
        { value: 'cfd', label: 'CFD' },
        { value: 'currency', label: 'Currency' },
        { value: 'crypto', label: 'Crypto' }
    ];

    onMount(async () => {
        try {
            instruments = await fetchTradeInstruments();
        } catch (error) {
            message = 'Error fetching trade instruments.';
        }
    });

    async function addInstrument(e) {
        e.preventDefault();
        const newInstrument = {
            symbol,
            name,
            type,
            tick_size: parseFloat(tick_size),
            tick_value: parseFloat(tick_value),
            contract_size: parseInt(contract_size),
            currency,
            exchange
        };

        try {
            const result = await createTradeInstrument(newInstrument);
            instruments.push(result);
            message = 'Instrument added successfully!';
        } catch (error) {
            message = 'Failed to add instrument.';
        }
    }

    async function removeInstrument(id) {
        try {
            await deleteTradeInstrument(id);
            instruments = instruments.filter(inst => inst.id !== id);
        } catch (error) {
            message = 'Failed to delete instrument.';
        }
    }
</script>

<h2>Trade Instruments</h2>

<form on:submit|preventDefault={addInstrument} class="form-container">
    <div class="form-column">
        <label>Symbol:</label>
        <input type="text" bind:value={symbol} required />

        <label>Name:</label>
        <input type="text" bind:value={name} required />

        <label>Type:</label>
        <select bind:value={type}>
            {#each instrumentTypes as instType}
                <option value={instType.value}>{instType.label}</option>
            {/each}
        </select>
    </div>

    <div class="form-column">
        <label>Tick Size:</label>
        <input type="number" bind:value={tick_size} required />

        <label>Tick Value:</label>
        <input type="number" bind:value={tick_value} required />

        <label>Contract Size:</label>
        <input type="number" bind:value={contract_size} required />

        <label>Currency:</label>
        <input type="text" bind:value={currency} required />
    </div>

    <div class="form-actions">
        <button type="submit" class="btn-primary">Add Instrument</button>
    </div>
</form>

{#if instruments.length > 0}
    <ul>
        {#each instruments as inst}
            <li>
                {inst.symbol} - {inst.name} ({inst.type}) 
                (Tick Size: {inst.tick_size}, Tick Value: ${inst.tick_value})
                <button on:click={() => removeInstrument(inst.id)} class="btn-secondary">Delete</button>
            </li>
        {/each}
    </ul>
{:else}
    <p>No instruments found.</p>
{/if}

<p>{message}</p>

<style>
    @import '$lib/styles/forms.css';
</style>
