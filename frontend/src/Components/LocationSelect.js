import React from 'react';
import { useEffect,useState } from 'react';



function LocationSelect(props) {
    const [location,setLocation]=useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/locationlist/",
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
            data => setLocation(data),
        )
            .then(
    
            ).catch(error => console.log(error))
         
    
            
    
    }, []);

    let op="<label for=\"location\">Choose a location:</label><select name=\"location\" required id=\"id_location\">  <option value=\"\">--Please choose an option--</option>";
            location.forEach(
                s => {
                    op+=`  <option value="${s.id}">${s.name},${s.city}</option>`
                })
                op+="</select>"
                console.log(op);         
    return (
        <>
        <div dangerouslySetInnerHTML={{__html: op}}/>

        </>)

}
export default LocationSelect;