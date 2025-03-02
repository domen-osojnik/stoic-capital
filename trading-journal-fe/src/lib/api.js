import { authStore, login, logout } from '$lib/stores/auth';

const API_URL = 'http://localhost:8000/api';

function getAuthToken() {
    let token;
    authStore.subscribe(user => {
        token = user ? user.token : null;
    })();
    return token;
}

// ✅ Function to check if the token is expired
function isTokenExpired(token) {
    if (!token) return true;

    const payload = JSON.parse(atob(token.split('.')[1]));
    const expiry = payload.exp * 1000; // Convert to milliseconds
    return Date.now() >= expiry;
}

// ✅ Function to refresh the token
async function refreshToken() {
    let refresh;
    authStore.subscribe(user => {
        refresh = user ? user.refresh : null;
    })();

    if (!refresh) {
        logout(); // No refresh token? Force logout.
        return null;
    }

    const response = await fetch(`${API_URL}/token/refresh/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh }),
    });

    if (!response.ok) {
        logout(); // Refresh failed? Force logout.
        return null;
    }

    const data = await response.json();
    login({ token: data.access, refresh }); // Update auth store with new token
    return data.access;
}

// ✅ Wrapper to handle API requests & auto-refresh token (except login/register)
async function apiRequest(endpoint, method = 'GET', body = null, skipRefresh = false) {
    let token = getAuthToken();

    // 🚀 Only refresh the token if it's expired & we are not skipping it
    if (!skipRefresh && isTokenExpired(token)) {
        token = await refreshToken();
        if (!token) return null; // 🚀 Stop request if refresh failed
    }

    const headers = { 'Content-Type': 'application/json' };
    if (token) headers['Authorization'] = `Bearer ${token}`;

    const response = await fetch(`${API_URL}${endpoint}`, {
        method,
        headers,
        body: body ? JSON.stringify(body) : null,
    });

    return response.json();
}

// ✅ API functions using auto-refresh logic
export async function loginUser(credentials) {
    return await apiRequest('/token/', 'POST', credentials, true); // 🚀 Skip refresh
}

export async function registerUser(userData) {
    return await apiRequest('/accounts/register/', 'POST', userData, true); // 🚀 Skip refresh
}

export async function fetchTradingAccounts() {
    return await apiRequest('/accounts/trading-accounts/');
}

export async function createTradingAccount(accountData) {
    return await apiRequest('/accounts/trading-accounts/', 'POST', accountData);
}

// ✅ PATCH: Update a trading account
export async function updateTradingAccount(accountId, updatedData) {
    return await apiRequest(`/accounts/trading-accounts/${accountId}/`, 'PATCH', updatedData);
}

// ✅ GET: Fetch a single trading account
export async function fetchTradingAccount(accountId) {
    return await apiRequest(`/accounts/trading-accounts/${accountId}/`, 'GET');
}

export async function fetchTradeInstruments() {
    return await apiRequest('/trading-data/trade-instruments/');
}

export async function createTradeInstrument(instrumentData) {
    return await apiRequest('/trading-data/trade-instruments/', 'POST', instrumentData);
}

export async function updateTradeInstrument(instrumentId, updatedData) {
    return await apiRequest(`/trading-data/trade-instruments/${instrumentId}/`, 'PATCH', updatedData);
}

// ✅ New DELETE function
export async function deleteTradeInstrument(instrumentId) {
    return await apiRequest(`/trading-data/trade-instruments/${instrumentId}/`, 'DELETE');
}
