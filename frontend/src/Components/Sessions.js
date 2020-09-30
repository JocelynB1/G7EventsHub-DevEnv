import React from 'react'
import MidmorningSide from './MidmorningSide'
import AfternoonSide from './AfternoonSide'
import MorningSide from './MorningSide'
import './landing.css';
import { useEffect, useState } from 'react';

export default function Sessions(props) {
    return (
        <div className = "sessions">
            <MorningSide  {... props} />
            <MidmorningSide  {... props} />
            <AfternoonSide  {... props} />
        </div>
    )
}
