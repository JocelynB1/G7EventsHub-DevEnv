import React from 'react';
import { useEffect, useState } from 'react';



function Profile(props) {
    // onSelect = (event) => {
    //     event.preventDefault();
    //     this.props.onSelect({ requestedComponent: this.props.menulabel })
    // }
    const [details, setDetails] = useState([]);

    useEffect(() => {
        loadDetails()

    }, []);
    let loadDetails = async () => {

        let data = await fetch("http://127.0.0.1:8000/api/details/",
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
    let thead = "<thead><tr><th>First Name</th><th>Last Name</th><th>Email</th><th>City</th><th>Address</th><th>Phone Number</th><th>Date of Birth</th></tr></thead>"
    let td = "";
    details.forEach(
        user => {
            td += `<tr><td>${user.first_name}</td><td>${user.last_name}</td><td>${user.email}</td><td>${user.city}</td><td>${user.address}</td><td>${user.phone_number}</td><td>${user.date_of_birth}</td></tr>`
        })
    let table = "<table>" + thead + "<tbody>" + td + "<tbody></table>";
    return (
        <>
            <div id="table-main">
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <div dangerouslySetInnerHTML={{ __html: table }} />
            </div>
        </>)

}
export default Profile;