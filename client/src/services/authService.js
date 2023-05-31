const API_URL = 'http://localhost:5000/api'; // replace with your Flask API URL

export const login = async (email, password) => {
  // Send a POST request to the '/login' endpoint with email and password
  const response = await fetch(`${API_URL}/login`, {
    method: 'POST',
    body: JSON.stringify({ email, password }),
    headers: { 'Content-Type': 'application/json' },
  });
  if (!response.ok) throw new Error('Login error');
  const data = await response.json();
  return data;
};

export const register = async (email, password) => {
  // similar to login, but to the '/register' endpoint
  const response = await fetch(`${API_URL}/register`, {
    method: 'POST',
    body: JSON.stringify({ email, password }),
    headers: { 'Content-Type': 'application/json' },
  });
  if (!response.ok) throw new Error('Registration error');
  const data = await response.json();
  return data;
};

export const logout = async () => {
  // implement logout function
};
