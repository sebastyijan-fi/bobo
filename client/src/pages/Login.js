import React from 'react';

function Login() {
  return (
    <form>
      <label>
        Email:
        <input type="email" name="email" />
      </label>
      <label>
        Password:
        <input type="password" name="password" />
      </label>
      <input type="submit" value="Login" />
    </form>
  );
}

export default Login;
