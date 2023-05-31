import React from 'react';

function Register() {
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
      <input type="submit" value="Register" />
    </form>
  );
}

export default Register;
