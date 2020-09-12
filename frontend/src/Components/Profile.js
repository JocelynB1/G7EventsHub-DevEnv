import React from 'react';

class Profile extends React.Component{
    onSelect = (event) => {
        event.preventDefault();
        this.props.onSelect({requestedComponent:this.props.menulabel})
     }
    render(){
        return(
            <>
               {this.props.details.map(
          user => (
            <div key={user.user}>
                <p>{user.date_of_birth}</p>
                <p>{user.phone_number}</p>
                <p>{user.city}</p>
                <p>{user.address}</p>                
                <p>{user.first_name}</p>                  
                <p>{user.last_name}</p>
                <p>{user.email}</p>
            </div>
          ))}
            </>)
    }
}
export default Profile;