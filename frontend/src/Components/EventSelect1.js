import React from 'react';
import { useEffect, useState } from 'react';



function EventSelect1(props) {
    const [event, setEvent] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/eventlist/",
            {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${props.token}`
                },

            }
        ).then(
            data => data.json()

        ).then(
            data => setEvent(data),
        )
            .then(

            ).catch(error => console.log(error))




    }, []);

    let op = "<label for=\"event1\">Choose a event:</label><select name=\"event1\" required id=\"id_event1\">  <option value=\"\">--Please choose an option--</option>";
    event.forEach(
        s => {
            op += `  <option value="${s.id}">${s.name}:${s.tag_line}</option>`
        })
    op += "</select>"
    return (
        <>
            <div dangerouslySetInnerHTML={{ __html: op }} />

        </>)

}
export default EventSelect1;