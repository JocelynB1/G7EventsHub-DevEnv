// import React from 'react';
// import { useEffect,useState } from 'react';



// function HiddenUserId(props) {
//     const [user,setUser]=useState([]);

//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/api/details/",
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
//             data => setUser(data),
//         )
//             .then(
    
//             ).catch(error => console.log(error))
         
    
            
    
//     }, []);

//     let id="";
   
//                     id+=`${user_id}`
                
//     return (
//         <>
//       <input id="id_user" name="id_user" type="hidden" value={id}></input>
//       <input id="user" name="user" type="hidden" value={id}></input>

//         </>)

// }
// export default HiddenUserId;