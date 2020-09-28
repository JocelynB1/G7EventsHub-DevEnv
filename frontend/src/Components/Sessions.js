import React from 'react'
import AfternoonSide from './AfternoonSide'
import EveningSide from './EveningSide'
import MorningSide from './MorningSide'
import './landing.css';

export default function Sessions() {
    return (
        <div className = "sessions">
            <MorningSide/>
            <AfternoonSide/>
            <EveningSide/>
        </div>
    )
}
