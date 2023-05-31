import React from 'react';

function TaskList() {
  // this will be replaced with actual data in the future
  const tasks = ['Task 1', 'Task 2', 'Task 3'];

  return (
    <ul>
      {tasks.map((task, index) => (
        <li key={index}>{task}</li>
      ))}
    </ul>
  );
}

export default TaskList;
