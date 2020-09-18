import React from 'react';
import SessionSelect from './SessionSelect';
import SessionSelect1 from './SessionSelect1';
import SessionSelect2 from './SessionSelect2';
import EventSelect from './EventSelect';
import EventSelect1 from './EventSelect1';
import EventSelect2 from './EventSelect2';
import HiddenUserId from './HiddenUserId';


function BookAnEventPage(props) {
    let postBooking = async (event) => {
        event.preventDefault();
        const formData = new FormData(document.querySelector("#form"))
        formData.append("user", document.querySelector("#id_user").value)
        formData.append("id_event", document.querySelector("#id_event").value)
        formData.append("id_event1", document.querySelector("#id_event1").value)
        formData.append("id_event2", document.querySelector("#id_event2").value)
        formData.append("id_session", document.querySelector("#id_session").value)
        formData.append("id_session1", document.querySelector("#id_session1").value)
        formData.append("id_session2", document.querySelector("#id_session2").value)
        formData.append("seats", document.querySelector("#seats").value)
        formData.append("seats1", document.querySelector("#seats1").value)
        formData.append("seats2", document.querySelector("#seats2").value)
        let data = fetch("http://127.0.0.1:8000/api/booking/",
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
                if (typeof(data) === 'object' && data !== null){
                
                Object.keys(err).map(key =>
                    errorArr.push(key + " : " + err[key].pop())
                )
                props.onErrors({ errors: errorArr })
                }
            } else {
    

                let d = await data
                let errorArr = []

                if (typeof(d) === 'object' && data !== null){
                    Object.keys(d).map(key =>
                        errorArr.push(key + " : " + d[key].pop())
                    )
                    props.onErrors({ errors: errorArr })
                        
                }
    
            }
        } catch (error) { console.log(error) }
    }
    return (
        <>

          <div id="main-form">
            <div className="form" >
                <form id="form">
                    <h2 id="bookevents">Book Events</h2>
                    <div className='forms'>
                        <div className='row'>
                            <div className='column'>
                                <div className='column-one'>
                                    <h2>
                                        Morning
                                    </h2>
                                    <EventSelect token={props.token} />
                                    <SessionSelect token={props.token} />
                                    <label htmlFor="seats">Seats</label>
                                    <input type="number" id="seats" name="seats" />
                                </div>
                            </div>
                            <div className='column'>
                                <div className='column-two'>
                                    <h2>Afternoon</h2>
                                    <EventSelect1 token={props.token} />
                                    <SessionSelect1 token={props.token} />
                                    <label htmlFor="seats1">Seats</label>
                                    <input type="number" id="seats1" name="seats1" />
                                    <button value="Submit" onClick={postBooking} className="button" id="submit1" value="Submit" >Submit</button>

                                </div>
                            </div>
                            <div className='column'>
                                <div className='column-three'>
                                    <h2>Evening</h2>
                                    <EventSelect2 token={props.token} />
                                    <SessionSelect2 token={props.token} />
                                    <label htmlFor="seats2">Seats</label>
                                    <input type="number" id="seats2" name="seats2" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <HiddenUserId token={props.token} />

                </form>
            </div></div>
        </>)

}
export default BookAnEventPage;