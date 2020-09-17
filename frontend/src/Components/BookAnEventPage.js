import React from 'react';
import { useEffect, useState } from 'react';
import SessionSelect from './SessionSelect';
import EventSelect from './EventSelect';
import HiddenUserId from './HiddenUserId';



function BookAnEventPage(props) {
    // const [user, setUser] = useState([]);

    // useEffect(() => {

    // }, []);

    let postBooking = async (event) => {
        event.preventDefault();
        const formData = new FormData(document.querySelector("#form"))
        formData.append("user", document.querySelector("#id_user").value)
        formData.append("id_event", document.querySelector("#id_event").value)
        formData.append("id_session", document.querySelector("#id_session").value)
        formData.append("seats", document.querySelector("#seats").value)
        let data=   fetch("http://127.0.0.1:8000/api/booking/",
        {
            method: "POST",
            headers: {
                Authorization: `Token ${props.token}`,

            },
            body: formData
            


        }
    )
    try {

        if (!data.ok) {
            let err = await (await data).json()
            console.log(err)
            let errorArr = []
            Object.keys(err).map(key =>
                errorArr.push(key + " : " + err[key].pop())
            )
             props.onErrors({ errors: errorArr })
        }else{
            console.log("here");
         
        let d = await data
        console.log(d)

        }
    }catch  (error) { console.log(error) }
        // fetch("http://127.0.0.1:8000/api/booking/",
        //     {
        //         method: "POST",
        //         headers: {
        //             "Content-Type": "application/json",
        //             Authorization: `Token ${props.token}`,
        //             body: formData

        //         },

        //     }
        // ).then(
        //     //400
        //     data => {

        //         if (!data.ok) {
        //             //         console.log(data.text())
        //             data.json().then((err) => {
        //                 let errorArr = []
        //                 Object.keys(err).map(key =>
        //                     errorArr.push(key + " : " + err[key])
        //                 )
        //                 props.onErrors({ errors: errorArr })

        //             });
        //         } else {
        //             data.json().then(
        //                 data => {
        //                     console.log(data)
        //                 }

        //             ).catch(error =>
        //                 props.onErrors({ errors: error.text })

        //             )
        //         }
        //     }

        // )



    }
    return (
        <>  <div id="main-form">
            <div className="form" >
                <form id="form">
                    <h2>Book an Event</h2>
                    <HiddenUserId token={props.token} />
                    <EventSelect token={props.token} />
                    <SessionSelect token={props.token} />
                    <label htmlFor="seats">Seats</label>
                    <input type="number" id="seats" name="seats" />
                    <button value="Submit" onClick={postBooking} className="button" value="Submit" >Submit</button>
                </form>
            </div></div>
        </>)

}
export default BookAnEventPage;