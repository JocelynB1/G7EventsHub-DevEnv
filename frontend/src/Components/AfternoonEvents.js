import React from 'react';
import { useEffect, useState } from 'react';

function AfternoonEvents(props) {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/afternooneventlist/",
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
            data => setEvents(data),
        )
            .then(

            ).catch(error => console.log(error))




    }, [props.token]);

    let postBooking = async (e, id, session) => {
        const formData = new FormData()
        formData.append("event", id)
        formData.append("session", session)
        formData.append("seats", 1)
        let data = await fetch("http://127.0.0.1:8000/api/booking/",
            {
                method: "POST",
                headers: {
                    'Accept': 'application/json',
                    Authorization: `Token ${props.token}`,
                    'Content-Type': 'application/json'

                },
                body: JSON.stringify(Object.fromEntries(formData))



            }
        )
        try {

            if (data.status == 200) {
                props.onSuccess({
                    requestedComponent: "My events",
                    message: "Booking successful"
                })
            } else {

                if (!data.ok) {
                    let err = await data.json()
                    let errorArr = []
                    if (typeof (data) === 'object' && data !== null) {

                        Object.keys(err).map(key =>
                            errorArr.push(key + " : " + err[key].pop())
                        )
                        props.onErrors({ errors: errorArr })
                    }
                } else {


                    let d = await data
                    let errorArr = []

                    if (typeof (d) === 'object' && data !== null) {
                        Object.keys(d).map(key =>
                            errorArr.push(key + " : " + d[key].pop())
                        )
                        props.onErrors({ errors: errorArr })

                    }

                }
            }
        } catch (error) { console.log(error) }
    }

    if (events.length == 1) {
        return (<>
            <h2>You have been booked for the following:</h2>
            <form id={events[0].id} >
                <figure className={events[0].id}>
                    <img src={events[0].image} alt={events[0].title}></img>
                    <figcaption> <b>{events[0].tag_line}</b>
                        <br /><i>{events[0].title}</i></figcaption>
                </figure>
            </form>
        </>
        )

    }
    return (
        events.map(
            row => {
                return (
                    <form id={row.id} onClick={(e) => postBooking(e, row.id, row.session)}>
                        <figure className={row.id}>
                            <img src={row.image} alt={row.title}></img>
                            <figcaption> <b>{row.tag_line}</b>
                                <br /><i>{row.title}</i></figcaption>
                        </figure>
                    </form>)

            }
        )
    )
}

export default AfternoonEvents;