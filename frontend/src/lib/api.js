import { refreshToken } from '$lib/auth.api'; // Assuming API_URL is defined in $lib/api.js

export const API_URL = 'http://localhost:8000/api'; // Replace with your API URL

export const fetchWithAuth = async (url, options = {}) => {
  const accessToken = localStorage.getItem('access_token');

  const headers = {
    'Content-Type': 'application/json',
    ...options.headers, // Allow overriding headers
  };

  if (accessToken) {
    headers['Authorization'] = `Bearer ${accessToken}`;
  }

  const response = await fetch(`${API_URL}${url}`, {
    ...options,
    headers,
  });

  if (response.status === 401) {
    // Token expired or invalid, handle token refresh
    await refreshToken();
  }

  return response;
};

