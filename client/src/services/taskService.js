const API_URL = 'http://localhost:5000/api'; // replace with your Flask API URL

export const createTask = async (task) => {
    // similar to login/register, but to the '/tasks' endpoint
    const response = await fetch(`${API_URL}/tasks`, {
      method: 'POST',
      body: JSON.stringify(task),
      headers: { 'Content-Type': 'application/json' },
    });
    if (!response.ok) throw new Error('Error creating task');
    const data = await response.json();
    return data;
  };

  export const getTasks = async () => {
    // implement getting tasks function
  };

  export const updateTask = async (taskId, updatedTask) => {
    // implement updating task function
  };

  export const deleteTask = async (taskId) => {
    // implement deleting task function
  };
