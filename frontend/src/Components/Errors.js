
import React from 'react';

function Errors(props) {
    const items = props.errors.map((e) =>
      <li key={e}>
        {e}
      </li>
    );
    return (
      <div className="errors">
      <ul>{items}</ul>
      </div>
    );
  }

  export default Errors; 