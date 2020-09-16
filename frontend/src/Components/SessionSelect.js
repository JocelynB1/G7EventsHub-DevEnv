import React from 'react';
import { useEffect,useState } from 'react';



function SessionSelect(props) {
    const [session,setSession]=useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/sessionlist/",
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
            data => setSession(data),
        )
            .then(
    
            ).catch(error => console.log(error))
         
    
            
    
    }, []);

    let op="<label for=\"session\">Choose a session:</label><select name=\"session\" required id=\"id_session\">  <option value=\"\">--Please choose an option--</option>";
            session.forEach(
                s => {
                    op+=`  <option value="${s.description}">${s.description}</option>`
                })
                op+="</select>"
                console.log(op);         
    return (
        <>
        <div dangerouslySetInnerHTML={{__html: op}}/>

        </>)

}
export default SessionSelect;