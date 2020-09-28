import React from 'react';
import './landing.css';

export default function MorningSide() {
    return (
        <div className = "morning">
            <h1>Morning Events</h1>

            <figure className = "one">
                    <img src="https://images.pexels.com/photos/1708936/pexels-photo-1708936.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="Event"/>       
                     <figcaption> 
                            <a href = "/"><b>Thu, Sep 24, 2020 6:30 PM </b><br/><i>A LADY'S GUIDE TO BOTANY</i></a>
                    </figcaption>
            </figure>

            <figure className = "two">
                <img src ="https://images.pexels.com/photos/159400/television-camera-men-outdoors-ballgame-159400.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500://www.freepik.com/https://www.freepik.com/free-vector/neon-retro-lights-cyber-monday_10071194.htm#page=1&query=events&position=6-photo/rear-side-audiences-sitting-listening-speackers-stage_2786344.htm#page=1&query=events&position=5" alt = "Event" />
                <figcaption> 
                    <a href = "/"><b>Tue, Sep 29, 2020 1:00 AM 2020</b> <br/><i> Ain't Cancelled Series</i></a>
                </figcaption>
            </figure>

            <figure className = "three">
                <img src ="https://images.pexels.com/photos/316465/pexels-photo-316465.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260" alt = "Event" />
                <figcaption> 
                    <a href = "/"><b>Fri, Sep 25, 2020 11:00 PM</b> <i>Diamond Bound 6.0 ONLINE</i></a>
                </figcaption>
            </figure>

            {/* <figure className = "four">
                <img src ="https://images.pexels.com/photos/2277784/pexels-photo-2277784.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt = "Event" />
                <figcaption> 
                    <a href = "/"><b>Thu, Oct 8, 2020 12:00 AM </b> <br/> <i>The Call Within</i></a>
                </figcaption>
            </figure> */}

            <a href = "/"><b>See more events....</b></a>
            
        </div>
    )
}
