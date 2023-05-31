export const setToken = (token) => {
    // save the JWT to localStorage
    localStorage.setItem('token', token);
  };

  export const getToken = () => {
    // get the JWT from localStorage
    return localStorage.getItem('token');
  };

  export const clearToken = () => {
    // remove the JWT from localStorage
    localStorage.removeItem('token');
  };
