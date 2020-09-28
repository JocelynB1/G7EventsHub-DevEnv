import React from 'react';
import './landing.css';

export default function AfternoonSide() {
    return (
        <div className = "afternoon">
            <h1>Afternoon Events</h1>
            <figure className = "one">
                <img src ="https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt = "Event" />
                <figcaption> 
                            <a href = "/"><b>Sat, Sep 26, 2020 2:00 AM </b><br/><i>Hold On We're Coming</i></a>
                    </figcaption>
            </figure>

            <figure className = "two">
                <img src ="https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?cs=srgb&dl=pexels-fauxels-3184418.jpg&fm=jpg" alt = "Event" />
               <figcaption> 
                            <a href = "/"><b>Fri, Sep 25, 2020 11:00 PM</b><br/><i>Baking with Our Buds</i></a>
                    </figcaption>
            </figure>

            <figure className = "three">
                <img src ="https://images.pexels.com/photos/2740956/pexels-photo-2740956.jpeg?cs=srgb&dl=pexels-prateek-katyal-2740956.jpg&fm=jpg" alt = "Event" />
                <figcaption> 
                            <a href = "/"><b>Fri, Oct 2, 2020 12:00 AM </b><br/><i>Comedy Crossing</i></a>
                    </figcaption>
            </figure>

            {/* <figure className = "four">
                <img src ="https://images.pexels.com/photos/7096/people-woman-coffee-meeting.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt = "Event" />
                <figcaption> 
                        <a href = "/"><b>Sat, Oct 3, 2020 4:00 PM</b><br/><i>Everygirls Rise</i></a>
                </figcaption>
            </figure> */}
            <a href = "/"><b>See more events....</b></a>
        
        </div>
    )
}
