import React from 'react';
import { useEffect, useState } from 'react';



function EventTable(props) {
    // onSelect = (event) => {
    //     event.preventDefault();
    //     this.props.onSelect({ requestedComponent: this.props.menulabel })
    // }
    const [details, setDetails] = useState([]);

    useEffect(() => {
        loadDetails()

    }, []);
    let loadDetails = async () => {

        let data = await fetch("http://127.0.0.1:8000/api/myevents/",
            {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${props.token}`
                },

            }
        )
        try {
            if (!data.ok) {
                let err = await data.json()
                let errorArr = []
                Object.keys(err).map(key =>
                    errorArr.push(key + " : " + err[key].pop())
                )
                this.props.onErrors({ errors: errorArr })
            } else {
                let d = await data.json()
                console.log(d)
                await   setDetails(d)
            }
        } catch (error) { console.log(error) }
        //        fetch("http://127.0.0.1:8000/api/details/",
        //             {
        //                 method: "GET",
        //                 headers: {
        //                     "Content-Type": "application/json",
        //                     Authorization: `Token ${props.token}`
        //                 },

        //             }
        //         ).then(
        //             data => data.json()

        //         ).then(
        //             data => setDetails(data),
        //         )
        //             .then(

        //             ).catch(error => console.log(error))


        //                 console.log(td);
    }
    
    let thead = "<thead><tr><th>Name</th><th>Location</th><th>Title</th><th>Tag Line</th><th>Session</th><th>Start Date</th><th>End Date</th><th>Seats</th></tr></thead>"
    let td = "";
    details.forEach(
        event => {
            td += `<tr><td>${event.event_name}</td><td>${event.location}<td>${event.title}</td><td>${event.tag_line}</td><td>${event.session}</td><td>${event.start_date}</td><td>${event.end_date}</td><td>${event.seats}</td></tr>`
        })
    let table = "<table id=\"Table\">" + thead + "<tbody>" + td + "<tbody></table>";
    return (
        <>
            <div id="table-main">
                <br />
               
                <div dangerouslySetInnerHTML={{ __html: table }} />
            </div>
        </>)

}
export default EventTable;