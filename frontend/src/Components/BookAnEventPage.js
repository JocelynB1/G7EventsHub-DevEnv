import React from 'react';
import { useEffect, useState } from 'react';
import SessionSelect from './SessionSelect';
import EventSelect from './EventSelect';
import HiddenUserId from './HiddenUserId';



function BookAnEventPage(props) {
    const [user, setUser] = useState([]);

    useEffect(() => {
        const formData = new FormData(document.querySelector("#form"))
        formData.append("id_user", document.querySelector("#id_user").value)
        formData.append("id_event", document.querySelector("#id_event").value)
        formData.append("id_session", document.querySelector("#id_session").value)
        formData.append("seats", document.querySelector("#seats").value)
        fetch("http://127.0.0.1:8000/api/booking/",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${props.token}`,
                    body: formData

                },

            }
        ).then(
           //400
           data => {

            if (!data.ok) {
                //         console.log(data.text())
                data.json().then((err) => {
                    let errorArr = []
                    Object.keys(err).map(key =>
                        errorArr.push(key + " : " + err[key])
                    )
                    this.props.onErrors({ errors: errorArr })

                });
            } else {
                data.json().then(
                    data => {
                        console.log(data)
                    }

                ).catch(error =>
                    this.props.onErrors({ errors: error.text })

                )
            }
        }

        )



    }, []);

    
    return (
        <>  <div id="main">
            <div className="form" >
                <form id="form">
                    <h2>Book an Event</h2>
                    <HiddenUserId token={props.token} />
                    <EventSelect token={props.token} />
                    <SessionSelect token={props.token} />
                    <label htmlFor="seats">Seats</label>
                    <input type="number" id="seats" name="seats" />
                    <input type="submit" class="button"  value="Submit"/>
                </form>
            </div></div>
        </>)

}
export default BookAnEventPage;