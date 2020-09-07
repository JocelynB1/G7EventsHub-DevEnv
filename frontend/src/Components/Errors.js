
import React from 'react';

function Errors(props) {
    const items = props.errors.map((e) =>
      <li key={e}>
        {e}
      </li>
    );
    return (
      <ul className="errors">{items}</ul>
    );
  }

  export default Errors; 