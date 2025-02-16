export const API_AUTH_URL = 'http://localhost:8000/api/auth'; // Base auth url

export const loginUser = async (username, password) => {
    const res = await fetch(`${API_AUTH_URL}/token/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
  
    return res;
  }
  
  export const registerUser = async (username, password, passwordConfirm) => {
    const res = await fetch(`${API_AUTH_URL}/register/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password, password_confirm: passwordConfirm })
    });
  
    return res; // Return JSON response so the caller can handle it
  };
  
  // Optionally, handle token refresh here
 export const refreshToken = async () => {
    const refreshToken = localStorage.getItem('refresh_token');
  
    if (!refreshToken) {
      window.location.href = '/login'; // Redirect to login page if no refresh token
      return;
    }
  
    const res = await fetch(`${API_AUTH_URL}/refresh/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh: refreshToken }),
    });
  
    if (res.ok) {
      const data = await res.json();
      localStorage.setItem('access_token', data.access);
      // Retry the original request after refreshing the token
    } else {
      window.location.href = '/'; // Redirect to login page if refresh fails
    }
  };
  