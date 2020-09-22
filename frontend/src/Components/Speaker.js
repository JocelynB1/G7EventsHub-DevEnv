import React from 'react';
import image from './image.jpg';
import "./index.css"

export default function Speaker() {
    return (
        <div className = "speaker">
           <h1>Meet your Speaker</h1>
            <figure>
                <img src={image} className="honu" alt="Regina Honu" />
                <figcaption>
                    Say hello to <b>Regina Honu</b>.
                    Regina Honu is a Ghanaian Social Entrepreneur, 
                    software developer and founder of Soronko Solutions, 
                    a software development company in Ghana. 
                    She opened Soronko Academy, the first coding 
                    and Human-centered design school 
                    for children and young adults in West Africa.
                    
                </figcaption>
            </figure>
            
        </div>
    )
}
