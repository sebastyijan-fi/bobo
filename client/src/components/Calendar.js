import React from 'react';

function Calendar() {
  return <div>Today's date: {new Date().toLocaleDateString()}</div>;
}

export default Calendar;
